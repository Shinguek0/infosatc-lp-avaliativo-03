Homem = 0
Mulher = 0
HomemIdade = 0
MulherIdade = 0
HomemTotal = 0
MulherTotal = 0
Total = 0
for x in range(10):
    genero = int(input("Qual o sexo da pessoa (digite 1 para homem, e 2 para mulher): "))
    if genero == (1 or 2):
        if genero == 1:
            Homem += 1
            HomemIdade = HomemIdade + (float(input("Insira a idade da pessoa: ")))
        if genero == 2:
            Mulher += 1
            MulherIdade = MulherIdade + (float(input("Insira a idade da pessoa: ")))
    else:
        print("Numero digitado errado!!!")
        print("Tente novamente")
        break
if Homem > 0:
    HomemTotal = HomemIdade/Homem
if Mulher > 0:
    MulherTotal = MulherIdade/Mulher
if genero == (1 or 2):
    Total = (HomemIdade + MulherIdade)/10
    print("Idade media dos homens: ", HomemTotal)
    print("Idade media das mulheres: ", MulherTotal)
    print("A idade media do grupo é: ", Total)