matriz = [[0]*4 for _ in range(5)]

maior_nota = -1
matricula_maior = 0

for i in range(5):
    print(f"\nAluno {i+1}")
    matriz[i][0] = int(input("Matrícula: "))
    matriz[i][1] = int(input("Média das provas: "))
    matriz[i][2] = int(input("Média dos trabalhos: "))
    
    # calcula nota final
    matriz[i][3] = matriz[i][1] + matriz[i][2]

    # verifica maior nota
    if matriz[i][3] > maior_nota:
        maior_nota = matriz[i][3]
        matricula_maior = matriz[i][0]

print("\nMatrícula com maior nota final:", matricula_maior)