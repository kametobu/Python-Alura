from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000"  # Given-Contexto
        esperado = 23
        funcionario_test = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_test.idade()  # When-ação
        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Alann_Batista_deve_retornar_Batista(self):
        entrada = "Alann Batista "
        esperado = "Batista"
        alann = Funcionario(entrada, "13/05/1998", 1111)
        resultado = alann.sobrenome()
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000
        funcionario_test = Funcionario(
            entrada_nome, "10/05/1998", entrada_salario)
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100
        funcionario_test = Funcionario("Teste", "10/05/1998", entrada)
        resultado = funcionario_test.calcular_bonus()
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000
            funcionario_test = Funcionario("Teste", "10/05/1998", entrada)
            resultado = funcionario_test.calcular_bonus()
            assert resultado
