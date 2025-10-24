# Análisis del Bienestar Estudiantil

Este proyecto realiza un análisis exploratorio de datos (EDA) a partir de dos encuestas distintas aplicadas a estudiantes, con el objetivo de obtener una visión integral de su bienestar. Los scripts automatizan la limpieza de datos, el cálculo de KPIs y la generación de visualizaciones profesionales para entender las conexiones entre la situación económica y el estilo de vida 

---

## Características

* **Análisis Modular**: El proyecto está dividido en scripts que analizan cada encuesta de forma independiente.
* **Análisis Combinado**: Un script dedicado fusiona los datos de las dos fuentes para descubrir insights más profundos y KPIs de diagnóstico.
* **Organización Automática**: Las visualizaciones generadas se guardan automáticamente.
* **Ejecución Simplificada**: Un único script maestro (`remoto.py`) orquesta la ejecución de todos los análisis en el orden correcto.

---

## Estructura del Proyecto

El flujo de trabajo está organizado de la siguiente manera:

* **/analisis/**: Contiene todos los scripts de Python (`.py`) para la limpieza y generación de gráficos.
    * `analizar_economia.py`: Script para la encuesta económica.
    * `analizar_estilo_vida.py`: Script para la encuesta de estilo de vida.
    * `analizar_combinado.py`: Script que une los datos limpios y genera gráficos de correlación.
    * `remoto.py`: Orquestador que ejecuta todos los scripts anteriores.
* **/data/01_crudos/**: Contiene los archivos CSV originales de las encuestas.
* **/data/02_limpios/**: Contiene los archivos CSV limpios generados por los scripts de análisis.
* **/resultados/**: Contiene todos los gráficos (`.png`) generados.
* `requirements.txt`: Lista de todas las dependencias de Python necesarias.

---

## Requisitos Previos

Compartimos el link de la versión de Python para la ejecución del código, para no llegar a tener incompatibilidades con el entorno virtual https://www.python.org/downloads/release/python-3119/ 

Para ejecutar este proyecto, se recomienda configurar un entorno virtual con **Python 3.11**.

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/JuanFranciscoRamosChavez/Analisis-Exploratorio.git
    cd Analisis-Exploratorio
    ```
2.  **Crear el entorno virtual**:
    Navega a la carpeta raíz de tu proyecto en la terminal y ejecuta:
    ```bash
    py -3.11 -m venv venv
    ```

3.  **Activar el entorno virtual**:
    * En **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    * En **macOS / Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Instalar las dependencias**:
    Una vez que el entorno esté activado, instala las bibliotecas necesarias con el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```
    Si no reconoce el comando anterior comando usa el siguiente:
    ```bash
    python -m pip install -r requirements.txt
    ```
5. **Navega a la carpeta de análisis y ejecuta el script principal:**
    ```sh
    cd analisis
    py remoto.py
    ```
6. **Revisa los archivos `.csv` en `/data/02_limpios/` y los gráficos `.png` en `/resultados/`.**

---

## Tecnologías Utilizadas

* **Python**
* **Pandas:** Para la carga, limpieza y manipulación de datos.
* **Matplotlib y Seaborn:** Para la visualización de datos.

#
