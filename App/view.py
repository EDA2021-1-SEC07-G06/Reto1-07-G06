"""
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
catalog = None

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar los videos por wiews")
    print("3- Consultar videos tendencia por categoría y país ")
    print("4- Consultar video tendencia por país")
    print("5- Consultar video tendencia por categoría")
    print("6- Videos con más likes")
    print("0- Salir")


def initCatalog(tipoLista):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(tipoLista)

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def printCountryData(video, dias, countryname):
    if video:
        print('Video encontrado: ' + video['video'])
        print('Canal: ' + video['canal'])
        print('País: ' + countryname)
        print('Número de días:' + str(dias))
        
    else:
        print('No se encontro video')


def printCategoryData(video):
    
    vide = video[0]
    dias = video[1]
    
    if video:
        print('Video encontrado: ' + vide['title'])
        print('Canal: ' + vide['channel_title'])
        print('Categoria-id: ' + vide['category_id'])
        print('Publi: ' + vide['publish_time'])
        print('Trend: ' + vide['trending_date'])
        print('Número de días: ' + str(dias))
        
    else:
        print('No se encontro video')


def printTrendingVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos: ')
        for video in lt.iterator(videos):
            print( 'Fecha de tendencia: ' + video['trending_date'] + 
                   ' Titulo: ' + video['title'] + '  Canal: ' + video['channel_title'] +
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


def printDatosCargados(intLista):
    resultado = 'Opción invalida. '
    array = 'ARRAY_LIST'
    link = 'LINKED_LIST'
    global catalog
    if int(intLista == 1):
        catalog = initCatalog(array)
        loadData(catalog)
        resultado = ('Videos cargados: ' + str(lt.size(catalog['videos'])))
    elif int(intLista == 2):
        catalog = initCatalog(link)
        loadData(catalog)
        resultado = ('Videos cargados: ' + str(lt.size(catalog['videos'])))

    return resultado

def printTipoOrd(tipo):
    ordenamiento = ''
    if int(tipo == 1):
        ordenamiento = 'selection'
        print("Ha seleccionado Selection Sort.")
    elif int(tipo == 2):
        ordenamiento = 'insertion'
        print("Ha seleccionado Insertion Sort.")
    elif int(tipo == 3):
        ordenamiento = 'shell'
        print("Ha seleccionado Shell Sort.")
    elif int(tipo == 4):
        ordenamiento = 'merge'
        print("Ha seleccionado Merge Sort.")
    elif int(tipo == 5):
        ordenamiento = 'quick'
        print("Ha seleccionado Quick Sort.")
        
    return ordenamiento




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
        resultado = printDatosCargados(int(lista))
        print(resultado)

    elif int(inputs[0]) == 2:
        print("1- Selection sort")
        print("2- Insertion sort")
        print("3- Shell sort")
        print("4- Merge sort")
        print("5- Quick sort")

        lista = input("Ingrese el tipo de ordenamiento que desee: ")
        ordenamiento = printTipoOrd(int(lista))
        size = input("Indique tamaño de la muestra: ")
        result = controller.sortVideos(catalog, int(size), ordenamiento)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        
    elif int(inputs[0]) == 3:
        country = input("Ingrese el país a consultar: ")
        category_name = input("Ingrese la categoría a consultar: ")
        n = input("Ingrese el número de videos que quiere listar: ")
        video = controller.getTrendingVideos(catalog, category_name, country, n)
        printTrendingVideos(video)

    elif int(inputs[0]) == 4:
        countryname = input("Nombre del país: ")
        country = controller.getVideosByCountry(catalog, countryname)
        if country == None:
            print("No se encontraron videos")
        else:
            printCountryData(country[0], country[1], countryname)
            
    elif int(inputs[0]) == 5:
        category_name = input("Ingrese la categoría: ")
        category = controller.getVideosByCategory(catalog, category_name)
        printCategoryData(category)

    elif int(inputs[0]) == 6:
        tag = input("Ingrese el tag a consultar: ")
        countryname = input("Nombre del país: ")
        n = input("Ingrese el número de videos que quiere listar")
        mas_likes = controller.getVideosByLikes(catalog, n, countryname, tag)
        printTagData(video)

    else:
        sys.exit(0)
sys.exit(0)
