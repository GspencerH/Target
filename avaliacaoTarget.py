# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CMks-1C6A7S3hyssYAiJil26-_9pz3k7
"""



#Questão 1

#SOMA = 91.



#Questão 2

def sequencia_fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    return sequencia

def principal():

    numero = int(input("Informe um número: "))

    sequencia = sequencia_fibonacci(numero)
    if numero in sequencia:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    principal()



#Questão 3


import json

def calcular_faturamento(faturamento_diario):
    faturamento_valido = [f["valor"] for f in faturamento_diario if f["valor"] is not None]
    if not faturamento_valido:
        return None, None, 0
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_superiores_media = sum(1 for faturamento in faturamento_valido if faturamento > media_mensal)
    return menor_faturamento, maior_faturamento, dias_superiores_media

def principal():
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    faturamento_diario = dados["faturamento_diario"]
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)
    print(f"Menor valor de faturamento: R${menor:.2f}")
    print(f"Maior valor de faturamento: R${maior:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

if __name__ == "__main__":
    principal()

#Questão 4


def calcular_percentuais(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}
    return percentuais

def principal():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    percentuais = calcular_percentuais(faturamento_estados)

    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    principal()


#Questão 5

def inverter_string(s):
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

def principal():
    entrada = input("Informe uma string para inverter: ")
    resultado = inverter_string(entrada)
    print(f"String invertida: {resultado}")

if __name__ == "__main__":
    principal()