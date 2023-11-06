# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
mi = 0
si = 0
hmv = ''
mih = 0
mm20 = 0

for i in range(1,5):
    nome = str(input(f"digite o nome da {i}ª pessoa: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite \n 'M' para macho ou 'F' para femea: "))
    sexo = sexo.upper()
    
    si += idade

    if sexo == "M" and idade >= mih:
        mih = idade
        hmv = nome
    if sexo == "F" and idade < 20:
        mm20 += 1

mi = si/4

print(f"Média de idade do grupo é de {mi} anos")
print(f'O homem mais velho tem {mih} anos e se chama {hmv}.')
print(f'Ao todo são {mm20} mulheres com menos de 20 anos.')