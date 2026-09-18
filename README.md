# JARL-9000

Este proyecto consiste en un chatbot desarrollado en Python para responder preguntas frecuentes sobre un centro educativo. Su objetivo es clasificar las consultas de los usuarios y devolver la respuesta más adecuada a partir de un conjunto de preguntas y respuestas predefinidas.

## ¿De qué trata?

El sistema trabaja con un modelo de clasificación de texto que analiza la pregunta introducida por el usuario y la compara con un conjunto de datos de preguntas frecuentes. Estas preguntas se organizan por categoría, como:

- Contacto
- Explicaciones
- Fechas
- Listas

El chatbot está preparado para manejar información de varios idiomas y devuelve la respuesta asociada a la categoría detectada.

## Estructura del proyecto

- `Chatbot/guardatext2.py`: script para entrenar el modelo de clasificación.
- `Chatbot/maintexto.py`: script principal para interactuar con el chatbot.
- `Chatbot/Preguntas_Frecuentes/`: contiene las preguntas frecuentes en distintos idiomas y categorías en formato CSV.

## Tecnologías utilizadas

- Python
- scikit-learn
- NLTK
- pandas
- pickle

## Uso

1. Preparar los datos de preguntas y respuestas en los CSV correspondientes.
2. Ejecutar el entrenamiento del clasificador.
3. Lanzar el chatbot para introducir preguntas y obtener respuestas.

Este proyecto sirve como base para un asistente de atención al alumnado o consulta institucional basado en preguntas frecuentes.

## Enlace a la máquina virtual (Ubuntu)
https://drive.google.com/file/d/1dRHUhdlaJQ5AcDLDKLV-3G0lVRrqRM_8/view?usp=drive_link
