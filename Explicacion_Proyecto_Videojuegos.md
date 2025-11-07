# Proyecto de Análisis del Mercado de Videojuegos (2025--2026)

Este documento explica detalladamente cómo se construyó la base de datos
y el proceso detrás de cada columna, fórmula y decisión tomada.

------------------------------------------------------------------------

## 🎯 Objetivo del proyecto

Analizar la evolución de precios, ventas y factores económicos del
mercado de videojuegos entre 2020 y 2026, con especial énfasis en los
títulos más recientes (2020 en adelante).\
El propósito final es desarrollar un portafolio de análisis que combine
datos reales y proyecciones fundamentadas, para mostrar habilidades en
limpieza, análisis y visualización de datos.

------------------------------------------------------------------------

## 📁 Estructura del archivo Excel

El archivo principal contiene varias pestañas, pero la pestaña base
incluye las siguientes columnas:

### 1. **nombre_juego**

-   Título del videojuego.
-   Seleccionados principalmente títulos populares y de relevancia
    comercial.
-   Se incluyen juegos de 2020 en adelante, con prioridad a lanzamientos
    recientes o próximos (2025--2026).

### 2. **anio_lanzamiento**

-   Año de salida oficial o prevista del videojuego.
-   Para 2025 y 2026 se consideraron datos proyectados y precios de
    preventa.

### 3. **precio_usd_2025**

-   Precio del videojuego en dólares estadounidenses para el año 2025.
-   Si el juego ya está lanzado, se usó su precio oficial de lista
    (Steam, PlayStation Store, etc.).\
-   Si aún no ha salido (ej. lanzamientos 2026), se utilizó el precio
    estimado de preventa.

### 4. **tipo_cambio_target**

-   Tasa de conversión utilizada para calcular el precio equivalente en
    pesos mexicanos.
-   Para los años **≤ 2025**, se usó el mismo valor del tipo de cambio
    promedio estimado de **18.02 MXN/USD** (dato realista según el
    comportamiento reciente del peso).\
-   Para el año **2026**, se aplicó un **tipo de cambio proyectado de
    18.65 MXN/USD**, que refleja una ligera depreciación esperada.

> 💡 **Motivo:** Se mantiene estable el tipo de cambio hasta 2025 para
> reflejar la tendencia actual, y se incrementa ligeramente para 2026
> con base en proyecciones económicas moderadas.

### 5. **precio_mxn_target**

-   Precio del juego convertido a pesos mexicanos según el tipo de
    cambio correspondiente.
-   Fórmula:\
    \\( `\text{precio\_mxn\_target}`{=tex} =
    `\text{precio\_usd\_2025}`{=tex}
    `\times `{=tex}`\text{tipo\_cambio\_target}`{=tex} )

### 6. **inflacion_anual**

-   Inflación estimada del sector de entretenimiento digital.
-   Valor de referencia: **8%** anual, aplicado principalmente a los
    títulos de 2026 o aquellos con alta demanda.
-   Se calculó considerando el incremento general en precios de juegos
    AAA y las tendencias del mercado global.

### 7. **precio_ajustado_2026**

-   Precio ajustado por inflación o proyección de mercado.
-   Fórmula:\
    \\( `\text{precio\_ajustado\_2026}`{=tex} =
    `\text{precio\_mxn\_target}`{=tex} `\times `{=tex}(1 +
    `\text{inflacion\_anual}`{=tex}) )

> Ejemplo: si un juego cuesta 1,000 MXN en 2025, y la inflación esperada
> es del 8%, su precio proyectado para 2026 será de 1,080 MXN.

### 8. **ventas_estimadas**

-   Estimación de ventas basada en popularidad, franquicia, género y
    expectativas de lanzamiento.
-   Se agrupan tres niveles:
    -   **Alta:** \> 5 millones de copias (franquicias establecidas como
        GTA, Call of Duty, etc.)
    -   **Media:** entre 1 y 5 millones.
    -   **Baja:** \< 1 millón (juegos de nicho o independientes).

### 9. **ingresos_estimados**

-   Cálculo del ingreso total esperado en pesos.
-   Fórmula:\
    \\( `\text{ingresos\_estimados}`{=tex} =
    `\text{ventas\_estimadas}`{=tex}
    `\times `{=tex}`\text{precio\_ajustado\_2026}`{=tex} )

------------------------------------------------------------------------

## ⚙️ Proceso general del proyecto

1.  **Selección de juegos:** se filtraron títulos lanzados desde 2020 en
    adelante.
2.  **Limpieza de datos:** se unificaron nombres, monedas y formatos de
    fechas.
3.  **Conversión de precios:** se aplicó el tipo de cambio target y los
    ajustes inflacionarios.
4.  **Proyección 2026:** se generaron valores nuevos para precios e
    ingresos esperados.
5.  **Exportación final:** el archivo corregido se guardó en formato
    Excel y se documentó con este texto.

------------------------------------------------------------------------

## 💬 Conclusión

Este proyecto integra datos reales y estimaciones razonadas, simulando
un análisis financiero del mercado gamer.\
Las decisiones sobre el tipo de cambio, inflación y selección de juegos
se basan en proyecciones económicas y tendencias del sector tecnológico.

------------------------------------------------------------------------

**Autor:** Miguel Noriega\
**Año:** 2025\
**Propósito:** Proyecto de portafolio para análisis de datos y
visualización profesional.
