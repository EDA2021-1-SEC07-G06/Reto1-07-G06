"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    """

    Inicializa el catálogo de videos.  Retorna el catalogo inicializado.

    """

    catalog = {'videos': None,

               'category': None,}

 

    catalog['videos'] = lt.newList()

    catalog['category'] = lt.newList('ARRAY_LIST',

                                    cmpfunction=comparecategory )

    catalog['canales'] = lt.newList('ARRAY_LIST',

                                    cmpfunction=comparecanal )

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):

    # Se adiciona el video a la lista de videos

    lt.addLast(catalog['videos'], video)

    # Se obtiene 

    canales = video['channel_title'].split(",")

    # Cada autor, se crea en la lista de libros del catalogo, y se

    # crea un libro en la lista de dicho autor (apuntador al libro)

    for canal in canales:

        addVideoscanal(catalog, canal.strip(), video)

 def addVideoscanal(catalog, canal , video):

    """
    Adiciona un canal a lista de canales, la cual guarda referencias
    a los videos de dicho canal
    """
    canales = catalog['canales']
    poscanal = lt.isPresent(canales, canal)
    if poscanal > 0:
        author = lt.getElement(canales, poscanal)
    else:
        author = newCanal(canal)
        lt.addLast(canales, author)
    lt.addLast(author['canales'], video)

def addCategory(catalog, video):
    """
    Adiciona un categoria a lista de categorias
    """
    t = newcategory(category['idname'])
    lt.addLast(catalog['category'], t)

# Funciones para creacion de datos

# Funciones de consulta

def getTrendingVideos(catalog, category_name, country, n):
    pass

def getVideosByCategory (catalog, category_name):
    pass

def getVideosByCountry (catalog, countryname):
    pass

def getVideosByLikes(catalog, n, countryname, tag):
    pass

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento