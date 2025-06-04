from operacoesbd import *

conexao = criarConexao('127.0.0.1','root','12345','locadora_saojoao')

consulta = 'select * from Filme'
filmes = listarBancoDados(conexao,consulta)

if len(filmes) == 0:
    print("Não existem filmes a serem exibidos")
else:
    print("Lista de Filmes:")
    for item in filmes:
        print("- Nome do filme:",item[1],"lançado em",item[3])

encerrarConexao(conexao)

print("Outra linha")