from django.urls import path
from .views import login_view, crear_cuenta


urlpatterns = [
     path('login/', login_view, name='login'),
     path('crearcuenta/', crear_cuenta, name='register')
]
