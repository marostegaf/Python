from random import randint
from time import sleep

lista = []
jogos = []

print(" " * 1)
print(f"\033[32m{'JOGA NA MEGA SENA':^36}\033[m")
print(" " * 1)
quantidade = int(input("Quantos jogos você quer fazer: "))

tot = 1
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("=" * 8, f"SORTEANDO {quantidade} JOGOS", "=" * 8)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
