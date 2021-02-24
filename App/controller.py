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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(tipoLista):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipoLista)
    return catalog
    
# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadCategory(catalog)
    loadVideos(catalog)
    

def loadVideos(catalog):
    """
    Carga los videos del archivo.
    """
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategory(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    categoryfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory(catalog, category)

# Funciones de ordenamiento


def sortVideos(catalog, size, tipo):
    """
    Ordena los videos por numero de views
    """
    model.sortVideos(catalog, size, tipo)

# Funciones de consulta sobre el catálogo

def getTrendingVideos(catalog, category_name, country, n):
    """
    Retorna los videos trending
    """
    trending = model.TrendingVideos(catalog, category_name, country, n)
    return trending

def getVideosByCategory(catalog, category_name):
    """
    Retorna los videos de una categoría
    """
    category = model.VideosByCategory(catalog, category_name)
    return category

def getVideosByCountry(catalog, countryname):
    """
    Retorna los videos de un país
    """
    country = model.getVideosByCountry(catalog, countryname)
    return country


def getVideosByLikes(catalog, n, countryname, tag):
    """
    Retorna los videos con más likes
    """
    likes = model.getVideosByLikes(catalog, n, countryname, tag)
    return likes

