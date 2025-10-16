import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

print("\nIniciando el script de Situación Económica y Bienestar Estudiantil...")

# --- CREACIÓN DE CARPETA DE RESULTADOS ---
output_dir = 'resultados_economia'
os.makedirs(output_dir, exist_ok=True)
print(f"Las imágenes se guardarán en la carpeta: '{output_dir}/'")

# --- PARTE 1: LIMPIEZA DE DATOS ---

file_path = 'Situación económica y bienestar estudiantil.csv'
try:
    df_raw = pd.read_csv(file_path)
    print("Archivo CSV original cargado exitosamente.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{file_path}'. Asegúrate de que está en la misma carpeta.")
    exit()

column_names = [
    'Timestamp', 'Numero_Cuenta', 'Semestre', 'Carrera',
    'Situacion_Economica', 'Fuente_Ingresos', 'Gasto_Dificil',
    'Impacto_Economico', 'Equilibrio_Trabajo_Estudio', 'Renuncia_Oportunidad',
    'Sentimiento_Finanzas', 'Estrategias_Dinero', 'Apoyo_Economico_Deseado',
    'Otro_Tipo_Ayuda', 'Utilidad_Educacion_Financiera',
    'Situacion_Economica_Ideal_5_Anios', 'Momento_Mayor_Presion',
    'Accion_Gasto_Inesperado', 'Recibio_Orientacion_Financiera', 'Consejo_Estudiantes'
]
df_raw.columns = column_names

# --- Funciones de Limpieza ---
def limpiar_situacion_economica(texto):
    if not isinstance(texto, str): return "No especificado"
    texto = texto.lower()
    if 'buena' in texto: return 'Buena'
    if 'estable' in texto: return 'Estable'
    if 'regular' in texto: return 'Regular'
    if 'complicada' in texto: return 'Complicada'
    if 'mala' in texto: return 'Mala'
    return 'Otra'

def limpiar_sentimientos(texto):
    if not isinstance(texto, str): return "No especificado"
    texto = texto.lower()
    if any(palabra in texto for palabra in ['ansiedad', 'preocupación', 'preocupacion']):
        return 'Ansiedad/Preocupación'
    if 'tranquilidad' in texto: return 'Tranquilidad'
    if 'indiferencia' in texto: return 'Indiferencia'
    return 'Otro'

def limpiar_gasto_dificil(texto):
    if not isinstance(texto, str): return "No especificado"
    texto = texto.lower()
    if 'transporte' in texto or 'pasajes' in texto: return 'Transporte'
    if 'comida' in texto or 'lunch' in texto or 'despensa' in texto: return 'Comida/Alimentos'
    if 'renta' in texto: return 'Renta'
    if 'ninguno' in texto: return 'Ninguno'
    return 'Otros'

def limpiar_renuncia_oportunidad(texto):
    if not isinstance(texto, str): return "No especificado"
    texto = texto.lower().strip()
    if texto.startswith('si') or texto.startswith('sí'): return 'Sí'
    if texto.startswith('no') or texto.startswith('ninguna'): return 'No'
    return 'No especificado'

def limpiar_impacto_academico(texto):
    if not isinstance(texto, str): return "No especificado"
    texto = texto.lower()
    if any(palabra in texto for palabra in ['alto', 'mucho', 'bastante']): return 'Alto'
    if 'medio' in texto: return 'Medio'
    if 'ninguno' in texto or 'no tiene' in texto: return 'Ninguno'
    return 'No especificado'

# --- Creación del DataFrame Limpio ---
datos_limpios = {
    'Situacion_Economica': df_raw['Situacion_Economica'].apply(limpiar_situacion_economica),
    'Sentimiento_Financiero': df_raw['Sentimiento_Finanzas'].apply(limpiar_sentimientos),
    'Gasto_Principal': df_raw['Gasto_Dificil'].apply(limpiar_gasto_dificil),
    'Renuncia_Oportunidad': df_raw['Renuncia_Oportunidad'].apply(limpiar_renuncia_oportunidad),
    'Impacto_Academico': df_raw['Impacto_Economico'].apply(limpiar_impacto_academico)
}
df = pd.DataFrame(datos_limpios)
print("Datos limpiados y estandarizados.")

# --- PARTE 2: VISUALIZACIÓN DE DATOS (CORREGIDA) ---

sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'

# --- Gráfico 1: Situación Económica ---
plt.figure(figsize=(10, 7))
ax1 = sns.countplot(y=df['Situacion_Economica'], order=df['Situacion_Economica'].value_counts().index, palette='summer')
plt.title('Distribución de la Situación Económica', fontsize=16, fontweight='bold')
plt.xlabel('Cantidad de Estudiantes', fontsize=12)
plt.ylabel('Situación Percibida', fontsize=12)
for p in ax1.patches:
    if p.get_width() > 0:
        ax1.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico_situacion_economica.png'))
plt.close()

# --- Gráfico 2: Sentimiento Financiero (sin cambios) ---
plt.figure(figsize=(8, 8))
sentimiento_counts = df['Sentimiento_Financiero'].value_counts()
plt.pie(sentimiento_counts, labels=sentimiento_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('coolwarm'))
plt.title('Sentimientos Generados por las Finanzas', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'grafico_sentimiento_financiero.png'))
plt.close()

# --- Gráfico 3: Gasto Principal ---
plt.figure(figsize=(10, 7))
ax3 = sns.countplot(x=df['Gasto_Principal'], order=df['Gasto_Principal'].value_counts().index, palette='magma')
plt.title('Gastos Mensuales Más Difíciles de Cubrir', fontsize=16, fontweight='bold')
plt.xlabel('Tipo de Gasto', fontsize=12)
plt.ylabel('Cantidad de Estudiantes', fontsize=12)
for p in ax3.patches:
    if p.get_height() > 0:
        ax3.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico_gasto_principal.png'))
plt.close()

# --- Gráfico 4: Renuncia a Oportunidades (sin cambios) ---
plt.figure(figsize=(8, 8))
renuncia_counts = df['Renuncia_Oportunidad'].value_counts()
plt.pie(renuncia_counts, labels=renuncia_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Renuncia a Oportunidades por Motivos Económicos', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'grafico_renuncia_oportunidades.png'))
plt.close()

# --- Gráfico 5: Impacto Académico ---
plt.figure(figsize=(10, 7))
ax5 = sns.countplot(x=df['Impacto_Academico'], order=df['Impacto_Academico'].value_counts().index, palette='cividis')
plt.title('Impacto Económico en el Desempeño Académico', fontsize=16, fontweight='bold')
plt.xlabel('Nivel de Impacto Percibido', fontsize=12)
plt.ylabel('Cantidad de Estudiantes', fontsize=12)
for p in ax5.patches:
    if p.get_height() > 0:
        ax5.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico_impacto_academico.png'))
plt.close()

print("\nAnálisis finalizado con éxito.")
