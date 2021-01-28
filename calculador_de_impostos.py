# -*- coding: UTF-8 -*-
from impostos import ISS, ICMS, ISS_Munic, ISS_SBC


class Calculador_de_impostos(object):
    def realizar_calculo(self, orcamento, imposto):
        # duck typing...
        try:
            return imposto.calcular(orcamento)
        except AttributeError:
            return "method not found"


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adicionar_item(
        Item(nome='Notebook importado do canadá', valor=1540))

    orcamento.adicionar_item(
        Item(nome='Ryzen 12, 500 threads', valor=300))

    print(calculador.realizar_calculo(orcamento, ISS()))
    print(calculador.realizar_calculo(orcamento, ICMS()))
    print(calculador.realizar_calculo(orcamento, ISS_Munic()))
    print(calculador.realizar_calculo(orcamento, ISS_SBC()))
