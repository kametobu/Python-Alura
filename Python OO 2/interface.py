from abc import ABC #abstract base classes
from abc import ABCMeta, abstractmethod 

from collections.abc import MutableSequence
from numbers import Complex

class Programa(metaclass = ABCMeta): 
    @abstractmethod
    def __str__(self): 
        pass

class Playlist(Programa):
    pass

class Numero(Complex): #click in Complex
    def __getitem__(self,item):
        super().__getitem__(item)

filmes = Playlist()
#numeros = Numero()
