

# O código é do @BrennoSullivan, só tô colocando aqui pra ficar mais fácil pro pessoal copiar.
# Adicionado Loop de 1 minuto, diferença de votos e o log a cada 5 min do progresso

"""

Coisas que precisam ser ajustadas:
    
    o URL do data request
    O nome de ambos candidatos no analise apuracao - precisa ser verificado no dia

"""


import requests
import json
import pandas as pd
from time import sleep
from datetime import datetime
# import os
#import analise_apuracao

x = 0

n = 10

while n > 0:


    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
    
    #O lugar para conseguir esse caminho é no site oficial, F12, TAB NETWORK, procurar pelo termpo .json e achar algo parecido com o valor acima
    
    # https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e544;uf=sp;ufbu=sp;mubu=71072;zn=0001;se=0001/resultados/cargo/1
    

    json_data = json.loads(data.content)

    candidato = []
    partido = []
    votos = []
    porcentagem = []

    total_apurado = json_data['psi']
    total_seq1 = ''
    total_seq2 = ''

    for informacoes in json_data['cand']:

        # if informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4' or informacoes['seq'] == '7':
            candidato.append(informacoes['nm'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])

            if informacoes['seq'] == '1':
                total_seq1 = informacoes['pvap']

            if informacoes['seq'] == '2':
                total_seq2 = informacoes['pvap']

    # total_diff = float(total_seq1) - float(total_seq2)


    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns = [
        'Candidato', 'Nº de Votos', 'Porcentagem'
    ])


    print(f"""
Total apurado: {total_apurado}%
{df_eleicao}
Diff de votos: {float(total_seq1.replace(',', '.')) - float(total_seq2.replace(',', '.'))}
        """)

    #Aqui a gente cria o tuple de log

    if x==5:
        
        log_resultados = str({json_data['cand'][0]['nm']: json_data['cand'][0]['vap'],json_data['cand'][1]['nm']: json_data['cand'][1]['vap']})
        
    
        log_tuple = (str(datetime.utcnow()),
                     log_resultados,
                     total_apurado,
                     "\n"
                     )
        
        #Aqui a gente transforma esse tuple em string pra depois quebrar em grafico
        
        log_string = ";".join(log_tuple)    
        
        #Aqui é pra escrever o que está acontecendo no log 
        
        f = open("apuracao.txt", "a")
        f.write(log_string)
        f.close()
        
        x=0
        
#        analise_apuracao.create_graph()

    sleep(60)
    
    x=x+1
    
    
