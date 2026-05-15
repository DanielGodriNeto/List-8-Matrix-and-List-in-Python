matriz4x4 = [
            [0,0,0,0],
            [2,0,6,4],
            [0,5,0,0],
            [0,0,8,0]
]

maior = [0][0]
Mline = [0]
Mrow = [0]

for line in range(4):
    for coluna in range (4):
        if matriz4x4[line][coluna] > maior:
            maior = matriz4x4[line][coluna]
            Mline = line
            Mrow = coluna

for line in range(4):
    print(matriz4x4[line])
print ("Esse e o maior numero", maior)
print ("Esse e a coluna do maior numero", Mrow)
print ("Esse e a linha do maior numero ", Mline)
