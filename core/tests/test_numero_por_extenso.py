from django.test import TestCase
from core.numero_por_extenso import NumeroPorExtenso


class TestNumeroPorExtenso(TestCase):

    def test_single_positive_number(self):
        """
            converte unico digito positivo por extenso
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(5) == 'cinco'
        assert numero_por_extenso.get(0) == 'zero'

    def test_single_negative_number(self):
        """
            converte unico digito negativo por extenso
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(-1) == 'menos um'
        assert numero_por_extenso.get(-5) == 'menos cinco'

    def test_dezena(self):
        """
            converte dezena (de 20 a 99) por extenso
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(20) == 'vinte'
        assert numero_por_extenso.get(21) == 'vinte e um'
        assert numero_por_extenso.get(22) == 'vinte e dois'
        assert numero_por_extenso.get(29) == 'vinte e nove'
        assert numero_por_extenso.get(30) == 'trinta'
        assert numero_por_extenso.get(35) == 'trinta e cinco'
        assert numero_por_extenso.get(60) == 'sessenta'
        assert numero_por_extenso.get(70) == 'setenta'
        assert numero_por_extenso.get(99) == 'noventa e nove'

    def test_primeira_dezena(self):
        """
            converte primeira dezena (de 11 a 19) por extenso
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(11) == 'onze'
        assert numero_por_extenso.get(12) == 'doze'
        assert numero_por_extenso.get(13) == 'treze'
        assert numero_por_extenso.get(14) == 'quatorze'
        assert numero_por_extenso.get(15) == 'quinze'
        assert numero_por_extenso.get(16) == 'dezesseis'
        assert numero_por_extenso.get(17) == 'dezessete'
        assert numero_por_extenso.get(18) == 'dezoito'
        assert numero_por_extenso.get(19) == 'dezenove'

    def test_centena(self):
        """
            converte centena (de 100 a 999) por extenso
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(100) == 'cem'
        assert numero_por_extenso.get(101) == 'cento e um'
        assert numero_por_extenso.get(111) == 'cento e onze'
        assert numero_por_extenso.get(129) == 'cento e vinte e nove'
        assert numero_por_extenso.get(172) == 'cento e setenta e dois'
        assert numero_por_extenso.get(199) == 'cento e noventa e nove'

    def test_milhar_menor(self):
        """
            converte milhar (de 1000 a 9999) por extenso
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(1000) == 'mil'
        assert numero_por_extenso.get(1001) == 'mil e um'
        assert numero_por_extenso.get(1012) == 'mil e doze'
        assert numero_por_extenso.get(1020) == 'mil e vinte'
        assert numero_por_extenso.get(1022) == 'mil e vinte e dois'

        assert numero_por_extenso.get(1100) == 'mil e cem'
        assert numero_por_extenso.get(1101) == 'mil cento e um'
        assert numero_por_extenso.get(1199) == 'mil cento e noventa e nove'

        assert numero_por_extenso.get(1200) == 'mil e duzentos'
        assert numero_por_extenso.get(1201) == 'mil duzentos e um'
        assert numero_por_extenso.get(1299) == 'mil duzentos e noventa e nove'

        assert numero_por_extenso.get(1234) == 'mil duzentos e trinta e quatro'
        assert numero_por_extenso.get(1300) == 'mil e trezentos'
        assert numero_por_extenso.get(1350) == 'mil trezentos e cinquenta'

        assert numero_por_extenso.get(2000) == 'dois mil'
        assert numero_por_extenso.get(2001) == 'dois mil e um'
        assert numero_por_extenso.get(2019) == 'dois mil e dezenove'
        assert numero_por_extenso.get(2099) == 'dois mil e noventa e nove'
        assert numero_por_extenso.get(2100) == 'dois mil e cem'

        assert numero_por_extenso.get(3000) == 'três mil'
        assert numero_por_extenso.get(9999) == 'nove mil novecentos e noventa e nove'

        assert numero_por_extenso.get(10000) == 'dez mil'
        assert numero_por_extenso.get(10001) == 'dez mil e um'
        assert numero_por_extenso.get(10100) == 'dez mil e cem'
        assert numero_por_extenso.get(10120) == 'dez mil cento e vinte'

        assert numero_por_extenso.get(11000) == 'onze mil'
        assert numero_por_extenso.get(25123) == 'vinte e cinco mil cento e vinte e três'

        assert numero_por_extenso.get(99999) == 'noventa e nove mil novecentos e noventa e nove'

    def test_numeros_negativos_aleatorios(self):
        """
            escreve por extenso numeros negativos aleatorios
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(-1000) == 'menos mil'
        assert numero_por_extenso.get(-1001) == 'menos mil e um'
        assert numero_por_extenso.get(-1012) == 'menos mil e doze'
        assert numero_por_extenso.get(-1020) == 'menos mil e vinte'
        assert numero_por_extenso.get(-1022) == 'menos mil e vinte e dois'

        assert numero_por_extenso.get(-1100) == 'menos mil e cem'
        assert numero_por_extenso.get(-1101) == 'menos mil cento e um'
        assert numero_por_extenso.get(-1199) == 'menos mil cento e noventa e nove'

        assert numero_por_extenso.get(-11000) == 'menos onze mil'
        assert numero_por_extenso.get(-25123) == 'menos vinte e cinco mil cento e vinte e três'

        assert numero_por_extenso.get(-99999) == 'menos noventa e nove mil novecentos e noventa e nove'

    def test_numeros_positivos_aleatorios(self):
        """
            escreve por extenso numeros positivos aleatorios
        """
        numero_por_extenso = NumeroPorExtenso()
        assert numero_por_extenso.get(0) == 'zero'
        assert numero_por_extenso.get(1) == 'um'
        assert numero_por_extenso.get(-1042) == 'menos mil e quarenta e dois'
        assert numero_por_extenso.get(94587) == 'noventa e quatro mil quinhentos e oitenta e sete'


