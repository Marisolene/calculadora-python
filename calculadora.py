# calculadora.py
# Autor: Mariana Solene da Silva
# Data: 13/08/2025
# Descrição: Calculadora básica em Python que realiza as 4 operações fundamentais.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print("=== Calculadora Básica ===")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"Soma: {soma(n1, n2)}")
print(f"Subtração: {subtracao(n1, n2)}")
print(f"Multiplicação: {multiplicacao(n1, n2)}")
print(f"Divisão: {divisao(n1, n2)}")