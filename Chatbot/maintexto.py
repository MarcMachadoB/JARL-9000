import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from langdetect import detect
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Cargar manualmente los tokenizadores punkt para cada idioma compatible
for lang in ['english']:
    try:
        nltk.data.find(f'tokenizers/punkt/{lang}.pickle')
    except LookupError:
        nltk.download(f'punkt_{lang}')

# Función para preprocesar el texto
def preprocesar_texto(texto):
    idioma = 'english'  # Especificamos manualmente el idioma como inglés
    tokens = word_tokenize(texto, language=idioma)
    stop_words = set(stopwords.words(idioma))
    tokens = [word for word in tokens if word.lower() not in stop_words and len(word) > 1]
    stemmer = SnowballStemmer(idioma)
    tokens = [stemmer.stem(word) for word in tokens]
    texto_preprocesado = ' '.join(tokens)
    return texto_preprocesado

# Función para cargar el modelo clasificador y las respuestas asociadas
def cargar_modelo_y_respuestas(ruta_modelo):
    with open(ruta_modelo, 'rb') as f:
        clasificador, vectorizador, respuestas = pickle.load(f)
    return clasificador, vectorizador, respuestas

# Función para clasificar una pregunta y obtener la respuesta asociada
def clasificar_pregunta(pregunta, clasificador, vectorizador, respuestas):
    pregunta_preprocesada = preprocesar_texto(pregunta)
    pregunta_vectorizada = vectorizador.transform([pregunta_preprocesada])
    categoria_predicha = clasificador.predict(pregunta_vectorizada)[0]
    
    # Verificar si categoria_predicha es numérica
    if categoria_predicha.isdigit():
        categoria_predicha = int(categoria_predicha)
        respuesta_asociada = respuestas[categoria_predicha]
    else:
        respuesta_asociada = "No se pudo determinar una respuesta."
    
    return respuesta_asociada


def main():
    # Ruta del archivo del modelo clasificador
    ruta_modelo = "/media/alumne/HPV212W/CEIABD/M2/Chatbot/clasificador_textos.pkl"

    # Cargar el modelo clasificador y las respuestas asociadas
    clasificador, vectorizador, respuestas = cargar_modelo_y_respuestas(ruta_modelo)

    # Solicitar al usuario que ingrese una pregunta
    pregunta = input("Ingrese una pregunta: ")

    # Clasificar la pregunta ingresada por el usuario y obtener la respuesta asociada
    respuesta = clasificar_pregunta(pregunta, clasificador, vectorizador, respuestas)

    print("Respuesta:", respuesta)

if __name__ == "__main__":
    main()