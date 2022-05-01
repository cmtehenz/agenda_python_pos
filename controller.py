'''
Agenda simples
'''
__author__ = 'Gustavo Costa'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from tabulate import tabulate
from contato import Contato

class Controller():
  def inserir(nome, telefone, cidade, estado, status):
    return Contato(nome, telefone, cidade, estado, status)

  def listarAll(listaContatos):
    table = []
    headers = ["NOME", "TELEFONE" , "CIDADE", "ESTADO", "STATUS"]
    for item in listaContatos:
      table.append([item.getNome(), item.getTelefone(), item.getCidade(), item.getEstado(), item.getStatus()])
    print(tabulate(table, headers, tablefmt="fancy_grid"))

  def listarNome(listaTelefone, nome):
    cont = 0
    for tel in listaTelefone:
      if tel.getNome() == nome:
        print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
        break
      cont += 1

  def deletarAll(listaTelefone):
    if len(listaTelefone) != 0:
      listaTelefone.clear()
      return 'Todos os contatos foram removidos!'
    else:
      return 'A lista telefonica está vazia!'

  def deletarNome(listaTelefone, nome):
    if len(listaTelefone) != 0:
      cont = 0
      for tel in listaTelefone:
        if tel.getNome() == nome:
          listaTelefone.pop(cont)
          return 'Contado {} removido com sucesso!'.format(nome)
        else:
          return 'Nome não encontrado!'
    else:
      return 'Lista está vazia!'
