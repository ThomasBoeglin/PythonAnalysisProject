from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Individu
from .serializers import IndividuSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("You are on the main page !")

@csrf_exempt 
def individu_detail(request, individu_id):
    try:
        ind = Individu.objects.get(pk=individu_id)
    except Individu.DoesNotExist:
        return HttpResponse(str(individu_id), status=404)
    if request.method == "GET":
        serializer = IndividuSerializer(ind)
        return JsonResponse(serializer.data)
    elif request.method =="DELETE":
        ind.delete()
        return HttpResponse("Suppression faite ! ", status = 204)


@csrf_exempt 
def i_want_a_list(request):
    if request.method == "POST":
        content = JSONParser().parse(request)
        serializer = IndividuSerializer(data=content)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)
    
    elif request.method=="GET":
        individus = Individu.objects.all()
        serializer = IndividuSerializer(individus, many=True)
        return JsonResponse(serializer.data, safe=False)

def predict_medv(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ["ChestACCX", "ChestACCY", "ChestACCZ", "ChestECG", "ChestResp", "WristACCX",
                        "WristACCY", "WristACCZ", "WristBVP", "Weight", "Gender", "Age",
                        "Height","Sport", "activity"]
    path_to_model   = "./ipynb/modelRF.pickle"
    #path_for_scaler = "./ipynb/scaler.sav"
    #unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    #scaler          = joblib.load(path_for_scaler)
    #donnees_scalees = scaler.transform([unscaled_data])
    medv            = model.predict(unscaled_data)
    return medv

@csrf_exempt
def predict(request):
    """
    Renvoie une house avec la MEDV completee
    (Attend une MEDV innexistante == null)
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = IndividuSerializer(data=data)
        if serializer.is_valid():
            data["activity"]        = predict_medv(data)
            serializer          = IndividuSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)