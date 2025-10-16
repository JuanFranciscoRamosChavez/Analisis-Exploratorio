import os
import sys

# --- Script Maestro para Ejecutar Todos los Análisis ---

print("\nIniciando la ejecución de todos los scripts de análisis...")
print("-" * 50)

# Verificamos qué comando usar para python (python o python3)
python_command = sys.executable

# --- Paso 1: Ejecutar el script economia.py ---
script_a_ejecutar = 'economia.py'
print(f"\nEjecutando {script_a_ejecutar}...")
exit_code = os.system(f'"{python_command}" {script_a_ejecutar}')
if exit_code != 0:
    print(f" ¡Error al ejecutar {script_a_ejecutar}!")
else:
    print(f"\n{script_a_ejecutar} finalizado.\n")
print("-" * 50)

# --- Paso 2: Ejecutar el script main.py ---
script_a_ejecutar = 'estres.py'
print(f"\nEjecutando {script_a_ejecutar}...")
exit_code = os.system(f'"{python_command}" {script_a_ejecutar}')
if exit_code != 0:
    print(f" ¡Error al ejecutar {script_a_ejecutar}!")
else:
    print(f"\n{script_a_ejecutar} finalizado.\n")
print("-" * 50)

# --- Paso 3: Ejecutar el script combinacion.py ---
script_a_ejecutar = 'combinacion.py'
print(f"\nEjecutando {script_a_ejecutar}...")
exit_code = os.system(f'"{python_command}" {script_a_ejecutar}')
if exit_code != 0:
    print(f" ¡Error al ejecutar {script_a_ejecutar}!")
else:
    print(f"\n{script_a_ejecutar} finalizado.\n")
print("-" * 50)

print("\nTodos los scripts han sido ejecutados.")