import unittest

from condicionador import Condicionador
from simulador import Simulador


class CondicionadorTestCase(unittest.TestCase):

    def setUp(self):
        self.condicionador = Condicionador()

    def tearDown(self):
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

    def test_refigera_recebe_temp_atual_e_temp_desejada(self):
        try:
            self.condicionador.refrigera(temp_atual=10, temp_desejada=20)
        except TypeError as err:
            self.fail('Parâmetros de entrada de \
                      condicionador.refrigera estão errados: %s' % err)

    def test_reduz_um_grau_baixa_temperatura(self):
        temperatura_atual = self.condicionador.temperatura_atual
        self.condicionador.reduz_um_grau()
        self.assertEqual(
            self.condicionador.temperatura_atual,
            temperatura_atual - 1
        )


class SimuladorTestCase(unittest.TestCase):

    AUMENTO_TEMPERATURA_MINUTO = 0.5
    CUSTO_LIGAR_COMPRESSOR = 0.5
    CUSTO_REDUZIR_UM_GRAU = 0.1

    def setUp(self):
        self.simulador = Simulador()

    def test_temperatura_sobe_em_um_minuto(self):
        temp_atual = 30
        self.simulador.executa(
            periodo=1,
            temp_atual=temp_atual,
            temp_desejada=30
        )
        self.assertEqual(
            self.simulador.ambiente.temperatura,
            temp_atual + SimuladorTestCase.AUMENTO_TEMPERATURA_MINUTO
        )

    def test_ligar_compressor_altera_valor(self):
        custo_total = self.simulador.custo_total
        self.simulador.ligar_compressor()
        self.asserEqual(
            self.simulador.custo_total,
            custo_total + SimuladorTestCase.CUSTO_LIGAR_COMPRESSOR
        )

    def test_reduz_um_grau_altera_valor(self):
        custo_total = self.simulador.custo_total
        self.simulador.executa(periodo=1, temp_atual=30, temp_desejada=29)
        self.asserEqual(
            self.simulador.custo_total,
            custo_total +
            SimuladorTestCase.CUSTO_LIGAR_COMPRESSOR +
            SimuladorTestCase.CUSTO_REDUZIR_UM_GRAU
        )

    def test_refrigera_retorna_tupla_temp_final_e_custo(self):
        retorno = self.condicionador.refrigera(30, 20)
        self.assertIsInstance(retorno, tuple)
        self.assertEqual(len(retorno), 2)
