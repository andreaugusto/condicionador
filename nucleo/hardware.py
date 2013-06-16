import logging


logger = logging.getLogger(__name__)


def reduz_um_grau():
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Um grau reduzido.")


def ligar_compressor():
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Compressor ligado.")


def desligar_compressor():
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Compressor desligado.")
