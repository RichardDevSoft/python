print("Seja muito bem vindo ao quiz!")
resposta = input("Quer começar? S/N ")

if resposta != "S":
    print("Até logo!")
    quit()

score = 0

print("Começando...")
print("------------------------------")

print("Qual o maior mandamento da Bíblia?\n (A) Amaras o teus bens acima de tudo \n (B) Amaras tua familia acima de tudo \n (C) Amaras o teu Deus de todo teu coração de toda tua força e de todo teu entendimento \n (D) Nenhuma das alternativas \n")
resposta_Um = input("Resposta : ")

if (resposta_Um == "C") or (resposta_Um == "c"):
    print("Parabéns!!!!! Você acertou!")
    score += 1
    print("------------------------------")
else:
    print("Infelizmente você errou!")


print("Qual o nome do primeiro homem criado por Deus?\n (A) João \n (B) Adão \n (C) Benedito \n (D) Adriano \n")
resposta_Dois = input("Resposta : ")
if (resposta_Dois == "B") or (resposta_Um == "b"):
    print("Parabéns!!!!! Você acertou!")
    score += 1
    print("------------------------------")
else:
    print("Infelizmente você errou!")


print("Qual o nome do último livro da Bíblia?\n (A) Ezequiel \n (B) Exôdo \n (C) Judas \n (D) Apocalipse \n")
resposta_Tres = input("Resposta : ")
if (resposta_Tres == "D") or (resposta_Um == "d"):
    print("Parabéns!!!!! Você acertou!")
    score += 1
    print("------------------------------")
else:
    print("Infelizmente você errou!")


print("Quiz terminado.........Somando pontos.... \n")    
print(f"Total de pontos é {score}")

if score == 3:
    print("Você fez a pontuação máxima!")

if score == 2:
     print("Você fez a pontuação média!")

if score == 1:
     print("Você fez a pontuação minima!")

if score == 0:
     print("Você fez a pior pontuação ;(!")