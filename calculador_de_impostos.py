from impostos import calcular_ISS, calcular_ICMS, calcular_ISS_Munic


class Calculador_de_impostos(object):
    def realizar_calculo(self, orcamento, imposto):
        return imposto(orcamento)


if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)

    print(calculador.realizar_calculo(orcamento, calcular_ISS))
    print(calculador.realizar_calculo(orcamento, calcular_ICMS))
    print(calculador.realizar_calculo(orcamento, calcular_ISS_Munic))
