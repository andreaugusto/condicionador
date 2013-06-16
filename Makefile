.PHONY: test run

run:
	python3 simulador.py

test:
	python3 -m unittest tests
