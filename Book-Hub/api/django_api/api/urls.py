from django.urls import path
from .views import *


urlpatterns = [
    path('createbook/',BookCreate.as_view(),name="createbook"),
    path('updatebook/<int:pk>/',BookUpdate.as_view(),name="updatebook"),
    path('deletebook/<int:pk>/',BookDelete.as_view(),name="deletebook"),
    path('detailsbook/<int:pk>/',BookDetails.as_view(),name="detailsbook"),
    path('searchbook/<str:title>/',BookSearch.as_view(),name="searchbook"),

    path('createuser/',UserCreate.as_view(),name="createUser"),
    path('updateuser/<int:pk>/',UserUpdate.as_view(),name="updateuser"),
    path('deleteuser/<int:pk>/',UserDelete.as_view(),name="deleteuser"),
    path('detailsuser/<int:pk>/',UserDetails.as_view(),name="detailsuser"),
    path('searchuser/<str:name>/',UserSearch.as_view(),name="searchuser"),
    
]