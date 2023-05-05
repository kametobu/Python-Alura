from CPF import CAD_CPF
from CNPJ import CAD_CNPJ
from TELEFONE import CAD_TEL
from DT_BR import DT_BR
#Factory
class Documento():
    @staticmethod
    def cria_documento(doc):
        if len(doc) == 11:
            return CAD_CPF(doc)
        elif len(doc) == 14:
            return CAD_CNPJ(doc)
        elif len(doc) == 13:
            return CAD_TEL(doc)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!")