import re

class CAD_TEL():
    def __init__(self,set_tel: str):
        super().__init__()
        self.user_tel = self.tel_eh_Valido(set_tel)

    def tel_eh_Valido(self,set_tel_valor: str) -> str:
        if not re.match("\d+", set_tel_valor):
            raise ValueError("TELEFONE INVALIDO!!")
        return set_tel_valor

    def mask(self,set_tel_valor):
        res = re.sub("(\d{2,3})(\d{2})(\d{5})(\d{4})", r"+\1(\2)\3-\4", set_tel_valor)
        return res

    def __str__(self):
        return self.mask(self.user_tel)