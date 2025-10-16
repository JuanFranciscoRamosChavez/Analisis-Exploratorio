import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

print("\nIniciando el script de Análisis de Estilo de Vida...")

# --- CREACIÓN DE CARPETA DE RESULTADOS ---
output_dir = 'resultados_estilo_vida'
os.makedirs(output_dir, exist_ok=True)
print(f"Las imágenes se guardarán en la carpeta: '{output_dir}/'")

# --- PARTE 1: LIMPIEZA Y PREPARACIÓN DE DATOS ---

file_path = 'Preguntas equipo 3 (respuestas).csv'
try:
    # Usamos 'utf-8-sig' para leer correctamente acentos y caracteres especiales
    df_raw = pd.read_csv(file_path, encoding='utf-8-sig')
    print("Archivo CSV original cargado exitosamente.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{file_path}'. Asegúrate de que está en la misma carpeta.")
    exit()

# Renombramos las columnas para que sean más fáciles de manejar
df_raw.columns = [
    'Timestamp', 'Numero_Cuenta', 'Dias_Ejercicio', 'Actividad_Recreativa',
    'Comidas_Dia', 'Toma_Alcohol', 'Horas_Sueño', 'Area_Trabajo', 'Edad',
    'Sexo', 'Nivel_Ansiedad', 'Vivienda', 'Tiene_Beca', 'Horas_Pantalla',
    'Ingresos_Mensuales', 'Siente_Energia', 'Promedio_Escolar', 'Es_Regular',
    'Ayuda_Psicologica', 'Tiene_Pareja', 'Alguien_Depende_Economicamente'
]

# --- Funciones de Limpieza Específicas para la nueva encuesta ---

def limpiar_texto_general(texto):
    """Limpia texto quitando espacios y convirtiendo a minúsculas."""
    if isinstance(texto, str):
        return texto.strip().lower()
    return texto

def limpiar_ansiedad(texto):
    """Estandariza las respuestas sobre el nivel de ansiedad."""
    texto = limpiar_texto_general(texto)
    if not texto: return "No especificado"
    if 'ninguno' in texto: return 'Ninguno'
    if 'leve' in texto: return 'Leve'
    if 'moderada' in texto: return 'Moderada'
    if 'grave' in texto: return 'Grave'
    return 'No especificado'

def limpiar_sexo(texto):
    """Estandariza las respuestas de sexo."""
    texto = limpiar_texto_general(texto)
    if not texto: return "No especificado"
    if texto.startswith('f'): return 'Femenino'
    if texto.startswith('m') or texto.startswith('h'): return 'Masculino'
    return 'No especificado'

def limpiar_si_no(texto):
    """Estandariza respuestas de Sí/No."""
    texto = limpiar_texto_general(texto)
    if not texto: return "No especificado"
    # Incluye "nop" y variaciones
    if texto.startswith('n'): return 'No'
    if texto.startswith('s'): return 'Sí'
    return 'No especificado'

# --- Creación del DataFrame Limpio ---
# Se aplica cada función de limpieza a su columna correspondiente
datos_limpios = {
    'Sexo': df_raw['Sexo'].apply(limpiar_sexo),
    'Nivel_Ansiedad': df_raw['Nivel_Ansiedad'].apply(limpiar_ansiedad),
    'Tiene_Beca': df_raw['Tiene_Beca'].apply(limpiar_si_no),
    # pd.to_numeric maneja la conversión a número, 'coerce' convierte errores en Nulo (NaN)
    'Horas_Sueño': pd.to_numeric(df_raw['Horas_Sueño'], errors='coerce'),
    'Promedio_Escolar': pd.to_numeric(df_raw['Promedio_Escolar'], errors='coerce')
}
df = pd.DataFrame(datos_limpios)

# Eliminamos filas donde datos clave (como el promedio) son nulos para mejorar los gráficos
df.dropna(subset=['Promedio_Escolar', 'Horas_Sueño'], inplace=True)

print("Datos limpiados y estandarizados.")

# --- PARTE 2: VISUALIZACIÓN DE DATOS ---

# Configuramos un estilo visual agradable para todos los gráficos
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'

# --- Gráfico 1: Nivel de Ansiedad ---
plt.figure(figsize=(10, 7))
ansiedad_orden = ['Ninguno', 'Leve', 'Moderada', 'Grave']
ax1 = sns.countplot(y=df['Nivel_Ansiedad'], order=ansiedad_orden, palette='viridis')
plt.title('Distribución del Nivel de Ansiedad en Estudiantes', fontsize=16, fontweight='bold')
plt.xlabel('Cantidad de Estudiantes', fontsize=12)
plt.ylabel('Nivel de Ansiedad Reportado', fontsize=12)
# Añadimos etiquetas a las barras
for p in ax1.patches:
    if p.get_width() > 0:
        ax1.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(5, 0), textcoords='offset points')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico_nivel_ansiedad.png'))
plt.close()

# --- Gráfico 2: Distribución por Sexo ---
plt.figure(figsize=(8, 8))
sexo_counts = df['Sexo'].value_counts()
plt.pie(sexo_counts, labels=sexo_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff9999'])
plt.title('Distribución de Estudiantes por Sexo', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'grafico_distribucion_sexo.png'))
plt.close()

# --- Gráfico 3: Horas de Sueño ---
plt.figure(figsize=(10, 7))
ax3 = sns.countplot(x=df['Horas_Sueño'].round(), palette='plasma')
plt.title('Horas de Sueño Promedio por Noche', fontsize=16, fontweight='bold')
plt.xlabel('Horas de Sueño', fontsize=12)
plt.ylabel('Cantidad de Estudiantes', fontsize=12)
# Añadimos etiquetas a las barras
for p in ax3.patches:
    if p.get_height() > 0:
        ax3.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico_horas_sueño.png'))
plt.close()

# --- Gráfico 4: Estudiantes con Beca ---
plt.figure(figsize=(8, 8))
beca_counts = df['Tiene_Beca'].value_counts()
plt.pie(beca_counts, labels=beca_counts.index, autopct='%1.1f%%', startangle=90, colors=['#c2c2f0','#ffb3e6'])
plt.title('Proporción de Estudiantes con Beca', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'grafico_becas.png'))
plt.close()

# --- Gráfico 5: Relación entre Ansiedad y Promedio Escolar ---
plt.figure(figsize=(12, 8))
# Usamos un Boxplot para comparar distribuciones
sns.boxplot(x='Nivel_Ansiedad', y='Promedio_Escolar', data=df, order=ansiedad_orden, palette='coolwarm')
plt.title('Promedio Escolar vs. Nivel de Ansiedad', fontsize=16, fontweight='bold')
plt.xlabel('Nivel de Ansiedad Reportado', fontsize=12)
plt.ylabel('Promedio Escolar', fontsize=12)
plt.ylim(5, 10) # Ajustamos el eje Y para enfocarnos en el rango de calificaciones
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico_ansiedad_vs_promedio.png'))
plt.close()

print("\nAnálisis finalizado con éxito. ")