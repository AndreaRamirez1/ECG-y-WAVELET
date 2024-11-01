# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:00:55 2024

@author: Karol Diaz
"""

import serial
import numpy as np
import pywt
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import time
import os

# Configuración del puerto serial y adquisición
port = 'COM5'  # Cambia según el puerto correspondiente
baud_rate = 9600
sampling_rate = 1000  # Frecuencia de muestreo en Hz
duration = 5 * 60  # Duración en segundos (5 minutos)
file_path = "ecg_data.npy"  # Archivo para guardar/cargar los datos

# Preguntar si se quiere adquirir una nueva señal
overwrite = input("¿Deseas adquirir una nueva señal ECG? (sí/no): ").strip().lower()

# Adquirir y guardar la señal ECG si no existe o si se quiere sobrescribir
if overwrite == 'sí' or not os.path.exists(file_path):
    ser = serial.Serial(port, baud_rate)
    time.sleep(2)  # Espera para estabilizar la conexión

    print("Iniciando adquisición de ECG...")
    ecg_data = []
    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line.isdigit():
                    ecg_data.append(int(line))

        print("Adquisición completa.")
        np.save(file_path, ecg_data)
        print("Señal ECG guardada en", file_path)

    except KeyboardInterrupt:
        print("Adquisición interrumpida.")
    finally:
        ser.close()

else:
    print("Cargando señal ECG guardada...")
    ecg_data = np.load(file_path)

# Convertir datos a un array de numpy
ecg_data = np.array(ecg_data)
time_axis = np.arange(len(ecg_data)) / sampling_rate

# ---- Análisis de la señal cruda ----
print(f"\nCaracterísticas de la señal cruda:")
print(f"Frecuencia de muestreo: {sampling_rate} Hz")
print(f"Número de muestras: {len(ecg_data)}")
print(f"Tiempo total de la señal: {len(ecg_data) / sampling_rate:.2f} s")
print(f"Niveles de cuantificación: {np.unique(ecg_data).size}")

# ---- Filtro de Promedio ----
def moving_average(data, window_size):
    """Aplica un filtro de promedio (media móvil) a la señal de ECG."""
    return np.convolve(data, np.ones(window_size) / window_size, mode='same')

# Aplicar el filtro de promedio
window_size = 10  # Tamaño de la ventana para el promedio
filtered_data = moving_average(ecg_data, window_size)

# Mostrar información del filtro
print("\nFiltro de Promedio:")
print(f"Tamaño de ventana: {window_size}")
print("Justificación: El filtro de promedio es útil para suavizar la señal y reducir el ruido, "
      "aunque puede disminuir la amplitud de las señales rápidas.")

# ---- Identificación de picos R ----
peaks, _ = find_peaks(filtered_data, distance=sampling_rate*0.6)
RR_intervals = np.diff(peaks) / sampling_rate

# Estadísticos de HRV
mean_RR = np.mean(RR_intervals)
std_RR = np.std(RR_intervals)

# Mostrar estadísticos de HRV
print("\nAnálisis estadístico de HRV:")
print(f"Media de intervalos R-R (mean_RR): {mean_RR:.3f} s")
print(f"Desviación estándar de intervalos R-R (std_RR): {std_RR:.3f} s")
print("Interpretación: Una media R-R elevada puede indicar una frecuencia cardíaca baja. "
      "Una desviación alta sugiere alta variabilidad cardíaca, asociada a un mejor tono vagal.")

# ---- Transformada Wavelet Continua ----
wavelet = 'morl'  # Wavelet Morlet
scales = np.arange(1, 512)  # Ajuste de escalas para incluir frecuencias más bajas
coefficients, frequencies = pywt.cwt(RR_intervals, scales, wavelet, sampling_period=1/sampling_rate)

# ---- Análisis de HRV en bandas de frecuencia ----
low_frequency_band = (0.04, 0.15)
high_frequency_band = (0.15, 0.4)
lf_indices = np.where((frequencies >= low_frequency_band[0]) & (frequencies <= low_frequency_band[1]))[0]
hf_indices = np.where((frequencies >= high_frequency_band[0]) & (frequencies <= high_frequency_band[1]))[0]
lf_power = np.sum(np.abs(coefficients[lf_indices, :])**2)
hf_power = np.sum(np.abs(coefficients[hf_indices, :])**2)

# Mostrar análisis de frecuencia
print("\nEspectrograma de HRV usando la Wavelet Morlet:")
print("La wavelet Morlet es adecuada para el análisis de HRV porque permite una buena resolución en frecuencia, "
      "capturando variaciones dinámicas en las bandas de LF y HF.")
print(f"Potencia en banda de baja frecuencia (LF): {lf_power:.2f}")
print(f"Potencia en banda de alta frecuencia (HF): {hf_power:.2f}")
print("Análisis de frecuencias: La banda LF (0.04-0.15 Hz) refleja el tono simpático y parasimpático, mientras que "
      "la banda HF (0.15-0.4 Hz) está asociada principalmente con la actividad parasimpática.")
print("La variación de la potencia espectral puede indicar la respuesta del sistema nervioso autónomo ante diferentes condiciones.")

# ---- Visualización de cada gráfico en una imagen individual ----
# Gráfica de la señal ECG cruda
plt.figure(figsize=(10, 4))
plt.plot(time_axis, ecg_data)
plt.title("Señal ECG Cruda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# Gráfica de la señal ECG filtrada y picos R
plt.figure(figsize=(10, 4))
plt.plot(time_axis, filtered_data, label="Señal ECG Filtrada")
plt.plot(peaks / sampling_rate, filtered_data[peaks], "rx", label="Picos R")
plt.title("Detección de Picos R en la Señal ECG Filtrada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()

# Comparación de la señal filtrada con los coeficientes de wavelet en una gráfica
plt.figure(figsize=(10, 4))
plt.plot(time_axis, filtered_data, label="Señal ECG Filtrada")
plt.plot(time_axis[:len(coefficients[0])], np.abs(coefficients[0]), label="Coeficientes de Wavelet (escala 1)", alpha=0.6)
plt.title("Comparación de Señal ECG Filtrada y Coeficientes de Wavelet")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud / Coeficientes")
plt.legend()
plt.grid()
plt.show()

# Espectrograma de HRV usando CWT
plt.figure(figsize=(10, 6))
plt.imshow(np.abs(coefficients), extent=[0, len(filtered_data), frequencies[-1], frequencies[0]], 
           aspect='auto', cmap='viridis')
plt.colorbar(label='Magnitud')
plt.xlabel('Tiempo')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma de HRV usando CWT')
plt.show()

# Distribución de potencia espectral en bandas LF y HF
plt.figure(figsize=(10, 4))
plt.plot(frequencies, np.sum(np.abs(coefficients)**2, axis=1))
plt.axvline(x=low_frequency_band[0], color='blue', linestyle='--', label='LF Start')
plt.axvline(x=low_frequency_band[1], color='blue', linestyle='--', label='LF End')
plt.axvline(x=high_frequency_band[0], color='green', linestyle='--', label='HF Start')
plt.axvline(x=high_frequency_band[1], color='green', linestyle='--', label='HF End')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Potencia espectral')
plt.title('Distribución de la Potencia Espectral en Bandas LF y HF')
plt.legend()
plt.grid()
plt.show()
