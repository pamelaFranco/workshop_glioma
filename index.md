---
layout: about
title: "Workshop: IA Interpretable en Neurooncología"
permalink: /
author_profile: true
---

![Banner](Figuras/banner.svg)

<p align="center">
  <a href="https://www.ismrm.org/meetings-workshops/endorsement-request/">
    <img src="https://img.shields.io/badge/ISMRT--Endorsed-Workshop-005A9C?style=for-the-badge" alt="ISMRT Endorsed">
  </a>
</p>

> **Gran Noticia / Announcement:** ¡Este Workshop cuenta con el **respaldo y endoso oficial de la ISMRT** (International Society for Magnetic Resonance Technicians)! El patrocinio institucional fue discutido y aprobado por el comité ejecutivo durante la reunión anual en Ciudad del Cabo (Cape Town).

---

<p align="center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLScVTNZGnZ7jFYkFfVNsTKiw_LQcgZfaXG4y_08lIPOTNVzjhA/viewform?usp=sharing" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Inscripción-Presencial-074E8C?style=for-the-badge&logo=googleforms&logoColor=white" alt="Inscripción Presencial" />
  </a>
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSffyLNNJZKNM4mLKOeudr3ltQmXyKQiwgkqvS51f6Oqe73-_A/viewform?usp=publish-editor" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Inscripción-Online-1182C4?style=for-the-badge&logo=zoom&logoColor=white" alt="Inscripción Online" />
  </a>
  <a href="https://docs.google.com/viewer?url=https://raw.githubusercontent.com/pamelaFranco/workshop_glioma/main/Programa/Charlas___Workshop_IA_Interpretable_Neurooncologia.pdf" target="_blank">
    <img src="https://img.shields.io/badge/Programa-PDF-A63737?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="Programa" />
  </a>
  <a href="https://www.instagram.com/neuro_artint/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Instagram-NeuroArtInt-F2A20C?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
</p>

<p align="center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLScrvB4-sUyraLQAthbE9K0Ph2O1xWT8xWlNHzRo8drDvrYp3Q/viewform?usp=sharing" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Abstract-Enviar_aquí-402C7C?style=for-the-badge&logo=googlesheets&logoColor=white" alt="Enviar Abstract" />
  </a>
  <a href="mailto:neurooncologia.ia@gmail.com">
    <img src="https://img.shields.io/badge/Consultas-Email-38585B?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

---

## Información del Evento

| Fecha | Horario | Lugar / Modalidad |
| :---: | :---: | :--- |
| 10 de diciembre de 2026 | 8:00 AM - 17:00 PM (GMT-4 / Hora de Chile)| **Presencial:** Auditorio Zócalo, Universidad Andrés Bello <br> (Antonio Varas 880, Providencia, Santiago, Chile) <br><br> **Online:** Vía Zoom (Enlace enviado tras inscripción) |

---

## Introducción
Este repositorio contiene los materiales para el laboratorio virtual sobre neurooncología de precisión. El workshop integra nueve fases críticas del análisis de imágenes médicas:

1. **Fundamentos del Espacio K:** Exploración del dominio de la frecuencia en RM.
2. **Simulación de Secuencias:** Modelado interactivo de las ecuaciones de Bloch para entender el contraste ($TR$, $TE$, $\alpha$).
3. **Física de Resonancia:** Generación de mapas paramétricos ($T1$ y $T2$).
4. **Microestructura Tisular:** Procesamiento de Tensores de Difusión ($DTI$).
5. **Mapeo Funcional:** Exploración de la dinámica de la señal $BOLD$ y $fMRI$.
6. **Hemodinámica y Biomecánica:** Reconstrucción de vasculatura mediante $TOF-MRA$.
7. **Extracción de Características de Radiómica:** Extracción de características cuantitativas de grado médico a partir de la distribución de grises en imágenes digitales.
8. **Pipeline Radiómico para la Clasificación de Gliomas (LGG vs. HGG):** Selección de características críticas y clasificación automatizada a partir de métricas extraídas de resonancia magnética en T1, utilizando datos clínicos reales para diferenciar bajo y alto grado.
9. **IA Interpretable:** Decodificación de severidad mediante radiómica y $SHAP$.

---

## Cómo usar este Workshop

### Obtener los materiales
Puedes trabajar con los materiales de este workshop de dos maneras:

* **Opción A (Recomendada):** Clonar el repositorio localmente mediante Git ejecutando en tu terminal:
    ```bash
    git clone [https://github.com/pamelaFranco/workshop_glioma.git](https://github.com/pamelaFranco/workshop_glioma.git)
    ```
* **Opción B:** Descargar el archivo comprimido directamente en formato ZIP haciendo [clic aquí](https://github.com/pamelaFranco/workshop_glioma/archive/refs/heads/main.zip) (o desde el botón verde **"Code" > "Download ZIP"** en la parte superior de esta página de GitHub).

### Requisitos Técnicos (Uso Local)
Si prefieres ejecución local, requiere:
* Python 3.10+
* Librerías: `pandas`, `numpy`, `scikit-learn`, `nibabel`, `dipy`, `nilearn`, `shap`, `matplotlib`, `scipy`, `os`, `pyradiomics`.

---

## Alianza e Integración Internacional
Este workshop se presenta en el marco de **REBECCA-IA**, una iniciativa financiada por el Programa Iberoamericano de Ciencia y Tecnología para el Desarrollo (CYTED) e impulsada por el [Instituto Tecnológico de Medellín (ITM)](https://www.itm.edu.co).

<details>
<summary> <b>¿Qué significa REBECCA-IA? (Haz clic para desplegar)</b></summary>
<br>
* **RE**d
* I**be**roamericana para el
* **C**ontrol Inteligente e Individualizado en el Tratamiento del
* **Cá**ncer con
* **I**nteligencia
* **A**rtificial
</details>
<br>
<p align="left">
  <a href="https://www.itm.edu.co" target="_blank" rel="noopener noreferrer">
    <img src="https://github.com/pamelaFranco/workshop_glioma/raw/main/Figuras/rebeccaia.svg" alt="Logo REBECCA-IA" width="220"/>
  </a>
</p>

---

## Reconocimiento Internacional
<table border="0" width="100%">
  <tr>
    <td width="25%" align="center" valign="middle">
      <a href="https://www.ismrm.org/ismrt/" target="_blank" rel="noopener noreferrer">
        <img src="Figuras/ISMRT.svg" alt="Logo ISMRT" width="180"/>
      </a>
    </td>
    <td width="75%" valign="middle">
      Este workshop y su entorno de laboratorios virtuales cuentan con el <strong>respaldo oficial (Endorsement) de la ISMRT</strong> (<em>International Society for Magnetic Resonance Technicians</em>), ratificado por su Junta Executiva durante la reunión anual en Ciudad del Cabo.<br><br>
      Para conocer más sobre la división y sus directrices internacionales, visite el sitio oficial de la <a href="https://www.ismrm.org/ismrt/" target="_blank" rel="noopener noreferrer"><strong>ISMRT International</strong></a>.
    </td>
  </tr>
</table>

---

## Agradecimientos
Este trabajo fue financiado por el Concurso Endowment I + D en Salud de la Universidad Andrés Bello (UNAB) 2025, proyecto DI-07-25/ICS

---

## Contacto, Soporte e Internacionalización
<table border="0" width="100%">
  <tr>
    <td width="60%" valign="top">
      <h3> Contacto y Soporte Técnico</h3>
      <p>Si tienes dudas académicas, consultas sobre las inscripciones o experimentas problemas técnicos al ejecutar los cuadernos de Google Colab o de forma local, puedes comunicarte a través de los siguientes canales:</p>
      <ul>
        <li><strong>Reportar un problema:</strong> Abre un <a href="https://github.com/pamelaFranco/workshop_glioma/issues" target="_blank" rel="noopener noreferrer">Issue en GitHub</a> detallando el error.</li>
        <li><strong>Consultas Generales:</strong> Escríbenos directamente a <a href="mailto:neurooncologia.ia@gmail.com">neurooncologia.ia@gmail.com</a>.</li>
        <li><strong>Comunidad:</strong> Síguenos y envíanos un mensaje en nuestro Instagram oficial <a href="https://www.instagram.com/neuro_artint/" target="_blank" rel="noopener noreferrer">@neuro_artint</a>.</li>
      </ul>
    </td>
    <td width="40%" valign="top" style="border-left: 1px solid #ccc; padding-left: 20px;">
      <h3> Language / Idioma</h3>
      <p><em>The materials, documentation, and interactive notebooks in this repository are written in <strong>Spanish</strong> to support the local Latin American neuro-oncology and medical physics community.</em></p>
      <p> <strong>Non-Spanish speakers:</strong> You can easily run and translate the Google Colab notebooks using standard browser translation extensions. The underlying Python code and medical imaging libraries (PyRadiomics, NiLearn, DIPY) follow international standards.</p>
    </td>
  </tr>
</table>

---

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)