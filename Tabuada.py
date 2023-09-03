acumulador_notas = 0
voltas = 0

while True:
    nota = input("Digite a nota: ")

    if nota not in "012345678910:":
        print("Numeros não encontrado")
    else:
        nota = float(nota)

        if nota >= 0 and nota <= 10:
            acumulador_notas += nota
            voltas += 1

            escolha = input("Quer adicionar mais uma nota? (s/n)")

            if escolha.lower() == 'n' or escolha.lower() == "não":
                break
            else:
                print("Notas apenas entr 0 e 10")


media = acumulador_notas / voltas

print(media)