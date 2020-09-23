#Exercicio01
#dicionario
mes = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho", 
    7: "Julho",
    8: "Agosto", 
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
x = int(input("Insira um número (entre 1 e 12): "))
#if para verificar se o numero corresponde a um mes.
if (x > 12) or (x < 0):
    print("O numero nao corresponde a nenhum mês, tente novamente")
else: 
    print("O mês correspondente é: ", mes[x])