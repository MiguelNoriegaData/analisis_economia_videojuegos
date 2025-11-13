# =====================================================
# ANALISIS INICIAL - Proyecto Videojuegos
# Autor: Miguel
# Fecha: 2025
# Descripción:
#   Este script realiza una exploración inicial del dataset
#   principal de videojuegos, incluyendo vistas generales,
#   información de columnas y estadísticas descriptivas.
# =====================================================

import pandas as pd
import os

# === Configuración de rutas ===
# Obtener el directorio actual del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "data_games_analysis_FINAL.xlsx")

# === Cargar la base de datos ===
df = pd.read_excel(DATA_PATH)

# === Vista general ===
print("\n--- Primeras filas del dataset ---")
print(df.head())

# === Información general ===
print("\n--- Información general ---")
print(df.info())

# === Estadísticas descriptivas ===
print("\n--- Estadísticas descriptivas ---")
print(df.describe())