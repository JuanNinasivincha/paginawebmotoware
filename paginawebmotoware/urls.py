
from django.contrib import admin
from django.urls import path , include
from .views import home  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('nosotros/', include('nosotros.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('servicios/', include('servicios.urls')),
    path('catalogo/', include('contacto.urls')),
    path('quejas/', include('quejas.urls')),

]
