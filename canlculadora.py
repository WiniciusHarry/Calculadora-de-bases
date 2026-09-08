def lin():
    print("--" * 20)
    
lin()
print("Calculadora de bases")
lin()

menu = """
[1] Decimal para Binário
[2] Decimal para Octal
[3] Decimal para Hexadecimal
"""
print(menu)
opcao = int(input("Escolha uma opção: "))
lin()
numero = int(input("Digite um número: "))
lin()

if opcao == 1:
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


if opcao == 2:
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
    

if opcao == 3:
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