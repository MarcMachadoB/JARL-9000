import os
import pickle
import pandas as pd
import glob
import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

# Descargar recursos de NLTK
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Definir las categorías de clasificación
CATEGORIAS = ['Contacto', 'Explicaciones', 'Fechas', 'Listas']

# Función para cargar los datos desde archivos CSV en diferentes idiomas y categorías
def cargar_datos(directorio_principal):
    textos = []
    etiquetas = []
    respuestas = []  # Lista para almacenar las respuestas asociadas
    for idioma in os.listdir(directorio_principal):
        idioma_path = os.path.join(directorio_principal, idioma)
        if os.path.isdir(idioma_path):
            print(f"Directorio de idioma encontrado: {idioma}")
            for archivo_csv in glob.glob(os.path.join(idioma_path, '*.csv')):
                categoria = os.path.splitext(os.path.basename(archivo_csv))[0]
                print(f"Cargando datos de {archivo_csv}")
                with open(archivo_csv, 'r', encoding='utf-8') as file:
                    df = pd.read_csv(file, encoding='utf-8')  # Añadir el parámetro encoding
                    print(f"Columnas en el archivo CSV: {df.columns}")
                    print(f"Filas en el archivo CSV: {len(df)}")
                    for index, row in df.iterrows():
                        pregunta = str(row["Pregunta"]).strip()
                        respuesta = str(row["Respuesta"]).strip()
                        if pregunta and respuesta:
                            print(f"Pregunta: {pregunta}")
                            print(f"Respuesta: {respuesta}")
                            textos.append(pregunta)  # Agregar la pregunta al texto
                            respuestas.append(respuesta)  # Agregar la respuesta
                            etiquetas.append(categoria)
    print(f"Total de textos cargados: {len(textos)}")
    return textos, respuestas, etiquetas  # Devolver también las respuestas

# Función para preprocesar el texto según el idioma
def preprocesar_texto(texto, idioma):
    # Tokenización
    tokens = word_tokenize(texto, language=idioma)
    # Eliminación de stopwords
    stop_words = set(stopwords.words(idioma))
    tokens = [word for word in tokens if word.lower() not in stop_words and len(word) > 1]  # Agregar condición de longitud
    # Stemming (derivación)
    stemmer = SnowballStemmer(idioma)
    tokens = [stemmer.stem(word) for word in tokens]
    # Reconstruir el texto preprocesado
    texto_preprocesado = ' '.join(tokens)
    return texto_preprocesado

# Función para entrenar el clasificador y guardar el modelo
def entrenar_clasificador(directorio_principal, archivo_salida):
    textos, respuestas, etiquetas = cargar_datos(directorio_principal)

    # Vectorizar los textos
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)

    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, etiquetas, test_size=0.2, train_size=0.8, random_state=42)

    # Crear el modelo de clasificación
    text_clf = MLPClassifier(hidden_layer_sizes=(20, 20, 20, 20, 20), max_iter=250, random_state=42)

    # Entrenar el modelo
    text_clf.fit(X_train, y_train)

    # Guardar el clasificador en un archivo .pkl
    with open(archivo_salida, 'wb') as f:
        pickle.dump((text_clf, vectorizer, respuestas), f)  # Guardar también las respuestas

    # Calcular la matriz de confusión
    y_pred = text_clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    # Plotear la matriz de confusión como un mapa de calor
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Matriz de Confusión')
    plt.colorbar()
    tick_marks = np.arange(len(CATEGORIAS))
    plt.xticks(tick_marks, CATEGORIAS, rotation=45)
    plt.yticks(tick_marks, CATEGORIAS)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('Etiqueta Verdadera')
    plt.xlabel('Etiqueta Predicha')
    plt.tight_layout()
    plt.show()

    return text_clf

# Función principal
def main():
    directorio_principal = "/media/alumne/HPV212W/CEIABD/M2/Chatbot/Preguntas_Frecuentes"  # Actualiza con la ruta correcta
    archivo_clasificador = "/media/alumne/HPV212W/CEIABD/M2/Chatbot/clasificador_textos.pkl"

    print("Entrenando el clasificador...")
    clasificador = entrenar_clasificador(directorio_principal, archivo_clasificador)
    print("El clasificador ha sido entrenado y guardado correctamente.")

if __name__ == "__main__":
    main()