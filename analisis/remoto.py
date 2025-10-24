import subprocess
import sys
import os

print("Iniciando la ejecución de todos los scripts de análisis...")
scripts_a_ejecutar = [
    'analizar_economia.py',     # 1. Primero este (genera economia_limpio.csv)
    'analizar_estilo_vida.py',  # 2. Segundo este (genera estilo_vida_limpio.csv)
    'analizar_combinado.py'     # 3. Al último (usa los dos CSV anteriores)
]

python_executable = sys.executable

for script in scripts_a_ejecutar:
    print(f"\nEjecutando {script}...")
    try:
        subprocess.run(
            [python_executable, script], 
            check=True, 
            text=True, 
            encoding='utf-8'
        )
        print(f"\n--- {script} finalizado. ---")
    
    except subprocess.CalledProcessError as e:
        print(f"*** ERROR al ejecutar {script}: ***")
        print(f"Salida: {e.stdout}")
        print(f"Error: {e.stderr}")
        print("Deteniendo la ejecución remota.")
        break 
    
    except FileNotFoundError:
        print(f"*** ERROR: No se encontró el script '{script}' ***")
        print("Asegúrate de que todos los scripts estén en la misma carpeta.")
        print("Deteniendo la ejecución remota.")
        break

print("\nTodos los scripts han sido ejecutados.")