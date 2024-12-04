import aluno as a
import turma as t

alunos = []

for dados in [
    ("Fabio", "Teixeira", 8),
    ("Fabiano", "Teixeira", 10),
    ("Melissa", "Teixeira", -1),
]:
    try:
        aluno = a.Aluno(*dados)
        alunos.append(aluno)
    except:
        pass

turmaObject = t.Turma()
turmaObject.cadastrarAlunos(alunos)

turmaObject.mostrarAlunos()
print("*" * 30)
print("Aluno com menor nota:", turmaObject.menorNota.mostrarAluno())
print("Aluno com maior nota:", turmaObject.maiorNota.mostrarAluno())
