'''
Agenda simples
'''
__author__ = 'Gustavo Costa'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from controller import Controller

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
    agenda.append(Controller.inserir(nome, telefone, cidade, estado, status))
    print ("\n" * 5)
    print('CONTATO SALVO COM SUCESSO!!!')
    print ("\n" * 5)
  elif op == 2:
    nome = input('Digite o nome para a pesquisa: ').upper()
    Controller.listarNome(agenda, nome)
  elif op == 3:
    Controller.listarAll(agenda)
  elif op == 4:
    nome = input('Digite o nome para a pesquisa: ').upper()
    Controller.listarNome(agenda, nome)
  elif op == 5:
    nome = input('Digite o nome para a excluir: ').upper()
    print(Controller.deletarNome(agenda, nome))
  elif op == 6:
    break
  else:
    print('Digite a opção correta!')

print('Obrigado por usar a agenda!!!')
print('~'*30)
