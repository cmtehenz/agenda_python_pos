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

  def listarNome(listaContatos, nome):
    cont = 0
    table = []
    headers = ["NOME", "TELEFONE" , "CIDADE", "ESTADO", "STATUS"]
    for item in listaContatos:
      if item.getNome() == nome:
        table.append([item.getNome(), item.getTelefone(), item.getCidade(), item.getEstado(), item.getStatus()])
        break
      cont += 1
    print(tabulate(table, headers, tablefmt="fancy_grid"))

  def deletarAll(listaTelefone):
    if len(listaTelefone) != 0:
      listaTelefone.clear()
      return 'Todos os contatos foram removidos!'
    else:
      return 'A lista telefonica está vazia!'

  def deletarNome(listaContatos, nome):
    cont = 0
    if len(listaContatos) != 0:
      for item in listaContatos:
        if item.getNome() == nome:
          listaContatos.pop(cont)
          return 'Contato {} removido com sucesso!'.format(nome)
        elif cont + 1 >= len(listaContatos):
          return 'Pessoa com o nome {} não encontrada !'.format(nome)
        else:
          cont += 1
    else:
      return 'Lista está vazia!'
