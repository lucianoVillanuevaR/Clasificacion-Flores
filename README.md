# Clasificación de Flores

## Descripción del proyecto

Este proyecto corresponde a un sistema de clasificación de flores mediante imágenes, desarrollado para la asignatura de Taller de Introducción a Visión por Computadora.

El objetivo principal es preparar y analizar un dataset de imágenes de flores para posteriormente entrenar un modelo de clasificación capaz de identificar automáticamente tres tipos de flores:

- Girasol
- Rosa
- Tulipán

En este avance todavía no se realiza el entrenamiento final del modelo. La etapa actual se enfoca en organizar, revisar y analizar el dataset de imágenes.

---

## Integrantes

- Luciano Villanueva Ramírez
- Mauricio Pérez
- Francisco Flores Cares

---

## Estado del proyecto

Este repositorio corresponde al **Avance 2** del proyecto.

En esta etapa se realizó:

- Organización del dataset de imágenes.
- Separación del dataset en entrenamiento, validación y prueba.
- Revisión de las clases disponibles.
- Conteo de imágenes por clase.
- Generación de un archivo CSV con el resumen del dataset.
- Generación de gráficos para visualizar la distribución y ejemplos del dataset.

---

## Cambio de enfoque del proyecto

Inicialmente se consideró el dataset Iris como referencia clásica para clasificación de flores. Sin embargo, para orientar el proyecto directamente a Visión por Computador, se decidió trabajar con un dataset de imágenes gestionado en Roboflow.

De esta manera, el proyecto deja de clasificar flores mediante datos numéricos y pasa a clasificar flores a partir de imágenes reales.

---

## Dataset utilizado

El dataset fue gestionado mediante **Roboflow** y contiene imágenes de flores organizadas en tres divisiones:

- `train`: imágenes para entrenamiento.
- `valid`: imágenes para validación.
- `test`: imágenes para prueba.

### Clases del dataset

| Clase | Descripción |
|---|---|
| Girasol | Imágenes de girasoles |
| Rosa | Imágenes de rosas |
| Tulipán | Imágenes de tulipanes |

---

## Distribución del dataset

### Cantidad por división

| División | Cantidad de imágenes |
|---|---:|
| Train | 86 |
| Valid | 26 |
| Test | 13 |
| **Total** | **125** |

### Cantidad por clase

| Clase | Cantidad de imágenes |
|---|---:|
| Girasol | 41 |
| Rosa | 41 |
| Tulipán | 43 |

El dataset se encuentra relativamente balanceado, ya que las tres clases poseen una cantidad similar de imágenes.

---

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Pillow
- Roboflow
- Git / GitHub

---

git clone https://github.com/lucianoVillanuevaR/Clasificacion-Flores.git

cd Clasificacion-Flores

python3 -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python3 main.py
