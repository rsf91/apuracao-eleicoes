# Apuração dos votos da Eleição 2022 em tempo real

Atualização de 5 em 5 minutos com criação de um log a cada 25 minutos do resultado e % da apuração. Arquivo já atualizado para o 2o Turno das eleições de 2022.

# Pré-requisitos:

Bibliotecas: <code>pandas</code>, <code>requests</code> e <code>json</code>

# Como funciona:

São dois scripts em Python. O arquivo <code>apuracao.py</code> capturarará o json do TSE e a cada minuto fará um print no seu terminal dos resultados atuais
A cada 5 minutos esse arquivo irá criar um TXT com os dados capturados daquele momento:
    timestamp;resultados;porcentagem da apuracao

O segundo arquivo <code>analise_apuracao.py</code> irá capturar o arquivo txt criado pela <code>apuracao.py</code> e produzirá um gráfico com a progressão da apuração.

# Recomendo:

Caso você já rode o pacote Anaconda, recomendo usar o Spider e rodar cada arquivo em Consoles diferentes, assim um continua rodando enquanto o outro você consegue rodar o gráfico pra ver como anda a progressão
