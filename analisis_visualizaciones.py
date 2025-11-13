# =====================================================
# ANALISIS VISUALIZACIONES - Proyecto Videojuegos
# Autor: Miguel
# Fecha: 2025
# Descripción:
#   Este script genera las visualizaciones principales
#   del análisis de precios de videojuegos. Se aplican
#   mejoras de estética, claridad y robustez en todas
#   las gráficas, las cuales se guardan en /output.
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Constantes clave para claridad ---
COL_PRECIO_ACTUAL = "precio_actual_target_mxn_resolved"
COL_PRECIO_PROYECTADO = "precio_proyectado_2026_mxn_final"
COL_PRECIO_INFLACION_USA = "precio_ajustado_inflacion_target_mxn_CPI_USA_final"
COL_VIOLENCIA = "violento_bool"

# ===============================
# 1. Configuración inicial
# ===============================
ruta_datos = os.path.join("data", "data_games_analysis_FINAL.xlsx")
ruta_output = os.path.join("output")

# Crear carpeta /output si no existe
os.makedirs(ruta_output, exist_ok=True)

# Cargar los datos
try:
    df = pd.read_excel(ruta_datos)
except FileNotFoundError:
    raise FileNotFoundError(f"❌ No se encontró el archivo en la ruta: {ruta_datos}")

# Estilo general
sns.set(style="whitegrid", palette="deep", font_scale=1.2)

# ===============================
# 2. Distribución general de precios ajustados
# ===============================
plt.figure(figsize=(10, 6))
sns.histplot(df[COL_PRECIO_ACTUAL], kde=True, bins='auto', color="#3498db")
plt.title("Distribución general de precios ajustados (MXN)", fontsize=16, fontweight='bold')
plt.xlabel("Precio ajustado a valor Target (MXN)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig(os.path.join(ruta_output, "distribucion_general_precios_mejorada.png"), dpi=300)
plt.close()

# ===============================
# 3. Violin Plot: relación entre violencia y precios
# ===============================
plt.figure(figsize=(9, 7))
df['Violento'] = df[COL_VIOLENCIA].map({True: 'Sí', False: 'No'})
sns.violinplot(
    data=df, 
    x='Violento', 
    y=COL_PRECIO_ACTUAL, 
    palette=["#2ecc71", "#e74c3c"], 
    inner="quartile", 
    linewidth=1.5
)
plt.title("Precio Ajustado por Categoría de Violencia", fontsize=16, fontweight='bold')
plt.xlabel("¿Es un videojuego violento?")
plt.ylabel("Precio ajustado (MXN)")
plt.tight_layout()
plt.savefig(os.path.join(ruta_output, "violinplot_violencia_precio_mejorada.png"), dpi=300)
plt.close()
df.drop(columns=['Violento'], inplace=True)

# ===============================
# 4. Histograma de precios proyectados a 2026
# ===============================
plt.figure(figsize=(10, 6))
sns.histplot(df[COL_PRECIO_PROYECTADO], kde=True, bins='auto', color="#e67e22")
plt.title("Distribución de precios proyectados a 2026 (MXN)", fontsize=16, fontweight='bold')
plt.xlabel("Precio proyectado 2026 (MXN)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig(os.path.join(ruta_output, "histograma_precios_2026_mejorado.png"), dpi=300)
plt.close()

# ===============================
# 5. Regplot: inflación vs precio actual
# ===============================
plt.figure(figsize=(10, 8))
sns.regplot(
    data=df,
    x=COL_PRECIO_INFLACION_USA,
    y=COL_PRECIO_ACTUAL,
    scatter_kws={'alpha': 0.6, 's': 50},
    line_kws={'color': 'red', 'linestyle': '--', 'alpha': 0.7}
)
plt.title("Relación entre Precio Ajustado por Inflación (USA) y Precio Actual", fontsize=16, fontweight='bold')
plt.xlabel("Precio Ajustado por Inflación (USA, en MXN)")
plt.ylabel("Precio actual (MXN)")
plt.tight_layout()
plt.savefig(os.path.join(ruta_output, "regplot_inflacion_vs_actual_mejorado.png"), dpi=300)
plt.close()

# ===============================
# 6. Mapa de correlación entre variables clave
# ===============================
COLUMNAS_CLAVE_CORR = [
    "anio_lanzamiento",
    "precio_original_usd",
    "equivalente_mxn_historico",
    "precio_usd_ajustado_target",
    COL_PRECIO_INFLACION_USA,
    "precio_ajustado_inflacion_target_mxn_CPI_MX_final",
    COL_PRECIO_ACTUAL,
    COL_PRECIO_PROYECTADO,
    COL_VIOLENCIA 
]

df_corr = df[COLUMNAS_CLAVE_CORR].copy()
df_corr[COL_VIOLENCIA] = df_corr[COL_VIOLENCIA].astype(int)
correlaciones = df_corr.fillna(df_corr.median()).corr()

plt.figure(figsize=(12, 10))
sns.heatmap(
    correlaciones,
    cmap='vlag',
    annot=True,
    fmt=".2f",
    linewidths=0.7,
    linecolor='white',
    cbar_kws={'label': 'Coeficiente de correlación'},
    annot_kws={"size": 9}
)
plt.title('Mapa de Correlación entre Variables de Precio Clave', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(ruta_output, "heatmap_correlacion_clave_mejorada.png"), dpi=300)
plt.close()

print("✅ Todas las visualizaciones se generaron y guardaron correctamente en la carpeta /output.")