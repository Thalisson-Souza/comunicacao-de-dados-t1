# Codificação de Linha - Simulador

Implementação de uma ferramenta para visualizar códigos de linha e compará-los em redes de comunicação de dados.

## Códificações Implementadas
- Manchester
- Manchester Diferencial
- NRZ-I
- NRZ-L
- AMI
- Pseudoternário
- CMI
- MLT-3
- 2B1Q

## Funcionamento

Ao executar o programa, é exibido um menu interativo no terminal. Nele, o usuário pode escolher uma sequência de bits pronta, gerar uma sequência aleatória de 16 bits ou digitar manualmente os bits.

Depois disso, é possível selecionar uma das codificações implementadas para visualizar o sinal correspondente em um gráfico. Também há um modo de comparação, que permite escolher dois códigos de linha e comparar seus sinais, mostrando informações como número de transições e valor médio aproximado.

### Possibilidades

- Visualizar 2 diferentes códigos de linha a partir da mesma sequência de bits.
- Testar sequências prontas, aleatórias ou digitadas manualmente.
- Comparar dois métodos de codificação.
- Observar graficamente as mudanças de nível do sinal ao longo dos intervalos de bit.

## Como executar

### 1. Com ambiente virtual (recomendado):

```bash
python -m venv venv

# no linux/macOS
source venv/bin/activate

# no windows
venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

### 2. Sem ambiente virtual (instalação global)
```bash
pip install -r requirements.txt

python main.py
```

