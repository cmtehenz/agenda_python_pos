# Agenda Telefônica em Python 

Agora que você já tem os conhecimentos básicos necessários para desenvolver aplicações em linguagem Python, lhe convido a colocar em prática estes novos conhecimentos. Considere que você está participando de um processo seletivo para uma vaga de desenvolvedor, foi requisitado a você elaborar um pequeno projeto em linguagem Python. O programa requisitado como Prova de Conceitos seria uma versão beta (versão de inicial), onde deveriam ser armazenados os dados de contato de sua agenda.

Para cada registro, deverá ser armazenado as seguintes informações:

Nome;

Telefone;

Cidade;

Estado;

Status (P-> Pessoal) ou (C-> Comercial).

O programa deverá apresentar um menu de opções ao usuário:

1.	Cadastrar Pessoa na Agenda

2.	Alterar dados da Pessoa

3.	Listar Agenda

4.	Procurar pessoa na Agenda 

5.	Excluir Pessoa da Agenda

6.	Sair do sistema



1 – Inserir um novo cadastro:  ao selecionar essa opção, o usuário deverá ser capaz de informar todos os dados do contato para registro;

2 –	Alterar dados da Pessoa:  ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja alterar, caso seja encontrado apresentar os campos para realizar a alteração, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;

3 – Listar Agenda: ao selecionar essa opção, o programa deverá imprimir, na tela, todos os registros, um contato por linha;

4 –	Procurar pessoa na Agenda:  ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja visualizar os dados, caso seja encontrado apresentar os dados do mesmo na tela, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;

5 –	Excluir pessoa da Agenda:  ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja excluir os dados, caso seja encontrado excluir o mesmo e escrever na tela “Cadastro excluído”, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;

6 – Encerrar: o programa deve ser encerrado se, e somente se, o usuário escolher essa opção.

Caso o usuário escolha uma opção que não conste no menu, o programa deverá exibir uma mensagem de erro como, por exemplo, “Erro: opção inválida!”; retornando ao menu logo em seguida.

 

A sua atividade deve ser entregue em um arquivo de código-fonte em linguagem Python (extensão .py).

DICA: Utilizem a estrutura de armazenamento em Lista[]

 

Algumas funções que serão úteis durante o desenvolvimento do programa:

XXXXXX.index(pessoa) #descobri a posição dos dados na lista

XXXXXXXXX.pop(posicao) #remove o cadastro da lista   

XXXXXX.append((DADO1, DADOS2, .......)) #insere o cadastro da lista