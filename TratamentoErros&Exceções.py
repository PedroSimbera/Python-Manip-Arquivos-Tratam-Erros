# Falhas são diferentes de erros, pois os erros são pontenciais erros de semânticas e ou sintaxe das lingaguens. Já as falhas são comportamentos do algoritmo diferente daquele que foi previsto pelo programador.

# Busque os erros e as falhas na documentação python

# Sobre as exceções
# Algo que ocorre que não é falha nem erro, e sim um problema mais conceitual. 
# Foge da regra.

# Em Python, o tratamento de exceções é realizado por meio de blocos try-except. O código suscetível a erros é colocado no bloco "try", enquanto os possíveis erros são capturados e tratados nos blocos "except". Aqui está um exemplo básico de como usar tratamento de exceções em Python:

# try:
#     # Código que pode gerar uma exceção
#     valor = int(input("Digite um número: "))
#     resultado = 10 / valor
#     print("O resultado é:", resultado)

# except ValueError:
#     print("O valor digitado não é um número válido.")

# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")

# except Exception as e:
#     print("Ocorreu um erro:", e)


# Neste exemplo, o bloco try tenta converter a entrada do usuário em um número inteiro e, em seguida, realiza uma divisão por esse número. Se o usuário digitar um valor inválido (por exemplo, uma string), uma exceção do tipo ValueError será gerada. Se o usuário digitar zero, uma exceção do tipo ZeroDivisionError será gerada. O bloco except correspondente captura cada tipo de exceção e executa o código apropriado.



# Além disso, você pode usar o bloco "finally" para definir um código que sempre será executado, independentemente de ocorrer uma exceção ou não. Por exemplo:

# try:
#     # Código que pode gerar uma exceção
#     arquivo = open("dados.txt", "r")
#     # Processar o arquivo
#     arquivo.close()

# except FileNotFoundError:
#     print("O arquivo não foi encontrado.")

# finally:
#     print("Finalizando o programa...")

# Nesse caso, o bloco finally garante que o arquivo seja fechado corretamente, independentemente de ocorrer uma exceção ou não.

# É possível também usar condicionais para tratar erros, como if e else, garantindo que a entrada seja a adequada