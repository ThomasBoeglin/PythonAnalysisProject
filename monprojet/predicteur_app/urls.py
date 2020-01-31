from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('individus/', views.i_want_a_list, name='list_individu'),
    path('individus/<int:individu_id>/', views.individu_detail, name='detail'),
    path('predict/', views.predict, name='to_predict'),
]