from datetime import datetime,date,timedelta
from functools import total_ordering

class DT_BR():
    def __init__(self):
        self.create_user = datetime.today()

    def mes_cad(self):
        meses_do_ano = [
            "janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"
        ]
        return meses_do_ano[self.create_user.month-1]

    def dia_semana(self):
        dias_semanas = ["segunda","terça","quarta","quinta","sexta","sabado","domingo"]
        return dias_semanas[self.create_user.weekday()]

    def tempo_cad(self):
        tempo = (self.create_user + timedelta(days=1)) - datetime.today() 
        return tempo

    def __str__(self):
        return self.create_user.strftime("%d/%m/%y %H:%M")

teste = DT_BR()
print(teste.mes_cad())
print(teste.dia_semana())
print(teste)
print(teste.tempo_cad())
