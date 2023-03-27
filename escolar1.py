class Matricula():
    def __init__(self,nome,idade,serie,sala):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.sala = sala
        self.visualizar()

    def visualizar(self):
        return f'{self.nome} cadastrado com sucesso!'





#####MAIN####

print('-' *20)
print('SISTEMA ESCOLAR'.center(20))
print('-' *20)

lista_alunos = list()
dic_alunos = dict()

while True:
    print('Deseja cadastrar um aluno? \nDigite 1 para cadastrar um novo aluno \nDigite 2 para visualizar os alunos cadastrados')
    opcao = int(input('Qual sua opção? '))
    while True:
        if opcao == 1:
            nome = input('Digite o nome do aluno: ')
            idade = int(input(f'Digite a idade do {nome}: '))
            serie = input('Digite a série (1, 2 ou 3): ')
            sala = input('Digite a sala (A, B ou C): ')
            lista_alunos.append(idade)
            lista_alunos.append(serie)
            lista_alunos.append(sala)
            dic_alunos[nome] = lista_alunos.copy()
            lista_alunos.clear()
            break
    opcao = input('Deseja voltar ao menu? [S/N]: ').upper().strip()
    if opcao in 'N':
        break

Matricula(nome,idade,serie,sala)
print(Matricula.visualizar(nome))






