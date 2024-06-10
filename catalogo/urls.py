from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('MotoryTransmisión/', views.categoria1, name='categoria1'),
    path('Frenos/', views.categoria2, name='categoria2'),
    path('Suspensión/', views.categoria3, name='categoria3'),
    path('Aceites/', views.categoria4, name='categoria4'),
    path('Neumáticos/', views.categoria5, name='categoria5'),
    path('Iluminación/', views.categoria6, name='categoria6'),
    path('Otros/', views.otros, name = 'otros'),
    path('Nosotros', views.aboutus, name = 'nosotros'),
    path('busqueda', views.busquedaavanzada, name = 'busquedav')
]