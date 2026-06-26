---
layout: page
title: "Actividades del Workshop"
permalink: /actividades/
---

La forma más sencilla de ejecutar el laboratorio es a través de **Google Colab**, ya que no requiere instalación local.

1. **Selecciona el módulo:** Haz clic en el botón **"Open In Colab"** de la actividad deseada.
2. **Configuración de Datos:** Los notebooks cargan automáticamente los archivos desde este repositorio. Ejecuta las celdas en orden correlativo.
3. **Interactividad:** Los laboratorios están diseñados como entornos de exploración dinámica. En cada módulo encontrarás herramientas interactivas para manipular datos médicos en tiempo real:

    * **Manipulación del Espacio K:** Utiliza *sliders* para filtrar frecuencias en el dominio de Fourier. Observa instantáneamente cómo la eliminación de información afecta la reconstrucción de la imagen.
    * **Simulación de Magnetización (Ecuaciones de Bloch):** Ajusta parámetros de adquisición ($TR$, $TE$, $\alpha$) y constantes de tejido ($T1$, $T2$) para observar las curvas de relajación y entender la física detrás de la generación de contraste en el fantoma.
    * **Exploración de Mapas de Relajación (T1/T2):** Interactúa con los algoritmos de ajuste para visualizar mapas paramétricos que diferencian tejidos sanos de lesiones oncológicas.
    * **Conectividad y Hemodinámica:**
        * **fMRI:** Explora umbrales de activación estadística para identificar redes funcionales cerebrales.
        * **Vasculatura:** Ajusta niveles de segmentación en proyecciones TOF para aislar la red vascular cerebral.
        * **DTI:** Visualiza la anisotropía y la integridad de los tractos de materia blanca afectados por el edema o la infiltración tumoral.
    * **Extracción de Características de Radiómica:** Este módulo actúa como una 'biopsia virtual por software' que extrae la firma digital oculta del glioma, transformando los patrones visuales de la resonancia magnética en mapas de colores y números que miden objetivamente la agresividad, el caos y la heterogeneidad del tumor.
    * **Flujo de Procesamiento y Clasificación Automatizada:** Un pipeline integrado que transforma el caos de los datos radiómicos en un diagnóstico preciso. El sistema normaliza las variables y aplica un filtro de varianza para retener las características críticas; luego, proyecta estas firmas multidimensionales en un mapa visual bidimensional y entrena un clasificador probabilístico para diferenciar LGG de HGG, evaluando rigurosamente su rendimiento mediante métricas de sensibilidad y matrices de confusión clínica.
    * **Simulador Clínico e IA Interpretable (SHAP):** En el módulo de clasificación de gliomas, ajusta variables del paciente (edad, volumen, ubicación) y observa cómo el modelo de IA actualiza sus predicciones y explicaciones visuales.

---

### *Hands-on* I.A: Fundamentos del Espacio K y Formación de Imágenes
* **Objetivo:** Comprender la relación entre el Espacio K y la imagen real mediante la Transformada de Fourier.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/EspacioK.ipynb)

### *Hands-on* I.B: Simulador Interactivo de Secuencias (Ecuaciones de Bloch)
* **Objetivo:** Experimentar en tiempo real con los parámetros de adquisición ($TR$, $TE$, $\alpha$) y observar su efecto en la magnetización y el contraste del fantoma.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/simulador_secuencias.ipynb)

### *Hands-on* II: Generación de Mapas Paramétricos ($T1$ y $T2$)
* **Objetivo:** Calcular mapas de tiempos de relajación utilizando modelos de ajuste no lineal.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/T1_T2_maps.ipynb)

### *Hands-on* III: Mapas de Difusión ($DTI$)
* **Objetivo:** Obtener mapas de Fracción de Anisotropía ($FA$), Difusividad Media ($MD$), Difusividad Radial ($RD$) y Difusividad Axial ($AD$) para caracterizar la infiltración tumoral.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/DTI_mapas_difusion.ipynb)

### *Hands-on* IV: Mapeo Funcional ($fMRI$)
* **Objetivo:** Mapear la arquitectura funcional del cerebro mediante el análisis de correlaciones de señales de baja frecuencia en estado de reposo ($rs-fMRI$).
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/fMRI.ipynb)

### *Hands-on* V: Hemodinámica y Biomecánica Cerebral ($TOF-MRA$)
* **Objetivo:** Reconstrucción de la vasculatura mediante el uso de imágenes adquiridas en la secuencia Time-Of-Flight ($TOF-MRA$) y la aplicación de la Proyección de Máxima Intensidad ($MIP$).
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/Vasculatura_Cerebral.ipynb)

### *Hands-on* VI: Extracción de Características y Mapas de Textura (GLCM) 
* **Objetivo:** Cuantificar la microestructura y heterogeneidad del glioma mediante la extracción de características radiómicas de textura de segundo orden (GLCM) a nivel de vóxel.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/radiomics.ipynb)

### *Hands-on* VII.A: Clasificación y Pipeline Radiómico 
* **Objetivo:** Construir un pipeline de Machine Learning para clasificar el grado tumoral (LGG vs. HGG) a partir de firmas radiómicas.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/ML.ipynb)

### *Hands-on* VII.B: Predicción de Severidad con IA 
* **Objetivo:** Modelar la severidad del tumor mediante Machine Learning interpretable (Caja Blanca).
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/Glioma_classification.ipynb)

---

## Estructura del Repositorio

* **`Code/`**: Notebooks `.ipynb` ($Hands-on$).
* **`Dataset/`**: Datos multimodales (`.mat`, `.nii.gz`, `.dcm` y `.csv`).
* **`Figuras/`**: Recursos visuales y diagramas explicativos.
* **`Formato Abstract/`**: Planillas para escribir el resumen ($abstract$) en formato Word y LaTeX.
* **`Template/`**: Formato editable de la charla (PPTX) e instrucciones del formato póster a presentar el día del evento.
* **`Programa/`**: Cronograma detallado en PDF.