"""Escreva um algoritmo que, dado um número inteiro, retorna a quantidade de dígitos
pares existentes nele."""

inteiro = int(input("Digite numero:"))
cont = 0

for numero in str(inteiro):
    if (int(numero) % 2 == 0):
        cont += 1

print(cont)



