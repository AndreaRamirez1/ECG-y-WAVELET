# Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet
> Realizado por: Andrea Ramírez y Karol Díaz

Para capturar la señal cardíaca de manera efectiva, se utilizan electrodos adhesivos conectados a un sistema de adquisición de datos basado en Arduino, el cual es programado en Python para realizar tanto la adquisición como el procesamiento de las señales. La implementación de este sistema requiere la verificación cuidadosa de los voltajes y corrientes de trabajo para garantizar la compatibilidad con el sistema operativo y evitar daños en los componentes electrónicos o en el usuario. Este laboratorio, por tanto, se centra en desarrollar un sistema de adquisición y análisis de HRV empleando técnicas avanzadas como la Transformada Wavelet y evaluando la dinámica del ritmo cardíaco a través de un entorno de programación accesible y compatible para investigaciones futuras en el área biomédica.

![image](https://github.com/user-attachments/assets/1c86eabc-bfac-4a6c-ae45-cf6b3db64fa1)

<em><strong>Figura 1.</strong> Posicionamiento de electrodos para ECG.</em>

Sin embargo, para dicha adquisisción de las señales en distintos sujetos de prueba se efectuo un consentimiento informado que se encuentra agregado en la presente plataforma. Esto para poder hacer uso de los datos recolectados y realizar su respectivo analisis. Así mismo, hay ciertos conceptos teoricos que es de suma importancia comprender antes de empezar con la obtención de las señales.

### Actividad simpática y parasimpática del sistema nervioso autónomo

El sistema nervioso autónomo (SNA) es responsable de regular muchas funciones involuntarias del organismo, como la frecuencia cardíaca, la respiración y la digestión. Se divide en dos ramas principales: el sistema nervioso simpático y el sistema nervioso parasimpático, las cuales operan de manera complementaria para mantener la homeostasis corporal. 

El sistema **simpático**, conocido también como el sistema de “lucha o huida”, se activa en situaciones de estrés o emergencia, aumentando la frecuencia cardíaca, la presión arterial y promoviendo la liberación de energía en los tejidos. Por otro lado, el sistema **parasimpático**, llamado el sistema de “descanso y digestión”, favorece la relajación y disminución de la actividad fisiológica, reduciendo la frecuencia cardíaca y promoviendo la recuperación del organismo. La regulación y balance de ambos sistemas sobre el corazón es esencial para una respuesta fisiológica adecuada a estímulos externos y para el mantenimiento de la salud cardiovascular.

###  Efecto de la actividad simpática y parasimpática en la frecuencia cardíaca

La frecuencia cardíaca es modulada por la actividad del sistema nervioso autónomo, donde los estímulos simpáticos incrementan la velocidad de los latidos, mientras que los estímulos parasimpáticos tienen un efecto de desaceleración. Cuando se activan los receptores simpáticos en el corazón, se incrementa la liberación de noradrenalina, lo cual resulta en un aumento en la frecuencia y fuerza de contracción cardíaca. En cambio, cuando el sistema parasimpático predomina, la acetilcolina liberada actúa sobre el nervio vago para disminuir la frecuencia cardíaca.

El equilibrio entre ambas ramas del SNA permite respuestas adaptativas a condiciones variables, como el ejercicio físico, el estrés o el descanso. Los cambios en la frecuencia cardíaca son, por tanto, una ventana a la actividad subyacente del sistema nervioso autónomo y se pueden medir para obtener información sobre la salud cardiovascular y la capacidad del organismo para responder a distintos estímulos.

###  Variabilidad de la Frecuencia Cardíaca (HRV)

La Variabilidad de la Frecuencia Cardíaca (HRV) se define como la variación en el tiempo entre latidos cardíacos sucesivos, comúnmente expresada como fluctuaciones en el intervalo R-R de un electrocardiograma (ECG). Este parámetro es una medida no invasiva de la actividad del SNA y de la regulación autonómica sobre el corazón. 

![image](https://github.com/user-attachments/assets/5f6a7c36-4eb0-4d22-a6eb-aacebb9c0748)

<em><strong>Figura 2.</strong> Visualización de señales ECG.</em>

El análisis de HRV se enfoca en frecuencias de interés que reflejan diferentes aspectos de la actividad simpática y parasimpática. Las principales bandas de frecuencia en el análisis de HRV son:
- **Frecuencia ultra baja (ULF, <0.003 Hz):** Asociada con ritmos circadianos y cambios hormonales.
- **Frecuencia muy baja (VLF, 0.003–0.04 Hz):** Relacionada con mecanismos térmicos, metabólicos y de regulación hormonal.
- **Frecuencia baja (LF, 0.04–0.15 Hz):** Indicativa de la actividad simpática y parasimpática combinada, aunque con mayor peso en la regulación simpática.
- **Frecuencia alta (HF, 0.15–0.4 Hz):** Relacionada principalmente con la actividad parasimpática y la respiración.

Un análisis detallado de estas frecuencias proporciona información sobre el balance simpático-parasimpático y la capacidad de adaptación del organismo, y ha sido útil en estudios de estrés, fatiga y rendimiento deportivo.

###  Transformada Wavelet

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

![image](https://github.com/user-attachments/assets/cbc4f337-2dae-4a70-945a-e2ced5c0c459)

<em><strong>Figura 3.</strong> Diagrama de flujpo para procesamiento de señales ECG.</em>

# Resultados

De manera análoga se hizo un circuito donde se usaron filtros análogos y se uso un optoacoplador para aislar al paciente de las posibles descargas que se podían generar en el momento de la obtención de la señal, para la parte analógica usamos los siguientes materiales y recursos para obtener una buena señal y así pasarla a un filtrado digital

Materiales empelados
Arduino uno (que nos va a permitir realizar la conexión entre el AD8232 y Python) 
Modulo AD8232 (para la amplificación de la señal ECG)
Amplificador operacional TL074 (Tiene 4 amplificadores integrados) 
Optoacoplador 4N25 (Para el aislamiento del paciente) 
Resistencias y capacitores para los filtros 
Diodos de protección 
Fuente de alimentación asilada 

Para la parte análoga implementamos diferentes filtros para obtener una buena señal 
Filtro pasa alto: 
En el cual lo hicimos porque elimina el ruido a baja frecuencia y evita que la deriva DC en la señal, este lo conectamos a la salida del AD8232 con una de las entradas del amplificador 

Filtro Notch para 60 Hz 
Este lo usamos para suprimir la interferencia eléctrica que se pueda tener en el momento de la obtención de la señal 
Filtro pasa-Bajo ( Para eliminar el aliasing) 
Este lo hicimos ya que este filtro reduce los componentes de alta frecuencia en este caso seria el ruido muscular y previene el aliasing al digitalizar la señal 
Aislamiento del paciente 
Usamos el optoacoplador 4N25 con el fin de proteger al paciente de cualquier corriente peligrosa y esto se hace antes de pasar la señal al Arduino. 



![image](https://github.com/user-attachments/assets/ebc5ebb6-93c9-44ed-86eb-5744628c3627)

 
Montaje Análogo 

![image](https://github.com/user-attachments/assets/6bea91f5-5096-4733-865d-37b62af73658)

Montaje Análogo

Ya que cuando terminamos la parte análoga se hizo la parte digital que fue un código en Python y una parte en Arduino uno la cual nos permite hacer la conexión entre el circuito análogo, que se conecta al AD8232 posteriormente al Arduino y este pasa la señal a Python. 
Para esta parte en necesitamos un consentimiento informado para poder obtener la señal ECG del paciente, grabamos la señal por 5 min donde el sujeto debía estar en reposo y en algunos intervalos se le hablo para poder tomar las señales del sistema simpático y parasimpático, todo con el fin de reducir el ruido experimental, para así poder asegurar la frecuencia de muestreo y los niveles de cuantificación, aplicamos filtros digitales, en este caso aplicamos un filtro de promedio esto con el fin de eliminar el ruido que aparece en la señal, de igual forma se hizo el respectivo análisis de HRV en el dominio del tiempo, en este caso la media de los intervalos R-R y su desviación estándar, seguido a esto aplicamos una transformada Wavelet continua en este caso usamos la transformada morlet y comparamos la señal obtenida con la trasnformada de wavelet para ver su comportamiento. 

 ![image](https://github.com/user-attachments/assets/dea2d2b5-8278-4d34-a12c-fddfa67d8001)

Señal electrocardiograma

 ![image](https://github.com/user-attachments/assets/624e4d2b-8201-4fa9-9977-237d4ef3c640)

Detención de picos 

 ![image](https://github.com/user-attachments/assets/762ce5ca-d3df-4a73-8baf-b64515181684)

Comparación 

 ![image](https://github.com/user-attachments/assets/60062af6-52c8-44f6-b56a-d17d4c6a3f89)

Espectrograma wavelet 

 ![image](https://github.com/user-attachments/assets/6bc0a631-fc41-44f2-9105-c75b665ba661)

Distribución de la potencia

![image](https://github.com/user-attachments/assets/42b3139e-837f-4ef8-8ced-70d8096d2527)

Resultados 1 

![image](https://github.com/user-attachments/assets/2d561ffc-18ff-4a47-abe6-1ddf30d20066)
Resultados 2

# Conclusiones

La Variabilidad de la Frecuencia Cardíaca (HRV) es un indicador esencial del estado y la regulación del sistema nervioso autónomo, proporcionando una ventana directa a la interacción entre el sistema simpático y parasimpático sobre el corazón. La necesidad de analizar esta señal, que es dinámica y no estacionaria, hace que la Transformada Wavelet sea una herramienta valiosa, ya que permite descomponer la señal en sus componentes de frecuencia y temporalidad, ofreciendo una representación precisa de las fluctuaciones instantáneas en el ritmo cardíaco. Mediante el uso de electrodos adhesivos, un sistema de adquisición basado en Arduino y un entorno de programación en Python, es posible implementar una plataforma robusta para la captura y análisis de señales de HRV. La verificación de la compatibilidad de voltajes y corrientes asegura la funcionalidad y seguridad del sistema, haciendo que este enfoque sea no solo práctico, sino también seguro para estudios biomédicos. Este proyecto tiene el potencial de sentar una base sólida para investigaciones futuras, ofreciendo un sistema accesible y adaptable para el análisis avanzado de HRV en entornos de laboratorio o clínicos.
