matriz5x5 = [
    [0] * 5,
    [0] * 5,
    [1] * 5,
    [0] * 5,
    [0] * 5,
]

for line in range (5):
    for row in range (5):
        if row == line:
            matriz5x5[line][row] = 1
        else:
            matriz5x5[line][row] = 0





for linha in range(5):
    print(matriz5x5[linha])