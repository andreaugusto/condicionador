.PHONY: test run

run:
	python simulador.py

test:
	python -m unittest tests
