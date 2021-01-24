from impostos import ISS, ICMS, ISS_Munic


class Calculador_de_impostos(object):
    def realizar_calculo(self, orcamento, imposto):
        # duck typing...
        return imposto.calcular(orcamento)


if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)

    print(calculador.realizar_calculo(orcamento, ISS()))
    print(calculador.realizar_calculo(orcamento, ICMS()))
    print(calculador.realizar_calculo(orcamento, ISS_Munic()))
