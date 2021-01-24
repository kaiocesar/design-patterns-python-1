from impostos import calcular_ISS, calcular_ICMS


class Calculador_de_impostos(object):
    def realizar_calculo(self, orcamento, imposto):
        if imposto == 'ISS':
            imposto_calculado = calcular_ISS(orcamento)
        elif imposto == 'ICMS':
            imposto_calculado = calcular_ICMS(orcamento)
        return imposto_calculado


if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)

    print(calculador.realizar_calculo(orcamento, "ISS"))
    print(calculador.realizar_calculo(orcamento, "ICMS"))
