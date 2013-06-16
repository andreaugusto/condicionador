**Build Status:** [![Build Status](https://drone.io/github.com/andreaugusto/condicionador/status.png)](https://drone.io/github.com/andreaugusto/condicionador/latest)

---

Dependências:
* python >= 2.7
* pip (para instalar as dependências dos testes)

Inicie por aqui:
```
git clone https://github.com/andreaugusto/condicionador.git
cd condicionador
```

Para executar testes e desafio:
```
./configure && make
```

Para utilizar os parâmetros default do desafio:
```
make run
```

Para utilizar outros parâmetros na simulação:
```
python runner.py [-h] [minuto] [temperatura_atual] [temperatura_desejada]
```

Para executar os testes com tox:
```
make test
```
