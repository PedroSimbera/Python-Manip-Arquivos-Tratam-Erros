# A manipulação de arquivos em Python é uma tarefa comum e útil para lidar com dados persistentes. Python fornece uma série de funções e métodos embutidos para trabalhar com arquivos de texto e binários. 

# Abrindo um arquivo:
# Para abrir um arquivo em Python, você pode usar a função embutida open(). Ela recebe dois argumentos principais: o caminho do arquivo e o modo de abertura. O modo de abertura pode ser "r" (leitura), "w" (escrita), "a" (anexação), "x" (criação exclusiva) ou "b" (modo binário). Por exemplo, para abrir um arquivo chamado "arquivo.txt" em modo de leitura, você pode fazer o seguinte:

        # arquivo = open("arquivo.txt", "r")


# Lendo o conteúdo de um arquivo:
# Após abrir um arquivo em modo de leitura, você pode ler o seu conteúdo usando o método read() do objeto de arquivo. Ele retorna todo o conteúdo do arquivo como uma string. Por exemplo:

        # arquivo = open("arquivo.txt", "r")
        # conteudo = arquivo.read()
        # print(conteudo)

# Escrevendo em um arquivo:
# Para escrever em um arquivo, você precisa abrir o arquivo em modo de escrita. Se o arquivo já existir, o conteúdo anterior será substituído. Se o arquivo não existir, um novo arquivo será criado. Para escrever no arquivo, você pode usar o método write() do objeto de arquivo. Por exemplo:

        # arquivo = open("arquivo.txt", "w")
        # arquivo.write("Olá, mundo!")
        # arquivo.close()

# É importante fechar o arquivo após terminar de escrever ou ler dele, usando o método close(). Isso garante que todos os recursos associados ao arquivo sejam liberados adequadamente.

# Manipulando arquivos com contexto:
# Uma maneira mais segura e conveniente de trabalhar com arquivos é usando o gerenciamento de contexto (with). Com o gerenciamento de contexto, você não precisa se preocupar em fechar o arquivo explicitamente. O Python cuidará disso automaticamente. Aqui está um exemplo:

        # with open("arquivo.txt", "r") as arquivo:
        #     conteudo = arquivo.read()
        #     print(conteudo)

# Nesse exemplo, o arquivo é automaticamente fechado quando o bloco with é concluído.
