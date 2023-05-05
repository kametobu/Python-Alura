from validate_docbr import CNPJ

class CAD_CNPJ(CNPJ):
    def __init__(self,set_cnpj: str):
        super().__init__()
        self.user_cnpj = self.cnpj_eh_Valido(set_cnpj)

    def cnpj_eh_Valido(self,set_cnpj_valor: str) -> str:
      if not self.validate(set_cnpj_valor):
          raise ValueError("CNPJ INVALIDO!!")
      return set_cnpj_valor

    def __str__(self):
        return self.mask(self.user_cnpj)