from Estudante import Estudante


nome = input("digite o nome: ")
matricula = input("digite a matricula: ")
creditos = int(input("digite a quantidade de creditos: "))

aluno1 = Estudante(nome, matricula, creditos)

aluno1.showNome()
aluno1.showMatricula()

aluno1.showCreditos()
aluno1.addCreditos(120)
aluno1.showCreditos()
