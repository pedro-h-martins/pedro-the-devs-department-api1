from flask import Flask, render_template
import mysql.connector
import requests
import json
 # URL da página

url = "https://camarasempapel.camarasjc.sp.gov.br//api/publico/parlamentar/?pg=1&qtd=30"

def get_vereadores(url):
    print(url)
    response = requests.get(url)

    if response.status_code == 200:

        # Step 2: Parse the response as JSON
        data = response.json()
        parlamentares = data['parlamentares']
        
        print(len(parlamentares))
        i = 0
        while i < len(parlamentares):
            parlamentarID = parlamentares[i]['parlamentarID']
            nome = parlamentares[i]['parlamentarNome']
            partido = parlamentares[i]['partidoSigla']
            foto = parlamentares[i]['parlamentarFoto']
            situacao = parlamentares[i]['parlamentarSituacao']
            telefone = parlamentares[i]['parlamentarTelefone']
            email = parlamentares[i]['parlamentarEmail']
            comissoes = parlamentares[i]['comissoesAtuantes'] # Retorna uma lista

            if len(comissoes) > 0:
                print("Parcipou de comissões")
                getComissoes(comissoes)

            else:
                print("Não participou de comissões")
            print()
            i+=1

def getComissoes(comissoes):
    i = 0
    while i < len(comissoes):
        comissaoId = comissoes[i]['comissaID']
        comissaoNome = comissoes[i]['comissaoNome']
        comissaoCargo = comissoes[i]['comissaoCargo']

def main():
    get_vereadores(url)

main()