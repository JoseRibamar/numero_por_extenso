from django.test import TestCase
from core.tradutor import Tradutor


class TestTradutor(TestCase):

    def test_unidade(self):
        """
            traduz unidade por extenso
        """
        assert Tradutor.unidade(1) == 'um'
        assert Tradutor.unidade(2) == 'dois'
        assert Tradutor.unidade(3) == 'três'
        assert Tradutor.unidade(4) == 'quatro'
        assert Tradutor.unidade(5) == 'cinco'
        assert Tradutor.unidade(6) == 'seis'
        assert Tradutor.unidade(7) == 'sete'
        assert Tradutor.unidade(8) == 'oito'
        assert Tradutor.unidade(9) == 'nove'

    def test_primeira_dezena(self):
        """
            traduz primeira dezena (do 11 ao 19)
        """
        assert Tradutor.primeira_dezena(11) == 'onze'
        assert Tradutor.primeira_dezena(12) == 'doze'
        assert Tradutor.primeira_dezena(13) == 'treze'
        assert Tradutor.primeira_dezena(14) == 'quatorze'
        assert Tradutor.primeira_dezena(15) == 'quinze'
        assert Tradutor.primeira_dezena(16) == 'dezesseis'
        assert Tradutor.primeira_dezena(17) == 'dezessete'
        assert Tradutor.primeira_dezena(18) == 'dezoito'
        assert Tradutor.primeira_dezena(19) == 'dezenove'

    def test_dezena(self):
        """
            traduz dezena (do 20 ao 90)
        """
        assert Tradutor.dezena(20) == 'vinte'
        assert Tradutor.dezena(30) == 'trinta'
        assert Tradutor.dezena(40) == 'quarenta'
        assert Tradutor.dezena(50) == 'cinquenta'
        assert Tradutor.dezena(60) == 'sessenta'
        assert Tradutor.dezena(70) == 'setenta'
        assert Tradutor.dezena(80) == 'oitenta'
        assert Tradutor.dezena(90) == 'noventa'

    def test_primeira_centena(self):
        """
            traduz primeira centena (do 100 ao 199)
        """
        assert Tradutor.centena(100) == 'cem'
        assert Tradutor.centena(101) == 'cento'

    def test_centena(self):
        """
            traduz centena (do 200 ao 900)
        """
        assert Tradutor.centena(200) == 'duzentos'
        assert Tradutor.centena(300) == 'trezentos'
        assert Tradutor.centena(400) == 'quatrocentos'
        assert Tradutor.centena(500) == 'quinhentos'
        assert Tradutor.centena(600) == 'seiscentos'
        assert Tradutor.centena(700) == 'setecentos'
        assert Tradutor.centena(800) == 'oitocentos'
        assert Tradutor.centena(900) == 'novecentos'

