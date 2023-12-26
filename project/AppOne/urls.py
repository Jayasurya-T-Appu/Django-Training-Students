from django.urls import path
from . import views
urlpatterns = [
    path('', views.createImage, name='image' ),
    path('form/', views.formView, name = 'formView'),
    path('relation/', views.relation, name='relation')
]