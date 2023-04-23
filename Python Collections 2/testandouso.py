from collections import defaultdict,Counter

texto_1 = """Quer ficar por dentro do que está rolando na área de Inteligência Artificial? Então confira o primeiro episódio do podcast Hipsters: Fora de Controle, o mais novo spin-off do Hipsters.tech!

O Paulo Silveira, nosso host fora de controle, convida uma equipe de especialistas para um bate-papo imperdível: Marcus Mendes, host do Bolha DEV; Mário Souto, Desenvolvedor no Nubank; Sérgio Lopes, CTO da Alura; e Guilherme Silveira, CIO na Alura.

Juntos, eles compartilham algumas das coisas mais incríveis que já viram na área de IA e apresentam ferramentas úteis que já estão disponíveis para uso. Ah, e tem mais, viu? O episódio também explora os principais tópicos em IA aplicada e suas implicações na tecnologia, na sociedade e, sobretudo, no seu dia a dia.

Então, se você quer mergulhar nesse novo universo, não perca tempo e confira a transcrição completa abaixo."""


texto_2 = """Aqui na Alura falamos bastante da importância dos estudos na área Dev. Tecnologias evoluem constantemente, novos frameworks são criados ininterruptamente e paradigmas mudam a uma velocidade desconcertante - lembra de uma época que mal se falava de Inteligência Artificial? Se manter em constante atualização é um desafio puxado!

"E que horas consigo um emprego?", particularmente espero que você consiga a tão sonhada primeira vaga agora!...

Se um e-mail do recrutador não bateu agora na sua caixa de entrada, nada tema! Reuni nossos Alura Stars e pedi para cada um passar 3 dicas de como descolar o primeiro emprego (e os próximos)! Foram tantos conselhos legais que precisei dividir este post em duas partes, a segunda chega na semana que vem.

Preciso reforçar que estas dicas são opiniões pessoais, acredito que a melhor forma de aproveitar não é necessariamente seguindo tudo à risca. Inspire-se e as adapte à sua realidade. E boa sorte!"""

def analisa_frequencia_de_ctr(texto):
    aparicoes_1 = Counter(texto.lower())
    Total_Crt = sum(aparicoes_1.values())
    lista_proporcoes = [(letra, frenquencia/Total_Crt) for letra, frenquencia in aparicoes_1.items()]
    proporcoes = Counter(dict(lista_proporcoes))
    for ctr, proporcao in proporcoes.most_common(10):
        print(f"{ctr} ==> {proporcao*100:.2f}")

analisa_frequencia_de_ctr(texto_1)

analisa_frequencia_de_ctr(texto_2)
