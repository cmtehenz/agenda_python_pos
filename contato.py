'''
Agenda simples
'''
__author__ = 'Gustavo Costa'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

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
