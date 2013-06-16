# -*- coding: utf-8 -*-
import logging

from simulacao.core.condicionador import Condicionador


logger = logging.getLogger("simulador")


class Simulador:

    VARIACAO_TEMPERATURA_POR_MINUTO = 0.5
    INFO_FINAL = "Temperatura: {temperatura} | Custo: R${custo:.2f}"

    def __init__(self):
        self.condicionador = Condicionador()

    def varia_temperatura_ambiente(self, temperatura):
        return temperatura + Simulador.VARIACAO_TEMPERATURA_POR_MINUTO

    def log(self, temperatura, custo):
        logger.info(
            Simulador.INFO_FINAL.format(
                temperatura=temperatura,
                custo=custo
            )
        )

    def executar(self, minutos, temp_atual, temp_desejada):
        temperatura = temp_atual
        custo_total = 0
        for x in range(minutos):
            temperatura = self.varia_temperatura_ambiente(
                temperatura
            )
            temperatura, custo = self.condicionador.refrigera(
                temperatura,
                temp_desejada
            )

            custo_total += custo

        self.log(temperatura, custo_total)

        return (temperatura, custo_total)
