﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar tipo de ordenamiento")
    print("3- Consultar videos tendencia por categoría y país ")
    print("4- Consultar video tendencia por país")
    print("5- Ordenar los videos por wiews")
    print("6- Consultar video tendencia por categoría")
    print("7- Videos con más likes")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def printCountryData(video):
    if video:
        print('Video encontrado: ' + video['title'])
        print('Canal: ' + video['cannel_title'])
        print('País: ' + video['country'])
        print('Número de días: ' + video['dias'])
        
    else:
        print('No se encontro video')


def printCategoryData(video):
    if video:
        print('Video encontrado: ' + video['title'])
        print('Canal: ' + video['cannel_title'])
        print('Categoria-id: ' + video['category_id'])
        print('Número de días: ' + video['dias'])
        
    else:
        print('No se encontro video')


def printTrendingVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos: ')
        for video in lt.iterator(videos):
            print( 'Fecha de tendencia: ' + video['trending_date'] + 
                   ' Titulo: ' + video['title'] + '  Canal: ' + video['cannel_title'] +
                   ' Tiempo de publicación: ' + video['publish_time'] +
                   ' Vistas: ' +video['views'] + ' Likes: ' +video['likes'] + 
                   ' Dislikes: ' + video['dislikes'])
    else:
        print('No se encontraron videos')


def printTagData(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos: ')
        for video in lt.iterator(videos):
            print( 'Fecha de tendencia: ' + video['trending_date'] + 
                   ' Titulo: ' + video['title'] + '  Canal: ' + video['cannel_title'] +
                   ' Tiempo de publicación: ' + video['publish_time'] +
                   ' Vistas: ' +video['views'] + ' Likes: ' +video['likes'] + 
                   ' Dislikes: ' + video['dislikes'] + ' Tags: ' + video['tags'])
    else:
        print('No se encontraron videos')

#catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("1- ArrayList")
        print("2- LinkedList")
        lista = input("Seleccione el tipo de Lista\n")
        if int(lista[0] == 1):
            catalog = initCatalog('ARRAY_LIST')
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['title'])))
        elif int(lista[0] == 2):
            catalog = initCatalog('LINKED_LIST')
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['title'])))
        else: 
            sys.exit(0)

    elif int(inputs[0]) == 2:
        country = input("Ingrese el tipo de ofrdenamiento que desee: ")
        ordenamiento = ''
        print("1- Selection sort")
        print("2- Insertion sort")
        print("2- Shell sort")
        if int(lista[0] == 1):
            ordenamiento = 'selection'
        elif int(lista[0] == 2):
            ordenamiento = 'insertion'
        elif int(lista[0] == 3):
            ordenamiento = 'shell'
        else: 
            sys.exit(0)

    elif int(inputs[0]) == 3:
        country = input("Ingrese el país a consultar")
        category_name = input("Ingrese la categoría a consultar")
        n = input("Ingrese el número de videos que quiere listar")
        video = controller.getTrendingVideos(catalog, category_name, country, n)
        printTrendingVideos(video)

    elif int(inputs[0]) == 4:
        countryname = input("Nombre del país: ")
        country = controller.getVideosByCountry(catalog, countryname)
        printCountryData(video)

    elif int(inputs[0]) == 5:
        if ordenamiento != '':
            size = input("Indique tamaño de la muestra: ")
            result = controller.sortVideos(catalog, int(size), ordenamiento)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result))
        else:
            print("Porfavor elija el tipo de ordenamiento")
            sys.exit(0)
           
    elif int(inputs[0]) == 6:
        category_name = input("Ingrese la categoría: ")
        category = controller.getVideosByCategory(catalog, category_name)
        printCategoryData(video)

    elif int(inputs[0]) == 7:
        tag = input("Ingrese el tag a consultar: ")
        countryname = input("Nombre del país: ")
        n = input("Ingrese el número de videos que quiere listar")
        mas_likes = controller.getVideosByLikes(catalog, n, countryname, tag)
        printTagData(video)

    else:
        sys.exit(0)
sys.exit(0)
