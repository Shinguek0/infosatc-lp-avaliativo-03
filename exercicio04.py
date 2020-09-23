x = 0
idade = int(input("Insira sua idade: "))
if idade >= 16 and idade <= 69:
    idade = 1
    x += 1
else:
    idade = 0
peso = int(input("Insira seu peso: "))
if peso > 50:
    peso = 1
    x += 1
else:
    peso = 0
dormida = input("Você dormiu pelo menos 6h nas últimas 24horas?(s/n): ")
if dormida == "s":
    x += 1

if x == 3:
    print("Você está apto para ser um doador")
else:
    print("Voce não está apto, pois:")
    if idade != 1:
        print(" Você não tem a idade ideal, que seria entre 16 e 69 anos")
    if peso != 1:
        print(" Você tem menos de 50kg")
    if dormida != "s":
        print(" Você nao dormiu pelo menos 6horas nas últimas 24horas")