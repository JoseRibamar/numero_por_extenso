from .tradutor import Tradutor


class NumeroPorExtenso:

    def intervalo_valido(self, number):
        return number >= -99999 and number <= 99999

    def get(self, number):
        numero_por_extenso = ''

        if number < 0:
            numero_por_extenso += 'menos '

        string_number = str(number).replace('-', '')

        if len(string_number) == 5:
            numero_por_extenso += self._dezena_milhar(string_number, True)

        if len(string_number) == 4:
            numero_por_extenso += self._milhar(string_number, True)

        if len(string_number) == 3:
            numero_por_extenso += self._centena(string_number, True)

        if len(string_number) == 2:
            numero_por_extenso += self._dezena(string_number, True)

        if len(string_number) == 1:
            numero_por_extenso += self._unidade(string_number, True)

        return numero_por_extenso

    def _dezena_milhar(self, string_number, full_number=False):
        numero_por_extenso = ''
        inteiro = int(string_number)

        parte = string_number[0:2]
        restante = string_number[-3:]
        numero_por_extenso += self._dezena(parte) + ' mil'
        if int(restante) > 0:
            numero_por_extenso += self._centena(restante)

        return numero_por_extenso

    def _milhar(self, string_number, full_number=False):
        numero_por_extenso = ''
        inteiro = int(string_number)

        if inteiro == 1000:
            numero_por_extenso += 'mil'
        elif inteiro > 1000 and inteiro < 1100:
            numero_por_extenso += 'mil'
            centena = string_number[-3:]
            numero_por_extenso += self._centena(centena)
        elif inteiro >= 1100 and inteiro < 2000:
            numero_por_extenso += 'mil'
            centena = string_number[-3:]
            numero_por_extenso += self._centena(centena)
        else:
            parte = string_number[0]
            restante = string_number[-3:]
            numero_por_extenso += self._unidade(parte) + ' mil'
            if int(restante) > 0:
                numero_por_extenso += self._centena(restante)

        return numero_por_extenso

    def _centena(self, string_number, full_number=False):
        numero_por_extenso = ''
        inteiro = int(string_number)

        if inteiro < 100:
            dezena = string_number[-2:]
            numero_por_extenso += self._dezena(dezena)
            if not full_number:
                numero_por_extenso = ' e ' + numero_por_extenso
            else:
                numero_por_extenso
        elif inteiro == 100:
            numero_por_extenso += Tradutor.centena(inteiro)
            if not full_number:
                numero_por_extenso = ' e ' + numero_por_extenso
            else:
                numero_por_extenso
        elif inteiro > 100 and inteiro < 200:
            if not full_number:
                numero_por_extenso = ' ' + numero_por_extenso
            else:
                numero_por_extenso
            numero_por_extenso += Tradutor.centena(inteiro)
            numero_por_extenso += ' e '
            dezena = string_number[-2:]
            numero_por_extenso += self._dezena(dezena)
        else:
            parte = string_number[0] + '00'
            numero_por_extenso += Tradutor.centena(int(parte))
            restante = string_number[-2:]
            if int(restante) > 0:
                numero_por_extenso = ' ' + numero_por_extenso + ' e '
                numero_por_extenso += self._dezena(restante)
            else:
                if not full_number:
                    numero_por_extenso = ' e ' + numero_por_extenso
                else:
                    numero_por_extenso

        return numero_por_extenso

    def _dezena(self, string_number, full_number=False):
        numero_por_extenso = ''
        inteiro = int(string_number)

        if inteiro < 10:
            unidade = string_number[-1:]
            numero_por_extenso += self._unidade(unidade)
        elif inteiro >= 10 and inteiro < 20:
            dezena = string_number
            numero_por_extenso += Tradutor.primeira_dezena(int(dezena))
        elif inteiro > 19:
            dezena = string_number[0] + '0'
            numero_por_extenso += Tradutor.dezena(int(dezena))
            unidade = string_number[1]
            if int(unidade) > 0:
                numero_por_extenso += ' e '
                numero_por_extenso += self._unidade(unidade)

        return numero_por_extenso

    def _unidade(self, string_number, full_number=False):
        inteiro = int(string_number)
        return Tradutor.unidade(inteiro)

