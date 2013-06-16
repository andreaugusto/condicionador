# -*- coding: utf-8 -*-
import logging

from nucleo import hardware


logger = logging.getLogger(__name__)


class Condicionador():

    CUSTO_LIGAR_COMPRESSOR = 0.5
    CUSTO_REDUZIR_UM_GRAU = 0.1
    VARIACAO_TEMP_ACEITAVEL = 2

    def __init__(self):
        self.compressor_ligado = False

    def refrigera(self, temp_atual, temp_desejada, **kwargs):
        '''Responsável por baixar temperatura até a
        desejada e calcular custos'''

        max_temp = temp_desejada + Condicionador.VARIACAO_TEMP_ACEITAVEL
        custo_total = 0

        while temp_atual > float(max_temp):
            temp_atual, custo_operacao = self.reduz_um_grau(temp_atual)
            custo_total += custo_operacao

        return (temp_atual, custo_total)

    def reduz_um_grau(self, temp_atual):
        ''' Chama função de Hardware reduz_um_grau

        Retorno:
        temp_alterada
        custo_operacao

        Side Effect:
        Liga compressor caso não esteja ligado
        '''

        custo_operacao = 0

        if not self.compressor_ligado:
            self.ligar_compressor()
            custo_operacao += Condicionador.CUSTO_LIGAR_COMPRESSOR

        try:
            hardware.reduz_um_grau()
        except Exception as err:
            logger.error(
                "Erro ao reduzir temperatura: {error}".format(error=err)
            )
            raise
        else:
            custo_operacao += Condicionador.CUSTO_REDUZIR_UM_GRAU
            return temp_atual - 1, custo_operacao

    def ligar_compressor(self):
        try:
            hardware.ligar_compressor()
        except Exception as err:
            logger.error(
                "Falha ao ligar compressor: {error}".format(error=err)
            )
            raise
        else:
            self.compressor_ligado = True

    def desligar_compressor(self):
        try:
            hardware.desligar_compressor()
        except Exception as err:
            logger.error(
                "Falha ao desligar compressor: {error}".format(error=err)
            )
            raise
        else:
            self.compressor_ligado = False
