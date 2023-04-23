class Programa():
    def __init__(self, nome,ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
    
    def dar_like(self):
        self.__likes +=1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @likes.setter
    def likes(self, valor):
        print("Valor não pode ser alterado") 
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor.title()

    def __str__(self):
        return f"{self.nome} - {self.ano} : {self.likes}"

class Filme(Programa):
    def __init__(self, nome,ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min: {self.likes}"

    def retorna_cadastro_diferenciado(self):
        pass

class Serie(Programa):
    def __init__(self, nome,ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas: {self.likes}"
        
class Playlist():
    def __init__(self,nome,programas):
        self.nome = nome
        self.__programas = programas
    #Python Data Model
    def __getitem__(self,item):
        return self.__programas[item]

    def __iter__(self):
        self.index = 0 
        return self
    
    def __next__(self):
        self.index += 1
        if self.index < len(self.__programas):
            return self.__programas[self.index]
        raise StopIteration

    def __len__(self):
        return len(self.__programas)


if __name__ == "__main__":
    vingadores = Filme("vingadores - guerra infinita",2018, 160)
    vingadores.dar_like()
    tmep = Filme("Todo Mundo em Panico", 1999, 100)
    tmep.dar_like()
    tmep.dar_like()
    #print(f"{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}")
    atlanta = Serie("atlanta",2018, 2)
    atlanta.dar_like()
    atlanta.dar_like()
    demolidor = Serie("Demolidor",2016, 2)
    demolidor.dar_like()
    demolidor.dar_like()    
    demolidor.dar_like()
    demolidor.dar_like()
    #print(f"{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}")
    filmes_e_series = [vingadores, atlanta, demolidor, tmep]

    playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)
    print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")
    for programa in playlist_fim_de_semana:
        #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
        #print(f"{programa.nome} - {detalhes}: {programa.likes}")
        print(programa)

    print(demolidor in playlist_fim_de_semana)
    