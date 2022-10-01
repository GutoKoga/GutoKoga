combinacao = 0
for dezena1 in range(1,56):
    for dezena2 in range(dezena1 + 1, 57):
        for dezena3 in range(dezena2 + 1, 58):
            for dezena4 in range(dezena3 + 1, 59):
                for dezena5 in range(dezena4 + 1, 60):
                    for dezena6 in range(dezena5 + 1, 61):
                        combinacao += 1
                        print(combinacao,dezena1,dezena2,dezena3,dezena4,dezena5,dezena6)
