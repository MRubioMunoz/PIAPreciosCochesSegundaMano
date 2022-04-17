from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import Formulario
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from joblib import load
import numpy as np
from tensorflow import keras

from keras.models import load_model 

import boto3

all_features = ['fuelTypeId', 'km', 'makeId', 'modelId','transmissionTypeId', 'year', 'cubicCapacity', 'doors', 'hp']


def formulario(response):
    if response.method == "POST":
        formulario = Formulario(response.POST)
        if formulario.is_valid:
            return HttpResponseRedirect(reverse('main:precio'))

    else:
        formulario = Formulario()
    return render(response,"main/formulario.html", {"form": formulario})

def precio(response):
    km = int(response.POST.get('km'))
    fuelTypeId = int(response.POST.get('fuelTypeId'))
    makeId = int(response.POST.get('makeId'))
    modelId = int(response.POST.get('modelId'))
    transmissionTypeId = int(response.POST.get('transmissionTypeId'))
    year = int(response.POST.get('year'))
    cubicCapacity =  int(response.POST.get('cubicCapacity'))
    door = int(response.POST.get('door'))
    hp = int(response.POST.get('hp'))

    array = np.array([[fuelTypeId,km,makeId,modelId,transmissionTypeId, year, cubicCapacity, door,hp]])

    knn_model = load('main/joblist/knn.joblib')
    linearRegresion = load('main/joblist/LinearRegression.joblib')
    randomForest = load('main/joblist/RandomForest.joblib')
    decisionTree = load('main/joblist/DecissionTree.joblib')
    keras = load_model('main/joblist/keras.h5')

    precioKnn = knn_model.predict(array)
    precioLN = linearRegresion.predict(array)
    precioRF = randomForest.predict(array)
    precioDT = decisionTree.predict(array)
    precioKeras = keras.predict(array)


    return render(response,"main/precio.html",
     {"precio1": precioKnn[0], "precio2": precioLN[0], "precio3": precioDT[0], "precio4": precioRF[0], "precio5": precioKeras[0]})
