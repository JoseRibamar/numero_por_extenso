
class Tradutor:

    @classmethod
    def unidade(self, number):
        mapeamento = {
            0: 'zero',
            1: 'um',
            2: 'dois',
            3: 'três',
            4: 'quatro',
            5: 'cinco',
            6: 'seis',
            7: 'sete',
            8: 'oito',
            9: 'nove'
        }
        return mapeamento[number]

    @classmethod
    def primeira_dezena(self, number):
        mapeamento = {
            10: 'dez',
            11: 'onze',
            12: 'doze',
            13: 'treze',
            14: 'quatorze',
            15: 'quinze',
            16: 'dezesseis',
            17: 'dezessete',
            18: 'dezoito',
            19: 'dezenove'
        }
        return mapeamento[number]

    @classmethod
    def dezena(self, number):
        mapeamento = {
            20: 'vinte',
            30: 'trinta',
            40: 'quarenta',
            50: 'cinquenta',
            60: 'sessenta',
            70: 'setenta',
            80: 'oitenta',
            90: 'noventa'
        }
        return mapeamento[number]

    @classmethod
    def centena(self, number):
        if number == 100:
            return 'cem'
        elif number > 100 and number < 200:
            return 'cento'

        mapeamento = {
            200: 'duzentos',
            300: 'trezentos',
            400: 'quatrocentos',
            500: 'quinhentos',
            600: 'seiscentos',
            700: 'setecentos',
            800: 'oitocentos',
            900: 'novecentos'
        }

        return mapeamento[number]

