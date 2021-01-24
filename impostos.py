class ISS(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.06


class ISS_Munic(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.013
