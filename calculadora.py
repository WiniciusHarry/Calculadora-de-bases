def lin():
    print("--" * 20)
    
lin()
print("Calculadora de bases")
lin()

menu = """
[1] Decimal para Binário
[2] Decimal para Octal
[3] Decimal para Hexadecimal
[4] Binário para Decimal
[5] Binário para Octal
[6] Binário para Hexadecimal
[7] Octal para Binário
[8] Octal para Decimal
[9] Octal para Hexadecimal
[10] Hexadecimal para Binario
[11] Hexadecimal para Decimal
[12] Hexadecimal para Octal
"""
print(menu)
opcao = int(input("Escolha uma opção: "))
lin()


if opcao == 1:
    numero = int(input("Digite o número: "))
    def decimal_to_binario(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número inteiro não negativo."
        elif numero == 0:
            return "0"
        
        binario = ""
        while numero > 0:
            binario = str(numero % 2) + binario
            print(f"Dividindo {numero} por 2, resto: {numero % 2}, quociente: {numero // 2}")
            numero //= 2
        lin()
        return binario
    print(f"O número {numero} em binário é: {decimal_to_binario(numero)}")  
    lin()


if opcao == 2:
    numero = int(input("Digite o número: "))
    def decimal_to_octal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número inteiro não negativo."
        elif numero == 0:
            return "0"
        
        octal = ""
        while numero > 0:
            octal = str(numero % 8) + octal
            print(f"Dividindo {numero} por 8, resto: {numero % 8}, quociente: {numero // 8}")
            numero //= 8
        lin()
        return octal
    print(f"O número {numero} em octal é: {decimal_to_octal(numero)}") 
    lin()
    

if opcao == 3:
    numero = int(input("Digite o número: "))
    def decimal_to_hexadecimal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número inteiro não negativo."
        elif numero == 0:
            return "0"
        
        hexadecimal = ""
        while numero > 0:
            resto = numero % 16
            if resto < 10:
                hexadecimal = str(resto) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
            print(f"Dividindo {numero} por 16, resto: {resto}, quociente: {numero // 16}, caractere: {hexadecimal[0]}")
            numero //= 16
        lin()
        return hexadecimal
    print(f"O número {numero} em hexadecimal é: {decimal_to_hexadecimal(numero)}") 
    lin()
    

if opcao == 4:
    numero = int(input("Digite o número: "))
    def binario_to_decimal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número binário não negativo."
        
        decimal = 0
        potencia = 0
        while numero > 0:
            digito = numero % 10
            if digito not in [0, 1]:
                return "Número inválido. Por favor, insira um número binário válido."
            decimal += digito * (2 ** potencia)
            print(f"Multiplicando {digito} por 2^{potencia}, temos: {digito * (2 ** potencia)}, e somando ao total: {decimal}")
            numero //= 10
            potencia += 1
        lin()
        return decimal
    print(f"O número {numero} em decimal é: {binario_to_decimal(numero)}")
    lin()
    

if opcao == 5:
    numero = int(input("Digite o número: "))
    def binario_to_octal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número binário não negativo."
        
        decimal = 0
        potencia = 0
        print(f"Convertendo o número binário {numero} para decimal:")
        while numero > 0:
            digito = numero % 10
            if digito not in [0, 1]:
                return "Número inválido. Por favor, insira um número binário válido."
            decimal += digito * (2 ** potencia)
            print(f"Multiplicando {digito} por 2^{potencia}, temos: {digito * (2 ** potencia)}, e somando ao total: {decimal}")
            numero //= 10
            potencia += 1
        lin()
        print(f"Convertendo o número decimal {decimal} para octal:")
        octal = ""
        while decimal > 0:
            octal = str(decimal % 8) + octal
            print(f"Dividindo {decimal} por 8, resto: {decimal % 8}, quociente: {decimal // 8}")
            decimal //= 8
        lin()
        return octal
    print(f"O número binário {numero} em octal é: {binario_to_octal(numero)}")
    lin()
    
    
if opcao == 6:
    numero = int(input("Digite o número: "))
    def binario_to_hexadecimal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número binário não negativo."
        
        decimal = 0
        potencia = 0
        print(f"Convertendo o número binário {numero} para decimal:")
        while numero > 0:
            digito = numero % 10
            if digito not in [0, 1]:
                return "Número inválido. Por favor, insira um número binário válido."
            decimal += digito * (2 ** potencia)
            print(f"Multiplicando {digito} por 2^{potencia}, temos: {digito * (2 ** potencia)}, e somando ao total: {decimal}")
            numero //= 10
            potencia += 1
        lin()
        print(f"Convertendo o número decimal {decimal} para hexadecimal:")
        hexadecimal = ""
        while decimal > 0:
            resto = decimal % 16
            if resto < 10:
                hexadecimal = str(resto) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
                print(f"Dividindo {decimal} por 16, resto: {resto}, quociente: {decimal // 16}, caractere: {hexadecimal[0]}")
                decimal //= 16
        lin()
        return hexadecimal
    print(f"O número binário {numero} em hexadecimal é: {binario_to_hexadecimal(numero)}")
    lin()
    

if opcao == 7:
    numero = int(input("Digite o número: "))
    def octal_to_binario(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número octal não negativo."
        
        decimal = 0
        potencia = 0
        print(f"Convertendo o número octal {numero} para decimal:")
        while numero > 0:
            digito = numero % 10
            if digito < 0 or digito > 7:
                return "Número inválido. Por favor, insira um número octal válido."
            decimal += digito * (8 ** potencia)
            print(f"Multiplicando {digito} por 8^{potencia}, temos: {digito * (8 ** potencia)}, e somando ao total: {decimal}")
            numero //= 10
            potencia += 1
        lin()
        print(f"Convertendo o número decimal {decimal} para binário:")
        binario = ""
        while decimal > 0:
            binario = str(decimal % 2) + binario
            print(f"Dividindo {decimal} por 2, resto: {decimal % 2}, quociente: {decimal // 2}")
            decimal //= 2
        lin()
        return binario
    print(f"O número octal {numero} em binário é: {octal_to_binario(numero)}")
    lin()

    
if opcao == 8:
    numero = int(input("Digite o número: "))
    def octal_to_decimal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número octal não negativo."
        
        decimal = 0
        potencia = 0
        print(f"Convertendo o número octal {numero} para decimal:")
        while numero > 0:
            digito = numero % 10
            if digito < 0 or digito > 7:
                return "Número inválido. Por favor, insira um número octal válido."
            decimal += digito * (8 ** potencia)
            print(f"Multiplicando {digito} por 8^{potencia}, temos: {digito * (8 ** potencia)}, e somando ao total: {decimal}")
            numero //= 10
            potencia += 1
        lin()
        return decimal
    print(f"O número octal {numero} em decimal é: {octal_to_decimal(numero)}")
    lin()
    

if opcao == 9:
    numero = int(input("Digite o número: "))
    def octal_to_hexadecimal(numero):
        if numero < 0:
            return "Número inválido. Por favor, insira um número octal não negativo."
        
        decimal = 0
        potencia = 0
        print(f"Convertendo o número octal {numero} para decimal:")
        while numero > 0:
            digito = numero % 10
            if digito < 0 or digito > 7:
                return "Número inválido. Por favor, insira um número octal válido."
            decimal += digito * (8 ** potencia)
            print(f"Multiplicando {digito} por 8^{potencia}, temos: {digito * (8 ** potencia)}, e somando ao total: {decimal}")
            numero //= 10
            potencia += 1
        lin()
        print(f"Convertendo o número decimal {decimal} para hexadecimal:")
        hexadecimal = ""
        while decimal > 0:
            resto = decimal % 16
            if resto < 10:
                hexadecimal = str(resto) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
                print(f"Dividindo {decimal} por 16, resto: {resto}, quociente: {decimal // 16}, caractere: {hexadecimal[0]}")
                decimal //= 16
        lin()
        return hexadecimal
    print(f"O número octal {numero} em hexadecimal é: {octal_to_hexadecimal(numero)}")
    lin()
    

if opcao == 10:
    numero = input("Digite o número: ")

    def hexadecimal_to_binario(numero):

        numero = numero.upper()

        decimal = 0
        potencia = 0

        print(f"Convertendo o número hexadecimal {numero} para decimal:")

        # HEXADECIMAL → DECIMAL
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

            print(
                f"{digito} = {valor}, "
                f"{valor} × 16^{potencia} = "
                f"{valor * (16 ** potencia)}, "
                f"total = {decimal}"
            )

            potencia += 1

        lin()

        # DECIMAL → BINÁRIO
        print(f"Convertendo o número decimal {decimal} para binário:")

        binario = ""

        if decimal == 0:
            binario = "0"

        while decimal > 0:

            resto = decimal % 2

            binario = str(resto) + binario

            print(
                f"Dividindo {decimal} por 2, "
                f"resto: {resto}, "
                f"quociente: {decimal // 2}"
            )

            decimal //= 2

        lin()

        return binario

    print(
        f"O número hexadecimal {numero} em binário é: "
        f"{hexadecimal_to_binario(numero)}"
    )

    lin()
    
    
if opcao == 11:

    numero = input("Digite o número hexadecimal: ")

    def hexadecimal_to_decimal(numero):

        numero = numero.upper()

        decimal = 0
        potencia = 0

        print(f"Convertendo o número hexadecimal {numero} para decimal:")

        # HEXADECIMAL → DECIMAL
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

            print(
                f"{digito} = {valor}, "
                f"{valor} × 16^{potencia} = "
                f"{valor * (16 ** potencia)}, "
                f"total = {decimal}"
            )

            potencia += 1

        lin()

        return decimal

    print(
        f"O número hexadecimal {numero} em decimal é: "
        f"{hexadecimal_to_decimal(numero)}"
    )

    lin()
    

if opcao == 12:
    numero = input("Digite o número hexadecimal: ")

    def hexadecimal_to_octal(numero):

        numero = numero.upper()

        decimal = 0
        potencia = 0

        print(f"Convertendo o número hexadecimal {numero} para decimal:")

        # HEXADECIMAL → DECIMAL
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

            print(
                f"{digito} = {valor}, "
                f"{valor} × 16^{potencia} = "
                f"{valor * (16 ** potencia)}, "
                f"total = {decimal}"
            )

            potencia += 1

        lin()

        # DECIMAL → OCTAL
        print(f"Convertendo o número decimal {decimal} para octal:")

        octal = ""

        if decimal == 0:
            octal = "0"

        while decimal > 0:

            resto = decimal % 8

            octal = str(resto) + octal

            print(
                f"Dividindo {decimal} por 8, "
                f"resto: {resto}, "
                f"quociente: {decimal // 8}"
            )

            decimal //= 8

        lin()

        return octal

    print(
        f"O número hexadecimal {numero} em octal é: "
        f"{hexadecimal_to_octal(numero)}"
    )

    lin()