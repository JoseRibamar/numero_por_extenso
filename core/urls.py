from django.urls import path, register_converter
from .converters import NegativeIntConverter
from .views import numero_por_extenso_view


register_converter(NegativeIntConverter, 'negative_int')

urlpatterns = [
    path('<negative_int:number>/', numero_por_extenso_view)
]
