import base64

# Função para converter string para Base64
def string_para_base64(string):
    string_bytes = string.encode('utf-8')  # Converte a string para bytes
    base64_bytes = base64.b64encode(string_bytes)  # Codifica para Base64
    return base64_bytes.decode('utf-8')  # Converte os bytes base64 para string

# Função para converter string para binário
def string_para_binario(string):
    return ''.join(format(ord(char), '08b') for char in string)  # Converte cada caractere da string para binário com 8 bits

# Função para converter Base64 para binário
def base64_para_binario(base64_string):
    base64_bytes = base64.b64decode(base64_string)  # Decodifica string base64 para bytes
    return ''.join(format(byte, '08b') for byte in base64_bytes)  # Converte os bytes para binário com zeros à esquerda

# Função para converter binário para Base64
def binario_para_base64(binario):
    bytes_data = int(binario, 2).to_bytes((len(binario) + 7) // 8, byteorder='big')  # Converte binário para bytes
    base64_bytes = base64.b64encode(bytes_data)  # Codifica os bytes para Base64
    return base64_bytes.decode('utf-8')  # Converte os bytes base64 para string


# Função para converter binário para string (normal) com caracteres ASCII legíveis
def binario_para_string(binario):
    binario = binario.replace(' ', '')  # Remove espaços da string binária
    while len(binario) % 8 != 0:
        binario = '0' + binario  # Adiciona zeros à esquerda para completar 8 bits

    caracteres = []
    for i in range(0, len(binario), 8):
        byte = binario[i:i+8]
        decimal = int(byte, 2)
        if 32 <= decimal <= 126:  # Verifica se está na faixa de caracteres ASCII legíveis
            caracteres.append(chr(decimal))
        else:
            caracteres.append('?')  # Substitui caracteres ilegíveis por "?"

    return ''.join(caracteres)  # Retorna a string original

# Função para converter Base64 para string normal
def base64_para_string(base64_string):
    base64_bytes = base64.b64decode(base64_string)  # Decodifica string base64 para bytes
    return base64_bytes.decode('utf-8')  # Decodifica os bytes para string original

# Função para converter decimal para binário
def numero_para_binario(numero):
    try:
        numero_int = int(numero)
        return bin(numero_int)[2:]  # Converte o número inteiro para binário e remove o prefixo '0b'
    except ValueError:
        return "Entrada inválida! Certifique-se de inserir um número inteiro válido."

# Função para converter binário para decimal (número inteiro)
def binario_para_numero(binario):
    # Verifica se a entrada é uma string binária válida
    if all(bit in '01' for bit in binario):
        return int(binario, 2)  # Converte a string binária para um número inteiro
    else:
        return "Entrada inválida! Certifique-se de inserir apenas 0s e 1s."

# Função principal para interação com o usuário
def calculadora_base64_binario():
    while True:  # Loop para manter o menu ativo
        print("\nEscolha uma opção:")
        print("1: Converter string para Base64")
        print("2: Converter string para Binário")
        print("3: Converter Base64 para Binário")
        print("4: Converter Binário para Base64")
        print("5: Converter Binário para string normal")
        print("6: Converter Base64 para string normal")
        print("7: Converter Número (Decimal) para Binário")
        print("8: Converter Binário para Número (Decimal)")
        print("0: Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "1":
            string = input("Digite a string que deseja converter para Base64: ")
            base64_resultado = string_para_base64(string)
            print("Resultado em Base64:", base64_resultado)

        elif escolha == "2":
            string = input("Digite a string que deseja converter para Binário: ")
            binario_resultado = string_para_binario(string)
            print("Resultado em Binário:", binario_resultado)

        elif escolha == "3":
            base64_input = input("Digite a string em Base64: ")
            binario_resultado = base64_para_binario(base64_input)
            print("Resultado em Binário:", binario_resultado)

        elif escolha == "4":
            binario_input = input("Digite a string em Binário (sem espaços): ")
            base64_resultado = binario_para_base64(binario_input)
            print("Resultado em Base64:", base64_resultado)

        elif escolha == "5":
            binario_input = input("Digite a string em Binário (com ou sem espaços): ")
            if all(bit in '01 ' for bit in binario_input):  # Verifica se a entrada é uma string binária válida (aceita espaços)
                string_resultado = binario_para_string(binario_input)
                print("Resultado em string normal:", string_resultado)
            else:
                print("Entrada inválida! Certifique-se de inserir apenas 0s e 1s.")

        elif escolha == "6":
            base64_input = input("Digite a string em Base64: ")
            string_resultado = base64_para_string(base64_input)
            print("Resultado em string normal:", string_resultado)

        elif escolha == "7":
            numero_input = input("Digite o número decimal que deseja converter para Binário: ")
            binario_resultado = numero_para_binario(numero_input)
            print("Resultado em Binário:", binario_resultado)

        elif escolha == "8":
            binario_input = input("Digite a string em Binário (sem espaços): ")
            numero_resultado = binario_para_numero(binario_input)
            print("Resultado em Número Decimal:", numero_resultado)

        elif escolha == "0":
            print("Saindo... Obrigado por usar a calculadora!")
            break  # Sai do loop e termina o programa

        else:
            print("Opção inválida! Tente novamente.")

        # Perguntar se o usuário quer tentar novamente
        continuar = input("\nDeseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Saindo... Obrigado por usar a calculadora!")
            break  # Sai do loop e termina o programa

# Executar a calculadora
calculadora_base64_binario()
