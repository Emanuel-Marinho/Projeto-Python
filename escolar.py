class Matricula():
    def __init__(self,nome,idade,serie,sala):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.sala = sala
        self.cadastro()

    def cadastro(self):
        aluno = list()
        self.matricula = dict()
        aluno.append(self.idade)
        aluno.append(self.serie)
        aluno.append(self.sala)
        self.matricula[self.nome] = aluno.copy()
        aluno.clear()


    def visualizar(self):
        for i in self.matricula.keys():
            print(f'{i}: {self.matricula.keys()}')



        

print('-' *20)
print('SISTEMA ESCOLAR'.center(20))
print('-' *20)

cadastro = 0
while True:
    print('Deseja cadastrar um aluno? \nDigite 1 para cadastrar um novo aluno \nDigite 2 para visualizar os alunos cadastrados')
    opcao = int(input('Qual sua opção? '))
    while True:
        if opcao == 1:
            nome = input('Digite o nome do aluno: ')
            idade = int(input(f'Digite a idade do {nome}: '))
            serie = input('Digite a série (1, 2 ou 3): ')
            sala = input('Digite a sala (A, B ou C): ')
            Matricula(nome,idade,serie,sala)
            cadastro += 1

        elif opcao == 2:
            if cadastro == 0:
                print('Nenhum aluno cadastrado ainda')
            else:
                Matricula.visualizar()
        opc1 = input('Deseja fazer um novo cadastro? [S/N]: ').upper().strip()
        if opc1 in 'N':
            break
    opc2 = input('Deseja continuar no sistema? [S/N]: ').upper().strip()
    if opc2 in 'N':
        break


