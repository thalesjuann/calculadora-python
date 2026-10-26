print("==============================")
print("     CALCULADORA EM PYTHON")
print("==============================")

while True:
    print("\n1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida!")

    else:
        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))

        if opcao == "1":
            resultado = numero1 + numero2
            operacao = "+"

        elif opcao == "2":
            resultado = numero1 - numero2
            operacao = "-"

        elif opcao == "3":
            resultado = numero1 * numero2
            operacao = "*"

        elif opcao == "4":
            if numero2 == 0:
                print("Erro: divisão por zero não é permitida.")
                resultado = None
            else:
                resultado = numero1 / numero2
                operacao = "/"

        if resultado is not None:
            print(f"\nResultado: {numero1} {operacao} {numero2} = {resultado}")

    continuar = input("\nOutro cálculo? (s/n): ")

    if continuar.lower() != "s":
        print("Programa encerrado.")
        break