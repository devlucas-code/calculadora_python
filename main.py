while True:
    try:
        opcao = int(input("Digite 1 para '+' 2 para '-' 3 para 'x' e 4 para '/':"))
        if opcao == 1:
            numero1 = int(input("digite o primeiro número:"))
            numero2 = int(input("digite o segundo número:"))
            print(sum(numero1, numero2))
        elif opcao == 2:
            numero1 = int(input("digite o primeiro número:"))
            numero2 = int(input("digite o segundo número:"))
            print((numero1 - numero2)) 
        elif opcao == 3:
            numero1 = int(input("digite o primeiro número:"))
            numero2 = int(input("digite o segundo número:"))
            print((numero1*numero2)) 
        elif opcao == 4:
            numero1 = int(input("digite o primeiro número:"))
            numero2 = int(input("digite o segundo número:"))
            print((numero1/numero2)) 
        else:
            print("Essa não é uma opção")
            continue
        break
    except ValueError:
        print("Isso não é um número")
        continue