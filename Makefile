.PHONY: test run clean

all: test run clean

run:
	@echo "\n-----Executando Simulador-----"
	python runner.py

test:
	@echo "\n-----Instalando depedências dos testes-----"
	@pip install -r test_requirements.txt
	@echo "\n-----Executando testes-----"
	tox

clean:
	@echo "\n-----Limpando diretório-----"
	@find . -name \*.pyc -delete
	@rm -Rf htmlcov
