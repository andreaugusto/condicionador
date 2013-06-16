# -*- coding: utf-8 -*-

import unittest

from simulacao.simulador import Simulador
from .tests_condicionador import CondicionadorTestCase


class SimuladorTestCase(unittest.TestCase):

    AUMENTO_TEMP_MINUTO = 0.5

    def setUp(self):
        self.simulador = Simulador()

    def test_varia_temperatura_minuto(self):
        temperatura_atual = 10
        temperatura = self.simulador.varia_temperatura_ambiente(
            temperatura_atual
        )
        self.assertEqual(
            temperatura,
            temperatura_atual + SimuladorTestCase.AUMENTO_TEMP_MINUTO
        )

    def test_executar_retorna_tupla(self):
        retorno = self.simulador.executar(360, 30, 20)
        self.assertIsInstance(retorno, tuple)
        self.assertEqual(len(retorno), 2)

    def test_simulador_calcula_temperatura_correta(self):
        temperatura = 18
        temp_esperada = temperatura + SimuladorTestCase.AUMENTO_TEMP_MINUTO
        temp_recebida, custo = self.simulador.executar(
            1,
            temperatura,
            temperatura
        )
        self.assertEqual(temp_recebida, temp_esperada)

    def test_simulador_calcula_valor_correto(self):
        temp, custo = self.simulador.executar(1, 18, 18)
        self.assertEqual(custo, 0)

    def test_simulador_calcula_valor_correto_2(self):
        temp, custo = self.simulador.executar(6, 18, 18)
        self.assertEqual(
            custo,
            CondicionadorTestCase.CUSTO_LIGAR_COMPRESSOR +
            CondicionadorTestCase.CUSTO_REDUZIR_UM_GRAU
        )
