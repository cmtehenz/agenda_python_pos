'''
Agenda simples
'''
__author__ = 'Gustavo Costa'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from tabulate import tabulate

class Contato():
  def __init__(self, nome, telefone, cidade, estado, status):
    self.__nome = nome
    self.__telefone = telefone
    self.__cidade = cidade
    self.__estado = estado
    self.__status = status

  def getNome(self):
    return self.__nome
  
  def getTelefone(self):
    return self.__telefone

  def getCidade(self):
    return self.__cidade
  
  def getEstado(self):
    return self.__estado
  
  def getStatus(self):
    return self.__status


def inserir(nome, telefone, cidade, estado, status):
  return Contato(nome, telefone, cidade, estado, status)


def editarContato(listaContatos, nome):
  cont = 0
  for item in listaContatos:
    if item.getNome() == nome:
        
      print("\n" * 130)
      print("Editar usuário")
      listaContatos.pop(cont)
      nomeNovo = str(input('Digite o nome: ')).upper()
      telefone = str(input('Digite o telefone: '))
      cidade = str(input('Digite a cidade: '))
      estado = str(input('Digite o estado: '))
      while True:
        status = str(input('Digite o status [P/C]: ')).upper()
        if status in 'PC':
          break
        print('ERRO! Por favor, digite apenas P para pessoal ou C para comercial.')
      listaContatos.append(inserir(nomeNovo, telefone, cidade, estado, status))
    elif cont + 1 >= len(listaContatos):
      return 'Pessoa com o nome {} não encontrada !'.format(nome)
    else:
      cont += 1

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

agenda = []
print ("\n" * 130)

while True:
  print('~'*30)
  print('Bem vindo à agendar telefonica')
  print('~'*30)
  print('1 - Cadastrar Pessoa na Agenda')
  print('2 - Alterar dados da Pessoa')
  print('3 - Listar Agenda')
  print('4 - Procurar pessoa na Agenda')
  print('5 - Excluir Pessoa na Agenda')
  print('6 - Sair.')
  
  op = 0

  try:
    op = int(input('Entre com a opção desejada: '))
  except ValueError:
    print('Opção invalida')
    print("\n" * 5)

  if op == 1:
    print ("\n" * 130)
    print('~'*30)
    print('Cadastro novo Contato')
    print('~'*30)

    nome = str(input('Digite o nome: ')).upper()
    telefone = str(input('Digite o telefone: '))
    cidade = str(input('Digite a cidade: '))
    estado = str(input('Digite o estado: '))
    while True:
      status = str(input('Digite o status [P/C]: ')).upper()
      if status in 'PC':
        break
      print('ERRO! Por favor, digite apenas P para pessoal ou C para comercial.')
    agenda.append(inserir(nome, telefone, cidade, estado, status))
    print ("\n" * 5)
    print('CONTATO SALVO COM SUCESSO!!!')
    print ("\n" * 5)
  elif op == 2:
    nome = input('Digite o nome para alterar: ').upper()
    editarContato(agenda, nome)
  elif op == 3:
    listarAll(agenda)
  elif op == 4:
    nome = input('Digite o nome para a pesquisa: ').upper()
    listarNome(agenda, nome)
  elif op == 5:
    nome = input('Digite o nome para a excluir: ').upper()
    print(deletarNome(agenda, nome))
  elif op == 6:
    break
  else:
    print('Digite a opção correta!')

print('Obrigado por usar a agenda!!!')
print('~'*30)
