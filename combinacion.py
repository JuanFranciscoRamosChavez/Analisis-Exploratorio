import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("\nIniciando el script de análisis unificado ...")

# --- CREACIÓN DE CARPETA DE RESULTADOS ---
output_dir = 'resultados_unificados'    
os.makedirs(output_dir, exist_ok=True)
print(f"Las imágenes se guardarán en la carpeta: '{output_dir}/'")

# --- PARTE 1: CARGA Y LIMPIEZA DE DATOS ---
def cargar_y_limpiar_bienestar(filepath):
    """Carga y limpia la encuesta."""
    try:
        df = pd.read_csv(filepath, encoding='utf-8-sig')
    except FileNotFoundError: return None
    df.columns = ['Timestamp', 'Numero_Cuenta', 'Dias_Ejercicio', 'Actividad_Recreativa', 'Comidas_Dia', 'Toma_Alcohol', 'Horas_Sueño', 'Area_Trabajo', 'Edad', 'Sexo', 'Nivel_Ansiedad', 'Vivienda', 'Tiene_Beca', 'Horas_Pantalla', 'Ingresos_Mensuales', 'Siente_Energia', 'Promedio_Escolar', 'Es_Regular', 'Ayuda_Psicologica', 'Tiene_Pareja', 'Alguien_Depende_Economicamente']
    def limpiar_texto(t): return t.strip().lower() if isinstance(t, str) else t
    def limpiar_si_no(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if t.startswith('s'): return 'Sí'
        if t.startswith('n'): return 'No'
        return 'No especificado'
    def limpiar_ansiedad(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if 'ninguno' in t: return 'Ninguno'
        if 'leve' in t: return 'Leve'
        if 'moderada' in t: return 'Moderada'
        if 'grave' in t: return 'Grave'
        return 'No especificado'
    df['Nivel_Ansiedad'] = df['Nivel_Ansiedad'].apply(limpiar_ansiedad)
    df['Tiene_Beca'] = df['Tiene_Beca'].apply(limpiar_si_no)
    df['Siente_Energia'] = df['Siente_Energia'].apply(limpiar_si_no)
    df['Horas_Sueño'] = pd.to_numeric(df['Horas_Sueño'], errors='coerce')
    df['Promedio_Escolar'] = pd.to_numeric(df['Promedio_Escolar'], errors='coerce')
    df['Numero_Cuenta'] = pd.to_numeric(df['Numero_Cuenta'], errors='coerce')
    cols_to_keep = ['Numero_Cuenta', 'Nivel_Ansiedad', 'Horas_Sueño', 'Promedio_Escolar', 'Tiene_Beca', 'Siente_Energia']
    return df[cols_to_keep].dropna(subset=['Numero_Cuenta'])

def cargar_y_limpiar_economia(filepath):
    """Carga y limpia la encuesta."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError: return None
    df.columns = ['Timestamp', 'Numero_Cuenta', 'Semestre', 'Carrera', 'Situacion_Economica', 'Fuente_Ingresos', 'Gasto_Dificil', 'Impacto_Economico', 'Equilibrio_Trabajo_Estudio', 'Renuncia_Oportunidad', 'Sentimiento_Finanzas', 'Estrategias_Dinero', 'Apoyo_Economico_Deseado', 'Otro_Tipo_Ayuda', 'Utilidad_Educacion_Financiera', 'Situacion_Economica_Ideal_5_Anios', 'Momento_Mayor_Presion', 'Accion_Gasto_Inesperado', 'Recibio_Orientacion_Financiera', 'Consejo_Estudiantes']
    def limpiar_texto(t): return t.strip().lower() if isinstance(t, str) else t
    def limpiar_si_no(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if t.startswith('s'): return 'Sí'
        if t.startswith('n'): return 'No'
        return 'No especificado'
    def limpiar_situacion(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if 'complicada' in t or 'mala' in t: return 'Complicada/Mala'
        if 'buena' in t: return 'Buena'
        if 'estable' in t: return 'Estable'
        if 'regular' in t: return 'Regular'
        return 'No especificado'
    def limpiar_impacto(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if any(palabra in t for palabra in ['alto', 'mucho', 'bastante']): return 'Alto'
        return 'Medio/Bajo'
    def limpiar_sentimientos(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if any(p in t for p in ['ansiedad', 'preocupación', 'estrés', 'preocupacion']): return 'Ansiedad/Preocupación'
        if 'tranquilidad' in t: return 'Tranquilidad'
        return 'Otro'
    def limpiar_gasto(t):
        t = limpiar_texto(t)
        if not t: return "No especificado"
        if 'transporte' in t: return 'Transporte'
        if 'comida' in t or 'alimento' in t: return 'Comida'
        if 'renta' in t or 'vivienda' in t: return 'Renta/Vivienda'
        return 'Otros'
    df['Situacion_Economica'] = df['Situacion_Economica'].apply(limpiar_situacion)
    df['Impacto_Academico'] = df['Impacto_Economico'].apply(limpiar_impacto)
    df['Sentimiento_Financiero'] = df['Sentimiento_Finanzas'].apply(limpiar_sentimientos)
    df['Renuncia_Oportunidad'] = df['Renuncia_Oportunidad'].apply(limpiar_si_no)
    df['Gasto_Principal'] = df['Gasto_Dificil'].apply(limpiar_gasto)
    df['Numero_Cuenta'] = pd.to_numeric(df['Numero_Cuenta'], errors='coerce')
    cols_to_keep = ['Numero_Cuenta', 'Situacion_Economica', 'Impacto_Academico', 'Sentimiento_Financiero', 'Renuncia_Oportunidad', 'Gasto_Principal']
    return df[cols_to_keep].dropna(subset=['Numero_Cuenta'])

# --- PARTE 2: UNIÓN Y CÁLCULO DE KPIS ---
df_bienestar = cargar_y_limpiar_bienestar('Preguntas equipo 3 (respuestas).csv')
df_economia = cargar_y_limpiar_economia('Situación económica y bienestar estudiantil.csv')

if df_bienestar is not None and df_economia is not None:
    df_completo = pd.merge(df_bienestar, df_economia, on='Numero_Cuenta', how='inner')
    print(f"Unión exitosa. Se encontraron {len(df_completo)} estudiantes en ambas encuestas.")
    
    sns.set_style("whitegrid")
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Arial'
    
    # --- GRÁFICO 1: Heatmap ---
    contingency_table = pd.crosstab(df_completo['Situacion_Economica'], df_completo['Nivel_Ansiedad'])
    ansiedad_orden = ['Ninguno', 'Leve', 'Moderada', 'Grave']
    contingency_table = contingency_table.reindex(columns=ansiedad_orden, fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Relación entre Situación Económica y Nivel de Ansiedad', fontsize=16, fontweight='bold')
    plt.ylabel('Situación Económica', fontsize=12) # Añadido para claridad
    plt.xlabel('Nivel de Ansiedad', fontsize=12) # Añadido para claridad
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafico_heatmap_economia_vs_ansiedad.png'), dpi=150)
    plt.close() 

    # --- GRÁFICO 2: Promedio vs. Estrés Financiero ---
    promedio_por_estres = df_completo.groupby('Sentimiento_Financiero')['Promedio_Escolar'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=promedio_por_estres.index, y=promedio_por_estres.values, palette='viridis', ax=ax)
    ax.set_title('El Estrés Financiero se Correlaciona con un Menor Promedio', fontsize=18, fontweight='bold', pad=25)
    fig.suptitle('Promedio escolar según el sentimiento generado por las finanzas personales', fontsize=12, color='gray')
    ax.set_ylabel('Promedio Escolar (GPA)', fontsize=12, fontweight='bold')
    ax.set_xlabel('')
    ax.bar_label(ax.containers[0], fmt='%.2f', size=12, fontweight='bold')
    sns.despine(left=True, bottom=True)
    if not promedio_por_estres.empty:
        plt.ylim(promedio_por_estres.min() * 0.95, promedio_por_estres.max() * 1.02)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.figtext(0.99, 0.01, f'Fuente: Encuesta Estudiantil (N={len(df_completo)})', horizontalalignment='right', size=8, color='grey')
    plt.savefig(os.path.join(output_dir, 'grafico_promedio_vs_estres.png'), dpi=150)
    plt.close()

    # --- GRÁFICO 3: Déficit de Energía por Gasto ---
    df_sin_energia = df_completo[df_completo['Siente_Energia'] == 'No']
    energia_por_gasto = df_sin_energia['Gasto_Principal'].value_counts().sort_values()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(energia_por_gasto.index, energia_por_gasto.values, color=sns.color_palette('viridis', len(energia_por_gasto)))
    ax.set_title('El Transporte es el Gasto que Más Drena la Energía', fontsize=18, fontweight='bold', pad=25)
    fig.suptitle('Principal gasto de los estudiantes que reportan sentirse sin energía', fontsize=12, color='gray')
    ax.set_xlabel('Cantidad de Estudiantes sin Energía', fontsize=12, fontweight='bold')
    ax.set_ylabel('')
    ax.bar_label(ax.containers[0], size=12, padding=5)
    sns.despine(left=True, bottom=True)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.figtext(0.99, 0.01, f'Fuente: Encuesta Estudiantil (N={len(df_sin_energia)})', horizontalalignment='right', size=8, color='grey')
    plt.savefig(os.path.join(output_dir, 'grafico_energia_vs_gasto.png'), dpi=150)
    plt.close()
    
    # --- GRÁFICO 4: Desglose de Ansiedad Exacerbada ---
    df_ansiedad_financiera = df_completo[df_completo['Sentimiento_Financiero'] == 'Ansiedad/Preocupación']
    ansiedad_counts = df_ansiedad_financiera['Nivel_Ansiedad'].value_counts().reindex(ansiedad_orden)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(ansiedad_counts.index, ansiedad_counts.values, color=sns.color_palette('viridis_r', len(ansiedad_counts)))
    ax.set_title('Ansiedad Moderada a Grave Domina en Estudiantes con Estrés Financiero', fontsize=18, fontweight='bold', pad=25)
    fig.suptitle('Desglose del nivel de ansiedad para el grupo con preocupación financiera', fontsize=12, color='gray')
    ax.set_xlabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
    ax.set_ylabel('')
    ax.bar_label(ax.containers[0], size=12, padding=5)
    sns.despine(left=True, bottom=True)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.figtext(0.99, 0.01, f'Fuente: Encuesta Estudiantil (N={len(df_ansiedad_financiera)})', horizontalalignment='right', size=8, color='grey')
    plt.savefig(os.path.join(output_dir, 'grafico_ansiedad_exacerbada.png'), dpi=150)
    plt.close()

    print("\nAnálisis completo y generación de imágenes finalizados.")
