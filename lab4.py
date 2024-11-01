# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 06:48:45 2024

@author: Karol Diaz
"""

import serial
import serial
import numpy as np
import pywt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
from datetime import datetime
import time

# Configuración del puerto serial
port = 'COM5'  # Cambia 'COM3' por el puerto correspondiente
baud_rate = 9600  # Tasa de baudios, misma que en Arduino
sampling_rate = 1000  # Frecuencia de muestreo (ajustable según tu configuración)
duration = 5 * 60  # Tiempo de grabación en segundos (5 minutos)

# Establece la conexión serial
ser = serial.Serial(port, baud_rate)
time.sleep(2)  # Esperar a que el puerto serial se estabilice

print("Iniciando adquisición de ECG...")
ecg_data = []
start_time = time.time()

try:
    # Lee datos hasta alcanzar el tiempo de duración
    while time.time() - start_time < duration:
        if ser.in_waiting > 0:
            # Lee y almacena el dato, eliminando caracteres extraños
            line = ser.readline().decode('utf-8').strip()
            if line.isdigit():  # Filtra datos no numéricos
                ecg_data.append(int(line))

    print("Adquisición completa.")
    
except KeyboardInterrupt:
    print("Adquisición interrumpida.")

# Cierra el puerto serial
ser.close()

# Convertir datos a un array de numpy
ecg_data = np.array(ecg_data)

# ---- Estadísticos y gráficos de la señal cruda ----
mean_value = np.mean(ecg_data)
std_value = np.std(ecg_data)
var_value = np.var(ecg_data)

# Tiempo de muestreo
time_axis = np.arange(len(ecg_data)) / sampling_rate

# Gráfica de la señal ECG cruda con detalles
plt.figure(figsize=(10, 4))
plt.plot(time_axis, ecg_data)
plt.title(f"Señal ECG Cruda (Fs={sampling_rate} Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.text(0.05, 0.95, f"Media: {mean_value:.2f}\nDesviación estándar: {std_value:.2f}\nVarianza: {var_value:.2f}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
plt.show()

# ---- Diseño del filtro pasa banda ----
# Justificación del filtro: Se elige un pasa banda de 0.5-40 Hz para capturar las frecuencias principales de ECG y eliminar ruido.
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Aplicar filtro pasa banda a la señal ECG
filtered_data = bandpass_filter(ecg_data, lowcut=0.5, highcut=40.0, fs=sampling_rate, order=4)

print("Diseño del Filtro Pasa Banda:")
print(f"Frecuencia de corte baja: 0.5 Hz")
print(f"Frecuencia de corte alta: 40.0 Hz")
print(f"Frecuencia de muestreo: {sampling_rate} Hz")
print(f"Orden del filtro: 4")
print(f"Tipo de filtro: Butterworth, para respuesta suave en la banda de paso")

# ---- Identificación de picos R ----
# Encuentra los picos de la señal filtrada para calcular intervalos R-R
peaks, _ = find_peaks(filtered_data, distance=sampling_rate*0.6)  # Ajuste según la frecuencia cardíaca
RR_intervals = np.diff(peaks) / sampling_rate  # Intervalos R-R en segundos

# Estadísticos de HRV
mean_RR = np.mean(RR_intervals)
std_RR = np.std(RR_intervals)

print("Análisis estadístico de HRV:")
print(f"Media de intervalos R-R (mean_RR): {mean_RR:.3f} s")
print(f"Desviación estándar de intervalos R-R (std_RR): {std_RR:.3f} s")
print("Interpretación: Una media R-R elevada puede indicar una frecuencia cardíaca baja. Una desviación alta sugiere alta variabilidad cardíaca, asociada a un mejor tono vagal.")

# ---- Transformada Wavelet Continua para HRV ----
# Selección de la wavelet Morlet para HRV
wavelet = 'morl'
scales = np.arange(1, 128)  # Ajustar el rango de escalas para cubrir la banda de frecuencias deseada

# Aplicar la transformada wavelet continua
coefficients, frequencies = pywt.cwt(RR_intervals, scales, wavelet, sampling_period=1/sampling_rate)

# Visualización del espectrograma
plt.figure(figsize=(10, 6))
plt.imshow(np.abs(coefficients), extent=[0, len(RR_intervals), frequencies[-1], frequencies[0]], 
           aspect='auto', cmap='viridis')
plt.colorbar(label='Magnitud')
plt.xlabel('Intervalo R-R')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma de HRV usando CWT')
plt.show()

# ---- Análisis en bandas de frecuencia ----
low_frequency_band = (0.04, 0.15)  # Banda de baja frecuencia (LF)
high_frequency_band = (0.15, 0.4)  # Banda de alta frecuencia (HF)

# Potencia en LF y HF
lf_power = np.sum(np.abs(coefficients[(frequencies >= low_frequency_band[0]) & 
                                      (frequencies <= low_frequency_band[1]), :])**2)
hf_power = np.sum(np.abs(coefficients[(frequencies >= high_frequency_band[0]) & 
                                      (frequencies <= high_frequency_band[1]), :])**2)

print("Espectrograma de HRV usando la Wavelet Morlet:")
print("La wavelet Morlet es adecuada para el análisis de HRV porque permite una buena resolución en frecuencia,")
print("capturando variaciones dinámicas en las bandas de LF y HF.")
print(f"Potencia en banda de baja frecuencia (LF): {lf_power:.2f}")
print(f"Potencia en banda de alta frecuencia (HF): {hf_power:.2f}")
print("Análisis de frecuencias: La banda LF (0.04-0.15 Hz) refleja el tono simpático y parasimpático, mientras que")
print("la banda HF (0.15-0.4 Hz) está asociada principalmente con la actividad parasimpática. Cambios en estas")
print("potencias reflejan la respuesta autónoma del corazón.")

# Visualización de la potencia espectral en bandas LF y HF
plt.figure(figsize=(10, 4))
plt.plot(frequencies, np.sum(np.abs(coefficients)**2, axis=1))
plt.axvline(x=low_frequency_band[0], color='blue', linestyle='--', label='LF Start')
plt.axvline(x=low_frequency_band[1], color='blue', linestyle='--', label='LF End')
plt.axvline(x=high_frequency_band[0], color='green', linestyle='--', label='HF Start')
plt.axvline(x=high_frequency_band[1], color='green', linestyle='--', label='HF End')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Potencia espectral')
plt.title('Distribución de la potencia espectral en bandas LF y HF')
plt.legend()
plt.show()
