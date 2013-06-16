# -*- coding: utf-8 -*-

import unittest

from core.condicionador import Condicionador
from simulador import Simulador


class CondicionadorTestCase(unittest.TestCase):

    CUSTO_LIGAR_COMPRESSOR = 0.5
    CUSTO_REDUZIR_UM_GRAU = 0.1

    def setUp(self):
        self.condicionador = Condicionador()

    def tearDown(self):
        '''Caso fosse utilizado em produção, seria legal desligar
        o compressor depois de cada teste.
        '''
        self.condicionador.desligar_compressor()

    def test_estado_inicial_compressor_desligado(self):
        self.assertFalse(self.condicionador.compressor_ligado)

    def test_ligar_compressor(self):
        self.condicionador.ligar_compressor()
        self.assertTrue(self.condicionador.compressor_ligado)

    def test_ligar_desligar_compressor(self):
        self.condicionador.ligar_compressor()
        self.condicionador.desligar_compressor()
        self.assertFalse(self.condicionador.compressor_ligado)

    def test_reduzir_um_grau_liga_compressor(self):
        self.condicionador.reduz_um_grau(0)
        self.assertTrue(self.condicionador.compressor_ligado)

    def test_refigera_recebe_temp_atual_e_temp_desejada(self):
        try:
            self.condicionador.refrigera(temp_atual=10, temp_desejada=20)
        except TypeError as err:
            self.fail('Parâmetros de entrada de \
                      condicionador.refrigera estão errados: %s' % err)

    def test_reduz_um_grau_baixa_um_grau_temperatura(self):
        temp_atual = 1
        temp_esperada = 0
        temp_baixada, custo = self.condicionador.reduz_um_grau(
            temp_atual
        )
        self.assertEqual(temp_baixada, temp_esperada)

    def test_primeira_reduzida_liga_compressor(self):
        self.condicionador.reduz_um_grau(10)
        self.assertTrue(self.condicionador.compressor_ligado)

    def test_primeira_reduzida_add_custo_compressor(self):
        temp, custo = self.condicionador.reduz_um_grau(10)
        self.assertEqual(
            custo,
            CondicionadorTestCase.CUSTO_LIGAR_COMPRESSOR +
            CondicionadorTestCase.CUSTO_REDUZIR_UM_GRAU
        )

    def test_segunda_reduzida_nao_duplica_custo_compressor(self):
        self.condicionador.reduz_um_grau(10)
        temp, custo = self.condicionador.reduz_um_grau(10)
        self.assertEqual(
            custo,
            CondicionadorTestCase.CUSTO_REDUZIR_UM_GRAU
        )

    def test_refrigera_retorna_tupla_temp_final_e_custo(self):
        retorno = self.condicionador.refrigera(30, 20)
        self.assertIsInstance(retorno, tuple)
        self.assertEqual(len(retorno), 2)


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
