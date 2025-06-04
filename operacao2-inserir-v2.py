from operacoesbd import *

conexao = criarConexao('127.0.0.1','root','12345','locadora_saojoao')

tituloFilme = 'homem da máscara de ferro'
sinopseFilme = 'leo de caprio 2006'
anoFilme = 2006

consulta = 'insert into Filme (titulo,sinopse,ano) values(%s,%s,%s)'
dados = [tituloFilme, sinopseFilme, anoFilme]

codigoFilme = insertNoBancoDados(conexao,consulta,dados)
print("Filme cadastrado com sucesso! O código é", codigoFilme)

encerrarConexao(conexao)