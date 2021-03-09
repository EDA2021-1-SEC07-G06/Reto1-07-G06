﻿"""
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
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
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
    catalog['videos'] = lt.newList(tipoLista, cmpfunction= cmpVideosByTitle)
    catalog['category'] = lt.newList(cmpfunction = cmpByIdCategory)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):

    # Se adiciona el video a la lista de videos

    lt.addLast(catalog['videos'], video)

    # Se obtiene la categoria del libro 

    categoriaid = int(video['category_id'])

    # Cada categoria, se crea en la lista de videos del catalogo, y se

    # crea un video en la lista de dicha categoria (apuntador al video)
    
    

    addVideosCategoria(catalog, categoriaid, video)
    

def addVideosCategoria(catalog, identificador, video):
    """
    Adiciona un categoria a lista de categorias
    """

    categorys = catalog['category']
    categoryTosearch = newCategory(identificador, '')
    posCategory = lt.isPresent(categorys, categoryTosearch)
    if posCategory > 0:
        categ = lt.getElement(categorys, posCategory)
    else: 
        categ = newCategory(identificador, 'desconocida')
        lt.addLast(categorys, categ)
    lt.addLast(categ['videos'], video)

def addCategory(catalog, category):
    t = newCategory(int(category['id']), category['name'])
    lt.addLast(catalog['category'], t)

def newCategory(id, name):
    """
    Crea una nueva estructura para modelar los videos de
    una categoria, su nombre e id.
    """
    categorys = {'id': id, 'name': name.strip(), 'videos': None }
    categorys['videos'] = lt.newList('ARRAY_LIST',cmpfunction=cmpVideosByTitle)
    return categorys

# Funciones para creacion de datos

def newVideoViews(name):
    """
    Crea una nueva estructura para modelar los videos de
    un país y su total de views
    """
    pais = {'country': "", "video": None,  "total_views": 0}
    pais['country'] = name
    pais['video'] = lt.newList('ARRAY_LIST')
    return pais

# Funciones de consulta

def getTrendingVideos(catalog, category_name, country, n):
    pass

def getVideosByCategory (catalog, category_name):
    pass

def getVideosByCountry (catalog, countryname):
    lista_videos_pais = []
    dict = {}
    for video in catalog:
        if video["country"] == countryname:
            dict["video"] = video["title"]
            dict["canal"] = video["cannel_title"]
            lista_videos_pais.append(dict)
            

    pos = 0
    mas_trending = ""
    dias_trending = 0
    for elem in lista_videos_pais:
        if lista_videos_pais[elem].count(lista_videos_pais[elem]["video"]) > dias_trending:
            dias_trending = lista_videos_pais.count(lista_videos_pais[elem]["video"])
            mas_trending = elem
        pos += 1
    
 return (mas_trending, dias_trending)

def getVideosByLikes(catalog, n, countryname, tag):
    pass

# Funciones utilizadas para comparar elementos dentro de una lista
   
def cmpVideosByViews(video1, video2):
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: video1: informacion del primer video que incluye su valor 'views'
          video2: informacion del segundo video que incluye su valor 'views' """
    return (float(video1['views']) < float(video2['views']))

def cmpVideosByTitle(video1, video2):
    
    title1 = video1['title']
    title2 = video2['title']
    if title1 == title2:
        return 0
    elif title1 < title2:
        return -1
    else:
        return 1
    
def cmpByIdCategory(cat1,cat2):

    idCat1 = cat1['id'] 
    idCat2 = cat2['id'] 
    if idCat1 == idCat2:
        return 0
    elif idCat1 < idCat2:
        return -1
    else:
        return 1


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
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    
    elif tipo == 'shell':
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    elif tipo == 'quick':
        start_time = time.process_time()
        sorted_list = qs.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
    elif tipo == 'merge':
        start_time = time.process_time()
        sorted_list = ms.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

        

