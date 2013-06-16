.PHONY: test run

all: test run clean

run:
	@echo "\n-----Executando Simulador-----"
	python simulador.py

test:
	@echo "\n-----Executando testes-----"
	@pip install -qr test_requirements.txt
	nosetests --with-coverage

clean:
	@echo "\n-----Limpando diretório-----"
	@find . -name \*.pyc -delete
	@rm -Rf htmlcov
