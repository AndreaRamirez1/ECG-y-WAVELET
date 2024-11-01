# Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet
> Realizado por: Andrea Ramírez y Karol Díaz

Para capturar la señal cardíaca de manera efectiva, se utilizan electrodos adhesivos conectados a un sistema de adquisición de datos basado en Arduino, el cual es programado en Python para realizar tanto la adquisición como el procesamiento de las señales. La implementación de este sistema requiere la verificación cuidadosa de los voltajes y corrientes de trabajo para garantizar la compatibilidad con el sistema operativo y evitar daños en los componentes electrónicos o en el usuario. Este laboratorio, por tanto, se centra en desarrollar un sistema de adquisición y análisis de HRV empleando técnicas avanzadas como la Transformada Wavelet y evaluando la dinámica del ritmo cardíaco a través de un entorno de programación accesible y compatible para investigaciones futuras en el área biomédica.

Sin embargo, para dicha adquisisción de las señales en distintos sujetos de prueba se efectuo un consentimiento informado que se encuentra agregado en la presente plataforma. Esto para poder hacer uso de los datos recolectados y realizar su respectivo analisis. Así mismo, hay ciertos conceptos teoricos que es de suma importancia comprender antes de empezar con la obtención de las señales.

## ** Actividad simpática y parasimpática del sistema nervioso autónomo**

El sistema nervioso autónomo (SNA) es responsable de regular muchas funciones involuntarias del organismo, como la frecuencia cardíaca, la respiración y la digestión. Se divide en dos ramas principales: el sistema nervioso simpático y el sistema nervioso parasimpático, las cuales operan de manera complementaria para mantener la homeostasis corporal. 

El sistema **simpático**, conocido también como el sistema de “lucha o huida”, se activa en situaciones de estrés o emergencia, aumentando la frecuencia cardíaca, la presión arterial y promoviendo la liberación de energía en los tejidos. Por otro lado, el sistema **parasimpático**, llamado el sistema de “descanso y digestión”, favorece la relajación y disminución de la actividad fisiológica, reduciendo la frecuencia cardíaca y promoviendo la recuperación del organismo. La regulación y balance de ambos sistemas sobre el corazón es esencial para una respuesta fisiológica adecuada a estímulos externos y para el mantenimiento de la salud cardiovascular.

## ** Efecto de la actividad simpática y parasimpática en la frecuencia cardíaca**

La frecuencia cardíaca es modulada por la actividad del sistema nervioso autónomo, donde los estímulos simpáticos incrementan la velocidad de los latidos, mientras que los estímulos parasimpáticos tienen un efecto de desaceleración. Cuando se activan los receptores simpáticos en el corazón, se incrementa la liberación de noradrenalina, lo cual resulta en un aumento en la frecuencia y fuerza de contracción cardíaca. En cambio, cuando el sistema parasimpático predomina, la acetilcolina liberada actúa sobre el nervio vago para disminuir la frecuencia cardíaca.

El equilibrio entre ambas ramas del SNA permite respuestas adaptativas a condiciones variables, como el ejercicio físico, el estrés o el descanso. Los cambios en la frecuencia cardíaca son, por tanto, una ventana a la actividad subyacente del sistema nervioso autónomo y se pueden medir para obtener información sobre la salud cardiovascular y la capacidad del organismo para responder a distintos estímulos.

## ** Variabilidad de la Frecuencia Cardíaca (HRV)**

La Variabilidad de la Frecuencia Cardíaca (HRV) se define como la variación en el tiempo entre latidos cardíacos sucesivos, comúnmente expresada como fluctuaciones en el intervalo R-R de un electrocardiograma (ECG). Este parámetro es una medida no invasiva de la actividad del SNA y de la regulación autonómica sobre el corazón. 

![image](https://github.com/user-attachments/assets/5f6a7c36-4eb0-4d22-a6eb-aacebb9c0748)

<em><strong>Figura 1.</strong> Visualización de señales ECG.</em>

El análisis de HRV se enfoca en frecuencias de interés que reflejan diferentes aspectos de la actividad simpática y parasimpática. Las principales bandas de frecuencia en el análisis de HRV son:
- **Frecuencia ultra baja (ULF, <0.003 Hz):** Asociada con ritmos circadianos y cambios hormonales.
- **Frecuencia muy baja (VLF, 0.003–0.04 Hz):** Relacionada con mecanismos térmicos, metabólicos y de regulación hormonal.
- **Frecuencia baja (LF, 0.04–0.15 Hz):** Indicativa de la actividad simpática y parasimpática combinada, aunque con mayor peso en la regulación simpática.
- **Frecuencia alta (HF, 0.15–0.4 Hz):** Relacionada principalmente con la actividad parasimpática y la respiración.

Un análisis detallado de estas frecuencias proporciona información sobre el balance simpático-parasimpático y la capacidad de adaptación del organismo, y ha sido útil en estudios de estrés, fatiga y rendimiento deportivo.

## ** Transformada Wavelet**

La Transformada Wavelet es una herramienta matemática que permite analizar señales no estacionarias en el dominio tiempo-frecuencia, proporcionando una visión detallada de cómo cambian las características de la señal a través del tiempo. A diferencia de la Transformada de Fourier, que se limita a representar la señal en términos de sus frecuencias globales, la Transformada Wavelet permite estudiar variaciones instantáneas y transitorias, siendo especialmente útil en el análisis de señales biológicas complejas como el ECG.

En el contexto del análisis de HRV, la Transformada Wavelet permite identificar y segmentar los cambios en las bandas de frecuencia de interés a lo largo del tiempo, proporcionando una representación precisa de la variabilidad en función de las distintas influencias del sistema nervioso autónomo.

**Tipos de wavelets comunes en señales biológicas**  
Existen varios tipos de wavelets que son populares para el análisis de señales biológicas, tales como:
- **Wavelet de Daubechies:** De uso frecuente en señales de ECG debido a su similitud con el pulso cardíaco.
- **Wavelet de Morlet:** Ideal para el análisis en tiempo-frecuencia, y ampliamente usada en señales cerebrales y cardíacas.
- **Wavelet de Haar:** Su simplicidad la hace útil en análisis rápidos, aunque es menos precisa para detalles finos.

La elección de la wavelet depende de la naturaleza de la señal y los objetivos del análisis, permitiendo la personalización de los estudios para extraer información significativa de los datos fisiológicos. En resumen, la Transformada Wavelet es un método robusto y flexible que, en combinación con herramientas de programación como Python y plataformas de adquisición como Arduino, ofrece un abordaje completo para el análisis de HRV en estudios biomédicos.

# Desarrollo de la Práctica

En el desarrollo se considero un orden de ejecución para la adquisisción de señales adecuadas. Dicho orden consiste en un diagrama de flujo que nos permitira llevar el paso a paso de cada procedimiento a ejecutar para las señales.


# Resultados

# Conclusiones
Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet 
