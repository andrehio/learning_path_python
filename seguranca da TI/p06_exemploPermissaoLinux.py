import os
import stat

# Apenas permissao de leitura para o proprietário
# os.chmod("exemplo.txt", stat.S_IRUSR)

# Dar permissão de leitura, escrita e execução ao proprietário
# os.chmod("exemplo.txt", stat.S_IRWXU)

if os.path.isfile("exemplo.txt"):
    os.chmod("exemplo.txt", stat.S_IRWXU)

arquivo = open("exemplo.txt", "w")
arquivo.write("Escrevendo Arquivo!")
arquivo.close()

os.chmod("exemplo.txt", stat.S_IRUSR)
