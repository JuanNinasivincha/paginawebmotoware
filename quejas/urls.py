from django.urls import path
from .views import quejas


urlpatterns = [
     path('queja/', quejas, name='vistaquejas')
]
