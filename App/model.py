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
from DISClib.Algorithms.Sorting import selectionsort as ss
<<<<<<< HEAD
from DISClib.Algorithms.Sorting import insertionsort as ins
=======
from DISClib.Algorithms.Sorting import insertionsort as inss
>>>>>>> 3d408957b9d0d986eb94ee1e3d4fe32b7d06c25b
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipoLista):

    """

    Inicializa el catálogo de videos.  Retorna el catalogo inicializado.

    """
    catalog = {'videos': None, 'category': None,}
    catalog['videos'] = lt.newList(tipoLista, cmpfunction= cmpVideosByViews)
    catalog['category'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):

    # Se adiciona el video a la lista de videos

    lt.addLast(catalog['videos'], video)

    # Se obtiene la categoria del libro 

    ident = video['category_id'].split(",")

    # Cada categoria, se crea en la lista de videos del catalogo, y se

    # crea un video en la lista de dicha categoria (apuntador al video)
    
    for iden in ident:

        addVideosCategoria(catalog, iden.strip(), video)

def addVideosCategoria(catalog, identificador, video):
    """
    Adiciona un categoria a lista de categorias
    """

    categorys = catalog['category']
    posCategory = lt.isPresent(categorys, identificador)
    if posCategory != 0:
        categ = lt.getElement(categorys, posCategory)
    else: 
        categ = newCategory(identificador, '')
        lt.addLast(categorys, categ)
    lt.addLast(categ['videos'], video)

def addCategory(catalog, category):
    t = newCategory(category['id'], category['name'])
    lt.addLast(catalog['category'], t)

def newCategory(id, name):
    """
    Crea una nueva estructura para modelar los videos de
    una categoria, su nombre e id.
    """
    categorys = {'id': id, 'name': name, 'videos': None }
    categorys['videos'] = lt.newList('ARRAY_LIST')
    return categorys

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
   
def cmpVideosByViews(video1, video2):
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: video1: informacion del primer video que incluye su valor 'views'
          video2: informacion del segundo video que incluye su valor 'views' """
    return (float(video1['views']) < float(video2['views']))
    


# Funciones de ordenamiento
def sortVideos(catalog, size, tipo):
    sub_list = lt.subList(catalog['videos'],0,size)
    sub_list = sub_list.copy()
    if tipo == 'selection':
        start_time = time.process_time()
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    elif tipo == 'insertion' :
        start_time = time.process_time()
<<<<<<< HEAD
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
=======
        sorted_list = inss.sort(sub_list, cmpVideosByViews)
>>>>>>> 3d408957b9d0d986eb94ee1e3d4fe32b7d06c25b
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    
    else :
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

        

