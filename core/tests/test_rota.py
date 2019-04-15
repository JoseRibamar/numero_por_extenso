from django.test import TestCase


class TestRoute(TestCase):

    def test_route_with_positive_number(self):
        """
            rota com numero positivo existe
        """
        response = self.client.get('/5/')
        assert response.status_code is 200

    def test_route_with_negative_number(self):
        """
            rota com numero negativo existe
        """
        response = self.client.get('/-10/')
        assert response.status_code is 200

    def test_route_without_params(self):
        """
            rota sem parametros nao existe
        """
        response = self.client.get('/')
        assert response.status_code == 404

    def test_route_with_unknown_params(self):
        """
            rota com letras nao existe
        """
        response = self.client.get('/xyz')
        assert response.status_code == 404

    def test_route_with_invalid_interval(self):
        """
            rota com numeros fora dos limites permitidos [-99999, 99999]
        """
        response = self.client.get('/9000999/')
        response.content == b'{"mensagem": "informe um numero na URL de -99999 a 99999."}'
        assert response.status_code is 400

    def test_route_with_invalid_interval(self):
        """
            rota com numeros fora dos limites permitidos [-99999, 99999]
        """
        response = self.client.get('/90000/')
        response.content == b'{"extenso": "noventa mil"}'
        assert response.status_code is 200

