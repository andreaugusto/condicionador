# -*- coding: utf-8 -*-
import logging

from simulacao.simulador import Simulador


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
