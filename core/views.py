from django.http import JsonResponse
from .numero_por_extenso import NumeroPorExtenso


def numero_por_extenso_view(request, number):
    numero_por_extenso = NumeroPorExtenso()

    if numero_por_extenso.intervalo_valido(number):
        return JsonResponse({"extenso": numero_por_extenso.get(number)})

    mensagem_intervalo_invalido = "Enter a number in the URL of -99999 a 99999."
    return JsonResponse({"message": mensagem_intervalo_invalido}, status=400)
