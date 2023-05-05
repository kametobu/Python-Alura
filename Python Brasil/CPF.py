from validate_docbr import CPF

class CAD_CPF(CPF):
    def __init__(self,set_cpf: str):
        super().__init__()
        self.user_cpf = self.cpf_eh_Valido(set_cpf)
    
    def cpf_eh_Valido(self,set_cpf_valor: str) -> str:
        if not self.validate(set_cpf_valor):
            raise ValueError("CPF INVALIDO!!")
        return set_cpf_valor

    def __str__(self):
        return self.mask(self.user_cpf)

