x = 0
listaNome = []
listaCPF = []
listaSenha = []
numeroCadastros = 0
numeroNaoCadastros = 0
numeroNaoAptos = 0
for i in range(5):
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
        oferta = input("Você gostaria de se cadastrar?(s/n)")
        if oferta.lower() == "s": 
                numeroCadastros += 1
                nomeCompleto = input("Cadastre seu nome completo: ")
                listaNome.append(nomeCompleto)
                cpf = int(input("Cadastre seu CPF: "))
                listaCPF.append(cpf)
                senha = input("Cadastre sua senha: ")
                listaSenha.append(senha)
        elif oferta.lower() == "n":
            print("legal, entao flw 👍")
            numeroNaoCadastros += 1

    else:
        print("Voce não está apto, pois:")
        if idade != 1:
            print(" Você não tem a idade ideal, que seria entre 16 e 69 anos")
        if peso != 1:
            print(" Você tem menos de 50kg")
        if dormida != "s":
            print(" Você nao dormiu pelo menos 6horas nas últimas 24horas")
        numeroNaoAptos += 1
    x = 0
print("Quantidade de nao Aptos: ", numeroNaoAptos)
print("Quantidade que nao se cadastrou: ", numeroNaoCadastros)
print(numeroCadastros," cadastros: ")
for i in range(numeroCadastros):
    print("Nome completo: ",listaNome[i])
    print("CPF: ",listaCPF[i])
    print("Senha: ",listaSenha[i])