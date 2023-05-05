import requests

class CEP():
    def __init__(self,set_cep):
        self.cep_user = self.cep_eh_valido(set_cep)

    def cep_eh_valido(self,set_cep:str)->str:
        if len(set_cep) == 8:
            return set_cep
        else:
            raise ValueError("CEP INVALIDO")

    def busca_cep(self):
        response = requests.get(f"https://viacep.com.br/ws/{self.cep_user}/json/")
        dict_r = response.json()
        return f"{dict_r['bairro']} - {dict_r['localidade']} - {dict_r['uf']}"

    def __str__(self):
        return f"{self.cep_user[:5]}-{self.cep_user[5:]}"

user = CEP("09910640")
print(user)
print(user.busca_cep())