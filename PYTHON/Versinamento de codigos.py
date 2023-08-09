#Aula do dia 12/06/23

#                            VERSIONAMENTO DE CODIGOS

# É o processo de gerernciar e controlae as alterações de um projeto de software, permitindo que os desenvolvedores trabalhem em comjjunto em um codigo fonte compartilhado.

#   Ferramentas:
# Bit Bucket, GitHub, GitLab.

#   Git x Github 
# Git: sistema de controle dispersão.
# GitHub: plataforma de hospedagem de codigo.

#   Terminal no Windows:
# Aplicativo de linha de comando.

#   Comandos no terminal do Windows:
# 1. dir: exibe a lista de arquivos e pastas de um diretorio.
# 2. cd: navegar entre os diretorios.
# 3. cd: retorna dos diretorios. Exemplo: cd ..
# mkdir: para criar ujma pasta no terminal dar o comando: mkdir (nomedapasta), dar enter, depois digite dir novamente.
# del: deletar
# rmdir: remover um arquivo/diretorio vazio. Exemplo rmdir (nomedapasta)
# copy: copia um arquivo de um local para outro. exemplo; copy arquivo.txt C:/Destino
# move
# ren
# type: exibe o conteudo de um arquivo de texto.
# echo: exibe mensagens na tela.
# tasklist: lista os processos em execução.
# touch: cria um novo arquivo.

#   Maneiras de usar o Git
# via terminal
# desktop
# Integrado ao VScode

#   Instalar o Git
# 1 - baixar para windows
# 2 - baixar a versão 64 bits

#              CONTINUAÇÃO DA AULA   13/06/23

#   Configurando o git:
# 1 comando: git config --global user.name Layla
# 2 comando: config --global user.email (meu email do github)

#   Criando um repositorio para o p´rojeto:
# 1 - mkdir meurepo
# 2 - cd meu repo
# 3 - code .

# baixar notepad versão Notepad++ v8.5.3

#   Gerando uma chave
# Precisamos gerar uma chave SSH que computador vai usar para validar com o GitHub. Digite o seguinte comando no Git Bash:
#         ssh-keygen -t rsa -b 4096 -C "email do github"
# depois:
#             notpad ~/.ssh/id_rsa.pub

# cadastrar chave ssh no GitHub
# configurações > chave SSH e GPG > colar a chave gerada no bloco de notas na lacuna 

#   Conectando ao VScode
#