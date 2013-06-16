.PHONY: test run

all: test run

run:
	python3 simulador.py

test:
	pip install -r test_requirements.txt
	nosetests
