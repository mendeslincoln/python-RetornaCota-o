#Documentacao API  https://github.com/raniellyferreira/economy-api
# Lincoln Mendes - https://lincolnmendes.com.br

#LIBS
from http.client import HTTPConnection
from datetime import datetime
import pandas as pd
import json


#Variáveis da conexão com API
host = "economia.awesomeapi.com.br"
request_string = "/json/last/USD-BRL,EUR-BRL"

#Criando conexão
connection = HTTPConnection(host)

#Capturando informaçoes da página
connection.request("GET", request_string)

#Salvando informaçoes em  um JSON depois em um Disc
response = connection.getresponse()
json_data = response.read()
data = json.loads(json_data)

#Método formatação Data
def format_date(utc_timestamp):
    d = datetime.utcfromtimestamp(utc_timestamp)
    offset = datetime.now() - datetime.utcnow()
    date = d + offset

    return date.strftime("%d/%m/%y")

#Método formatação Hora
def format_hora(utc_timestamp):
    d = datetime.utcfromtimestamp(utc_timestamp)
    offset = datetime.now() - datetime.utcnow()
    date = d + offset

    return date.strftime("%H:%M:%S")


#Método que retorna dados formatados
def retornaCotacao(conversao):

        #Coletando as variáveis
        moeda = str(data[conversao]['code'])
        valor = float(data[conversao]['ask'])
        variacao = float(data[conversao]['varBid'])
        variacaoPorc = float(data[conversao]['pctChange'])
        ultimaData = format_date(int (data[conversao]['timestamp']))
        ultimaHora = format_hora(int (data[conversao]['timestamp']))

        lista = {"Moeda": moeda, "Valor":valor, "Variacao":variacao,"Variacao%": variacaoPorc,  "Ultima Data" :ultimaData , "Ultima Hora": ultimaHora}
        return lista

    
#Chama os métodos com a moeada da conversão e inseri em um disc
DataSet = []
lista= {'USDBRL', 'EURBRL'}

for itens in lista:
    DataSet+=[retornaCotacao(itens)] 

#Converte em um DataFrame
df = pd.DataFrame(DataSet)
                    
print(df)