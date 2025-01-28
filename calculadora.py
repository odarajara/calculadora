def calculadora (op, n1, n2):
    if(op == 1):
        resposta = n1 + n2
    elif(op == 2):
        resposta = n1 - n2
    elif(op ==3):
        resposta = n1 * n2
    else:
        resposta = n1 / n2
    return resposta
        
op = int(input("Informe qual operação quer efetuar: (1)Soma (2)Subtração (3)Multiplicação (4)Divisão "))
n1 = int(input("Digite o primeiro número para a operação escolhida: "))
n2 = int(input("Digite o segundo número: "))
        
resultado = calculadora(op, n1, n2)

if(op ==1):
    print("A soma entre os números ", n1, " e " ,n2, " é ", resultado)
elif(op ==2):
    print("A subtração entre os números ", n1, " e " ,n2, " é ", resultado)
elif(op ==3):
    print("A multiplicação entre os números ", n1, " e " ,n2, " é ", resultado)
else:
    print("A divisão entre os números ", n1, " e " ,n2, " é ", resultado)