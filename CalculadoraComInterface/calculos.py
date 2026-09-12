# calculos.py
# Funções responsáveis pelas conversões entre bases numéricas.


def decimal_para_binario(numero):
    if numero < 0:
        return "Número inválido. Digite um inteiro não negativo."

    if numero == 0:
        return "0"

    binario = ""

    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero //= 2

    return binario


def decimal_para_octal(numero):
    if numero < 0:
        return "Número inválido. Digite um inteiro não negativo."

    if numero == 0:
        return "0"

    octal = ""

    while numero > 0:
        resto = numero % 8
        octal = str(resto) + octal
        numero //= 8

    return octal


def decimal_para_hexadecimal(numero):
    if numero < 0:
        return "Número inválido. Digite um inteiro não negativo."

    if numero == 0:
        return "0"

    hexadecimal = ""

    while numero > 0:
        resto = numero % 16

        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(ord("A") + resto - 10) + hexadecimal

        numero //= 16

    return hexadecimal


def binario_para_decimal(numero):
    numero = str(numero)

    for digito in numero:
        if digito not in "01":
            return "Número binário inválido."

    if numero == "":
        return "Número binário inválido."

    decimal = 0
    potencia = 0
    numero = int(numero)

    while numero > 0:
        digito = numero % 10
        decimal += digito * (2 ** potencia)
        numero //= 10
        potencia += 1

    return decimal


def binario_para_octal(numero):
    numero = str(numero)

    for digito in numero:
        if digito not in "01":
            return "Número binário inválido."

    if numero == "":
        return "Número binário inválido."

    while len(numero) % 3 != 0:
        numero = "0" + numero

    octal = ""

    for i in range(0, len(numero), 3):
        grupo = numero[i:i + 3]

        if grupo == "000":
            octal += "0"
        elif grupo == "001":
            octal += "1"
        elif grupo == "010":
            octal += "2"
        elif grupo == "011":
            octal += "3"
        elif grupo == "100":
            octal += "4"
        elif grupo == "101":
            octal += "5"
        elif grupo == "110":
            octal += "6"
        elif grupo == "111":
            octal += "7"

    return octal.lstrip("0") or "0"


def binario_para_hexadecimal(numero):
    numero = str(numero)

    for digito in numero:
        if digito not in "01":
            return "Número binário inválido."

    decimal = binario_para_decimal(numero)

    if isinstance(decimal, str):
        return decimal

    return decimal_para_hexadecimal(decimal)


def octal_para_binario(numero):
    numero = str(numero)

    for digito in numero:
        if digito not in "01234567":
            return "Número octal inválido."

    if numero == "":
        return "Número octal inválido."

    decimal = octal_para_decimal(numero)

    if isinstance(decimal, str):
        return decimal

    return decimal_para_binario(decimal)


def octal_para_decimal(numero):
    numero = str(numero)

    for digito in numero:
        if digito not in "01234567":
            return "Número octal inválido."

    if numero == "":
        return "Número octal inválido."

    decimal = 0
    potencia = 0
    numero = int(numero)

    while numero > 0:
        digito = numero % 10
        decimal += digito * (8 ** potencia)
        numero //= 10
        potencia += 1

    return decimal


def octal_para_hexadecimal(numero):
    decimal = octal_para_decimal(numero)

    if isinstance(decimal, str):
        return decimal

    return decimal_para_hexadecimal(decimal)


def hexadecimal_para_decimal(numero):
    numero = str(numero).upper().strip()

    if numero == "":
        return "Número hexadecimal inválido."

    decimal = 0
    potencia = 0

    for digito in reversed(numero):
        if digito.isdigit():
            valor = int(digito)
        elif digito == "A":
            valor = 10
        elif digito == "B":
            valor = 11
        elif digito == "C":
            valor = 12
        elif digito == "D":
            valor = 13
        elif digito == "E":
            valor = 14
        elif digito == "F":
            valor = 15
        else:
            return "Número hexadecimal inválido."

        decimal += valor * (16 ** potencia)
        potencia += 1

    return decimal


def hexadecimal_para_binario(numero):
    decimal = hexadecimal_para_decimal(numero)

    if isinstance(decimal, str):
        return decimal

    return decimal_para_binario(decimal)


def hexadecimal_para_octal(numero):
    decimal = hexadecimal_para_decimal(numero)

    if isinstance(decimal, str):
        return decimal

    return decimal_para_octal(decimal)


# Mantém também um menu no terminal para quem quiser usar a calculadora
# sem a interface gráfica.
def executar_terminal():
    while True:
        print("\n" + "=" * 40)
        print("CALCULADORA DE BASES")
        print("=" * 40)
        print("[1] Decimal para Binário")
        print("[2] Decimal para Octal")
        print("[3] Decimal para Hexadecimal")
        print("[4] Binário para Decimal")
        print("[5] Binário para Octal")
        print("[6] Binário para Hexadecimal")
        print("[7] Octal para Binário")
        print("[8] Octal para Decimal")
        print("[9] Octal para Hexadecimal")
        print("[10] Hexadecimal para Binário")
        print("[11] Hexadecimal para Decimal")
        print("[12] Hexadecimal para Octal")
        print("[0] Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "0":
                print("Programa encerrado.")
                break

            numero = input("Digite o número: ").strip()

            if opcao == "1":
                resultado = decimal_para_binario(int(numero))
            elif opcao == "2":
                resultado = decimal_para_octal(int(numero))
            elif opcao == "3":
                resultado = decimal_para_hexadecimal(int(numero))
            elif opcao == "4":
                resultado = binario_para_decimal(numero)
            elif opcao == "5":
                resultado = binario_para_octal(numero)
            elif opcao == "6":
                resultado = binario_para_hexadecimal(numero)
            elif opcao == "7":
                resultado = octal_para_binario(numero)
            elif opcao == "8":
                resultado = octal_para_decimal(numero)
            elif opcao == "9":
                resultado = octal_para_hexadecimal(numero)
            elif opcao == "10":
                resultado = hexadecimal_para_binario(numero)
            elif opcao == "11":
                resultado = hexadecimal_para_decimal(numero)
            elif opcao == "12":
                resultado = hexadecimal_para_octal(numero)
            else:
                print("Opção inválida.")
                continue

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Digite um número válido.")


if __name__ == "__main__":
    executar_terminal()
