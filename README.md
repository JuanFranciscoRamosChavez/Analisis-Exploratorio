# Análisis del Bienestar Estudiantil

Este proyecto realiza un análisis exploratorio de datos (EDA) a partir de dos encuestas distintas aplicadas a estudiantes, con el objetivo de obtener una visión integral de su bienestar. Los scripts automatizan la limpieza de datos, el cálculo de KPIs y la generación de visualizaciones profesionales para entender las conexiones entre la situación económica y el estilo de vida 

---

## Características

* **Análisis Modular**: El proyecto está dividido en scripts que analizan cada encuesta de forma independiente.
* **Análisis Combinado**: Un script dedicado fusiona los datos de las tres fuentes para descubrir insights más profundos y KPIs de diagnóstico.
* **Organización Automática**: Las visualizaciones generadas se guardan automáticamente en carpetas separadas para mantener el orden y la claridad.
* **Ejecución Simplificada**: Un único script maestro (`remoto.py`) orquesta la ejecución de todos los análisis en el orden correcto.

---

## Estructura del Proyecto

El flujo de trabajo está organizado de la siguiente manera:

1.  **`economia.py`**:
    * **Entrada**: `Situación económica y bienestar estudiantil.csv`
    * **Proceso**: Limpia y analiza los datos relacionados con la situación financiera de los estudiantes.
    * **Salida**: Genera gráficos y los guarda en la carpeta `./resultados_economia/`.

2.  **`estres.py`**:
    * **Entrada**: `Preguntas equipo 3 (respuestas).csv`
    * **Proceso**: Limpia y analiza datos sobre hábitos, estrés y estilo de vida.
    * **Salida**: Genera gráficos y los guarda en la carpeta `./resultados_estilo_vida/`.

3.  **`combinacion.py`**:
    * **Entrada**: Utiliza los datos de las tres encuestas (económica, hábitos y salud mental).
    * **Proceso**: Realiza un análisis cruzado para calcular KPIs de diagnóstico complejos.
    * **Salida**: Genera visualizaciones avanzadas y las guarda en la carpeta `./resultados_combinados/`.

4.  **`remoto.py`**:
    * **Función**: Es el script principal que se debe ejecutar. Llama a `economia.py`, `estres.py`, y `combinacion.py` en secuencia para realizar el análisis completo con una sola instrucción.

---

## Requisitos Previos

Para ejecutar este proyecto, se recomienda configurar un entorno virtual con **Python 3.11**.

1.  **Crear el entorno virtual**:
    Navega a la carpeta raíz de tu proyecto en la terminal y ejecuta:
    ```bash
    python3.11 -m venv venv
    ```

2.  **Activar el entorno virtual**:
    * En **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    * En **macOS / Linux**:
        ```bash
        source venv/bin/activate
        ```

3.  **Instalar las dependencias**:
    Una vez que el entorno esté activado, instala las bibliotecas necesarias con el siguiente comando:
    ```bash
    pip install requirements.txt
    ```
    Si no reconoce el comando anterior comando usa el siguiente:
        ```bash
    python -m pip install -r requirements.txt
    ```

### Archivos de Datos Necesarios

Para que los scripts funcionen, debes colocar los siguientes archivos CSV en la misma carpeta que los archivos `.py`:

1.  `Situación económica y bienestar estudiantil.csv`
2.  `Preguntas equipo 3 (respuestas).csv`

---

## Cómo Ejecutar el Análisis

1.  **Clona el repositorio** y navega a la carpeta del proyecto.
2.  **Configura el entorno virtual** y activa las dependencias como se describe en la sección de Requisitos.
3.  **Asegura los datos**: Verifica que los tres archivos CSV requeridos estén en la carpeta principal.
4.  **Ejecuta el script maestro**: Con el entorno virtual activado, ejecuta el siguiente comando en tu terminal:
    ```bash
    python remoto.py
    ```

---

##  Resultados

Después de ejecutar el script, se crearán tres nuevas carpetas en tu directorio:

* `resultados_economia/`
* `resultados_estilo_vida/`
* `resultados_combinados/`

Dentro de cada una, encontrarás las imágenes (`.png`) de los gráficos generados por el análisis correspondiente.#
