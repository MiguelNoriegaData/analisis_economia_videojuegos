🎮 Proyecto de Análisis de Videojuegos

Este proyecto analiza información de precios, calificaciones y tendencias en el mercado de videojuegos.
El objetivo es explorar cómo variables como la violencia, el género, la plataforma y la inflación se relacionan con el precio final de los videojuegos.

---

## 📂 Estructura del Proyecto
proyecto_analisis_videojuegos/
│
├── data/
│   ├── data_games_analysis_FINAL.xls     # Base de datos original
│   ├── data_games_analysis_FINAL.csv     # Versión en formato CSV (para análisis con pandas)
│
├── analisis_visualizaciones.py           # Script principal de análisis y visualización
├── analisis_inicial.py                   # Script para exploración inicial del dataset
├── README.md                             # Documento principal del proyecto
│
└── output/
    ├── boxplot_violencia_precio.png
    ├── distribucion_general_precios.png
    ├── histograma_precios_2026_mejorado.png
    ├── scatter_inflacion_vs_actual.png
    ├── mapa_correlaciones.png            # Mapa de calor de correlaciones


---

## 📊 Análisis Realizados

1. Distribución de precios (histograma mejorado)
Permite ver cómo se concentran los precios y detectar si hay sesgos hacia rangos altos o bajos.

2. Boxplot de violencia vs precio
Analiza si el nivel de violencia en un juego influye en su precio promedio.

3. Gráfica de correlación (heatmap)
Muestra las relaciones entre variables numéricas clave: inflación, precio actual, precio ajustado, etc.

4. Dispersión inflación vs precio actual
Identifica si existe una relación significativa entre inflación y precios finales.

---

## ⚙️ Requisitos del Proyecto

Asegúrate de tener instaladas las siguientes librerías antes de ejecutar el script:
pip install pandas matplotlib seaborn numpy
```bash
pip install pandas matplotlib seaborn numpy

▶️ Ejecución del Proyecto
Para generar las visualizaciones, ejecuta desde la terminal:
python analisis_visualizaciones.py
Las gráficas generadas se guardarán automáticamente en la carpeta /output.

🧠 Conclusiones Generales
* Los precios de los videojuegos tienden a concentrarse en un rango medio, con pocos títulos extremadamente caros.
* La violencia puede estar relacionada con una ligera tendencia al aumento de precios, posiblemente por la popularidad de géneros de acción.
* La inflación influye de forma moderada en los precios finales, pero no de manera directa.
* El análisis visual permite comprender mejor los patrones del mercado y apoyar decisiones de compra o diseño de estrategias comerciales.
* Las visualizaciones ayudan a comprender mejor el comportamiento del mercado gamer.

🧾 Autor
Miguel Noriega
Proyecto de análisis de datos y visualización — 2025

🧠 Tecnologías Usadas
Python 3.13
Pandas
Matplotlib
Seaborn
NumPy

💡 Próximos pasos
* Ampliar el dataset con nuevas variables (ventas, reseñas, popularidad).
* Crear un dashboard interactivo (por ejemplo, con Power BI o Plotly).
* Analizar tendencias temporales o estacionales del mercado gamer.
