import csv
import os

def separar_noticias(archivo_csv):
    """
    Separa las noticias por categoría en un archivo CSV.

    Args:
        archivo_csv (str): Ruta al archivo CSV.

    Returns:
        None
    """

    with open(archivo_csv, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None)  
        noticias = list(reader)

    categorias = {}
    for noticia in noticias:
        categoria = noticia[1]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(noticia[2])

    for categoria in categorias:
        os.makedirs(categoria, exist_ok=True)

    for categoria, urls in categorias.items():
        with open(os.path.join(categoria, "/media/alumne/HPV212W/CEIABD/M2/Extract_Clasificador/Clasificador_Texto/urls.txt"), "w") as outfile:
            outfile.write("\n".join(urls))

if __name__ == "__main__":
    archivo_csv = "/media/alumne/HPV212W/CEIABD/M2/Extract_Clasificador/Clasificador_Texto/train.csv"
    separar_noticias(archivo_csv)