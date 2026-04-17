![Banner](Figuras/banner.svg)

# Workshop: IA Interpretable en Neurooncología: Decodificando la severidad tumoral mediante resonancia multimodal

---
<p align="center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLScVTNZGnZ7jFYkFfVNsTKiw_LQcgZfaXG4y_08lIPOTNVzjhA/viewform?usp=sharing" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Inscripción-Workshop-074E8C?style=for-the-badge&logo=googleforms&logoColor=white" alt="Inscripción" />
  </a>

  <a href="https://docs.google.com/viewer?url=https://raw.githubusercontent.com/pamelaFranco/workshop_glioma/main/Programa/Charlas___Workshop_IA_Interpretable_Neurooncologia.pdf" target="_blank">
    <img src="https://img.shields.io/badge/Programa-PDF-A63737?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="Programa" />
  </a>

  <a href="https://www.instagram.com/neuro_artint/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Instagram-NeuroArtInt-F2A20C?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
</p>

<p align="center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLScrvB4-sUyraLQAthbE9K0Ph2O1xWT8xWlNHzRo8drDvrYp3Q/viewform?usp=sharing">
    <img src="https://img.shields.io/badge/Abstract-Enviar_aquí-402C7C?style=for-the-badge&logo=googlesheets&logoColor=white" />
  </a>
  <a href="mailto:neurooncologia.ia@gmail.com">
    <img src="https://img.shields.io/badge/Consultas-Email-38585B?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</p>

---

## Introducción
Este repositorio contiene los materiales para el laboratorio virtual sobre neurooncología de precisión. El workshop integra seis fases críticas del análisis de imágenes médicas:

1. **Fundamentos del Espacio K:** Exploración del dominio de la frecuencia en RM.
2. **Física de Resonancia:** Generación de mapas paramétricos ($T1$ y $T2$).
3. **Microestructura Tisular:** Procesamiento de Tensores de Difusión ($DTI$).
4. **Mapeo Funcional:** Exploración de la dinámica de la señal $BOLD$ y $fMRI$.
5. **Hemodinámica y Biomecánica:** Reconstrucción de vasculatura mediante $TOF-MRA$.
6. **IA Interpretable:** Decodificación de severidad mediante radiómica y $SHAP$.

---

## Cómo usar este Workshop

La forma más sencilla de ejecutar el laboratorio es a través de **Google Colab**, ya que no requiere instalación local.

1. **Selecciona el módulo:** Haz clic en el botón **"Open In Colab"** de la actividad deseada.
2. **Configuración de Datos:** Los notebooks cargan automáticamente los archivos desde este repositorio. Ejecuta las celdas en orden correlativo.
3. **Interactividad:** Los laboratorios están diseñados como entornos de exploración dinámica. En cada módulo encontrarás herramientas interactivas para manipular datos médicos en tiempo real:

    * **Manipulación del Espacio K:** Utiliza *sliders* para filtrar frecuencias en el dominio de Fourier. Observa instantáneamente cómo la eliminación de información afecta la reconstrucción de la imagen y la visibilidad de estructuras tumorales.
    * **Exploración de Mapas de Relajación (T1/T2):** Interactúa con los algoritmos de ajuste para visualizar mapas paramétricos que diferencian tejidos sanos de lesiones oncológicas.
    * **Conectividad y Hemodinámica:**
        * **fMRI:** Explora umbrales de activación estadística para identificar redes funcionales cerebrales.
        * **Vasculatura:** Ajusta niveles de segmentación en proyecciones TOF para aislar la red vascular cerebral.
        * **DTI:** Visualiza la anisotropía y la integridad de los tractos de materia blanca afectados por el edema o la infiltración tumoral.
    * **Simulador Clínico e IA Interpretable (SHAP):** En el módulo de clasificación de gliomas, ajusta variables del paciente (edad, volumen, ubicación) y observa cómo el modelo de IA actualiza sus predicciones y explicaciones visuales.
---

## Actividades del Workshop

### *Hands-on* I: Fundamentos del Espacio K y Formación de Imágenes
* **Objetivo:** Comprender la relación entre el Espacio K y la imagen real mediante la Transformada de Fourier.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/EspacioK.ipynb)

### *Hands-on* II: Generación de Mapas Paramétricos ($T1$ y $T2$)
* **Objetivo:** Calcular mapas de tiempos de relajación utilizando modelos de ajuste no lineal.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/T1_T2_maps.ipynb)

### *Hands-on* III: Mapas de Difusión ($DTI$)
* **Objetivo:** Mapear la arquitectura funcional del cerebro mediante el análisis de correlaciones de señales de baja frecuencia en estado de reposo ($rs-fMRI$).
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/DTI_mapas_difusion.ipynb)

### *Hands-on* IV: Mapeo Funcional ($fMRI$)
* **Objetivo:** Obtener mapas de Fracción de Anisotropía ($FA$), Difusividad Media ($MD$), Difusividad Radial ($RD$) y Difusividad Axial ($AD$) para caracterizar la infiltración tumoral.
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/fMRI.ipynb)

### *Hands-on* V: Hemodinámica y Biomecánica Cerebral ($TOF-MRA$)
* **Objetivo:** Reconstrucción de la vasculatura mediante el uso de imágenes adquiridas en la secuencia Time-Of-Flight ($TOF-MRA$) y la aplicación de la Proyección de Máxima Intensidad ($MIP$).
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/Vasculatura_Cerebral.ipynb)

### *Hands-on* VI: Predicción de Severidad con IA (Radiómica)
* **Objetivo:** Modelar la severidad del tumor mediante Machine Learning interpretable (Caja Blanca).
* **Cuaderno:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pamelaFranco/workshop_glioma/blob/main/Code/Glioma_classification.ipynb)

---

## Envío de Resúmenes ($Abstracts$)

Invitamos a investigadores y especialistas a presentar trabajos relacionados con procesamiento de imágenes médicas, Machine Learning/Deep Learning y aplicaciones en salud.

> **Fecha límite:** 15 de noviembre de 2026, 23:59 PM (UTC-3).

### ¿Cómo obtener la plantilla?
* **Opción A: Formato Word** - [Descargar desde Google Drive](https://docs.google.com/document/d/1190HBUgn2zWm8GyvswGrgzw2nrgt1yDC/edit?usp=drive_link&ouid=100388382858978154255&rtpof=true&sd=true)
* **Opción B: Formato LaTeX** - [Acceder a los archivos en GitHub](https://github.com/pamelaFranco/workshop_glioma/blob/main/Formato%20Abstract/Formato_Resumen___Workshop_IA_Interpretable_Neurooncologia.zip)

---

## Estructura del Repositorio

* **`Code/`**: Notebooks `.ipynb` de todas las actividades.
* **`Dataset/`**: Archivos `.mat`, `.nii.gz`, `.dcm` y `.csv` necesarios para los análisis.
* **`Figuras/`**: Recursos visuales y diagramas explicativos.
* **`Formato Abstract/`**: Planillas para escribir el resumen ($abstract$) en formato Word y LaTeX.
* **`Template/`**: Formato editable de la charla (PPTX) e instrucciones del formato póster a presentar el día del evento.
* **`Programa/`**: Cronograma del workshop con los expositores y sus horarios.
---

## Requisitos Técnicos (Uso Local)
Si prefieres ejecución local, requiere:
* Python 3.10+
* Librerías: `pandas`, `numpy`, `scikit-learn`, `nibabel`, `dipy`, `nilearn`, `shap`, `matplotlib`, `scipy`.


---

## Respaldo Científico y Cita

Este laboratorio virtual implementa los findazgos descritos en el estudio:

<p align="center">
  <a href="https://link.springer.com/article/10.1007/s10334-025-01278-8">
    <img src="https://img.shields.io/badge/Ver_en_ESMRMB_2025-496C76?style=for-the-badge&logo=springer&logoColor=white" />
  </a>
  <a href="https://ieeexplore.ieee.org/document/11302837">
    <img src="https://img.shields.io/badge/Ver_en_ICPRS_2025-533A72?style=for-the-badge&logo=ieee&logoColor=white" />
  </a>
</p>

Si utilizas este código o dataset para tu investigación, por favor cita los siguientes trabajos:

```bibtex
@article{Franco2026Glioma,
  title={Beyond Binary Classification: A Pilot Study of Imaging-Derived Glioma Severity Modeling Using T1-Weighted and Diffusion MRI Radiomics},
  author={Franco, Pamela and Montalba, Cristian and Caulier-Cisterna, Raúl and Espinoza, Ignacio and Cornejo, M. Daniela and others},
  journal={Magnetic Resonance Materials in Physics, Biology and Medicine (MAGMA)},
  year={2026},
  note={10.1007/s10334-026-01346-7}
}

@inproceedings{Franco2025ICPRS,
  title={Radiomic Glioma Grading Using T1-weighted MRI vs. Diffusion Tensor Metrics: A Proof-of-Concept Comparative Analysis with Explainable Machine Learning},
  author={Franco, Pamela and Montalba, Cristian and Caulier-Cisterna, Raúl and Espinoza, Ignacio and Cornejo, and others},
  booktitle={2025 15th IEEE International Conference on Pattern Recognition Systems (ICPRS)},
  pages={1--7},
  year={2025},
  publisher={IEEE},
  doi={10.1109/ICPRS64124.2025.11302837}
}

@article{Franco2025ESMRMB,
  title={Explainable machine learning models for radiomic-based assessment of glioma severity using multiparametric MRI (Abstract \#215)},
  author={Franco, Pamela and Montalba, Cristian and Caulier-Cisterna, Raúl and Espinoza, Ignacio and Bennet, Carlos and Torres, Francisco and Chabert, Steren and Salas, Rodrigo},
  journal={Magnetic Resonance Materials in Physics, Biology and Medicine},
  volume={38},
  number={1},
  pages={201--202},
  year={2025},
  publisher={Springer},
  doi={10.1007/s10334-025-01278-8}
}

```

---

##  Agradecimientos
Este trabajo fue financiado por el Concurso Endowment I + D en Salud de la Universidad Andrés Bello (UNAB) 2025, proyecto DI-07-25/ICS


--- 

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

