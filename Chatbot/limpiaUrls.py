import os
import re

CATEGORIAS = ['Medicina', 'Economia', 'Motor', 'Deportes', 'Religion', 'Guerra', 'Politico', 'Ocio', 'Moda', 'Informática', 'Astronomia', 'Alimentación']

def clasificar_urls(ruta_directorio, ruta_salida):
  """
  Clasifica las URLs de un directorio y sus subdirectorios en diferentes archivos .txt según la categoría.
  """
  categorias = {}
  for ruta, subcarpetas, archivos in os.walk(ruta_directorio):
    for archivo in archivos:
      if archivo.endswith('.txt'):
        with open(os.path.join(ruta, archivo), 'r') as f:
          urls = f.readlines()
        for url in urls:
          categoria = obtener_categoria(url)
          if categoria not in categorias:
            categorias[categoria] = []
          categorias[categoria].append(url)

  for categoria in CATEGORIAS:
    if categoria not in categorias:
      categorias[categoria] = []

  for categoria, urls in categorias.items():
    with open(os.path.join(ruta_salida, f'{categoria}.txt'), 'w') as f:
      for url in urls:
        f.write(url + '\n')

def obtener_categoria(url):
  """
  Extrae la categoría de una URL.
  """
  CATEGORIAS_REGEX = {
    'Medicina': r'(medicina|salud|hospital|virus|infecciones|artritis|enfermedades|enfermedad|diabetes)',
    'Economia': r'(economia|dinero|negocios|finanzas|consumo|precio|empresa|deuda|economico|comisiones|inversion)',
    'Motor': r'(motor|coches|automoviles|conduccion)',
    'Deportes': r'(deportes|futbol|baloncesto|tenis)',
    'Religion': r'(religion|dios|iglesia|creer|francisco|papa|cristianismo|islam|musulman)',
    'Guerra': r'(guerra|kiev|conflicto|iraqui|iran|armas|soldados|rusia|ucraina|hamas|ruso|rusa|ucraniano|ucraniana|siria|sirios|armenios|armenia|israel|gaza|islam|armada|putin|holocausto|yihadista)',
    'Politico': r'(politico|global|feminista|feminista|machismo|machista|chavismo|climatico|planeta|bruselas|estado|cambio|sociales|ue|calvino|autoritarismo|erdogan|elecciones|feijoo|sanchez|ley|comunismo|trump|tribunal|europa|europeos|estoicismo|machismo|femenismo|politica|gobierno|presidente|leyes|catalunya|espana|activistas|naufrago|mundo|huelga|raza|ultraderecha|pp|psoe|junts|esquerra|vox|castas|republica|democracia|derecha|izquierda)',
    'Ocio': r'(ocio|conciertos|concierto|musicales|teatro|tiempo\slibre|vacaciones|peliculas|tv|tele|cine|hollywood|pop|rock|banda|museo|literatura|dylan|spotify|jagger|podcast|comic|musica)',
    'Moda': r'(moda|ropa|estilo|tendencias|mujer|hombre|gente|pelo|belleza|socialite|famosos|arte|barbaros|anticelulitico)',
    'Informática': r'(informatica|artificial|inteligencia|portatiles|computadoras|ordenadores|software|tecnologia|app|virtual|juegos|nintendo|playstation|inteligencia artificial|tablet|windows|apple|movil|moviles|pc|CPU|gaming|monitores)',
    'Astronomia': r'(estrellas|planetas|espacio|luna|telescopio|planeta|estrella|agujero negro|asteroide|asterioides|espacial|nasa|astronauta)',
    'Alimentación': r'(alimentacion|cocinar|alimentaria|apetito|edulcorantes|chocolate|cafe|bebidas|ayuno|alcohol|comida|recetas|chef|gastronomia|vaso|alimento|leche|dieta|nutricion|ecologico|hambre|gluten|celiaco|hambre|proteinas|uva|pescado|carne|pasta|pan|vegetales)' 
  }

  for categoria, regex in CATEGORIAS_REGEX.items():
    if re.search(regex, url):
      return categoria
  return 'Sin categoría'

# Ejemplo de uso
ruta_directorio = 'C:/Users/XAVIER/Documents/Clasificador_Texto/Clasificador_Texto'
ruta_salida = 'C:/Users/XAVIER/Documents/Clasificador_Texto/urls'

clasificar_urls(ruta_directorio, ruta_salida)

print('Las URLs se han clasificado correctamente.')
