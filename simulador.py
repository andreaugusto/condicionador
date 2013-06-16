import logging

from condicionador import Condicionador


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


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="Simulador para executar classe Condicionador"
    )
    parser.add_argument(
        'minutos',
        default=360,
        nargs='?',
        type=int,
        help="Minutos que o simulador deve simular"
    )
    parser.add_argument(
        'temp_atual',
        default=30,
        nargs='?',
        type=int,
        help="Temperatura atual que deve ser assumida pelo simulador"
    )
    parser.add_argument(
        'temp_desejada',
        default=20,
        nargs='?',
        type=int,
        help="Temperatura que o simulador deve solicitar ao condicionador"
    )

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = parse_args()

    logging.basicConfig(level=logging.INFO)
    simulador = Simulador()
    simulador.executar(**vars(args))
