# PythonAnalysisProject

Concernant l'API, voici les actions disponibles :

POST 

curl -X POST \
  http://0.0.0.0:8000/prediction/individus/ \
  -H 'Content-Type: application/json' \
  -d '{
	"ChestACCX":1.022898,
    "ChestACCY" :1.022515,
    "ChestACCZ" :1.022853,
    "ChestECG" : 0.071857,
    "ChestResp" : -3.235465,
    "WristACCX" : -0.349609,
    "WristACCY" : 0.763672,
    "WristACCZ" : 0.111328,
    "WristBVP" :-48.900625,
    "Weight" : 78,
    "Gender" : 1,
    "Age" : 37,
    "Height" : 182,
    "Sport" : 6,
    "activity":null
}'

GET

curl -X GET \
  http://0.0.0.0:8000/prediction/individus/1/ \
  
DELETE 
 
 curl -X DELETE \
  http://0.0.0.0:8000/prediction/individus/1/ \

Mes modèles sont disponibles dans le dossier ipynb
