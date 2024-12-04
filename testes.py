import unittest
import aluno as a
import turma as t


class turmaTest(unittest.TestCase):
    def setUp(self):
        print("Teste", self._testMethodName, "sendo executado...")
        self.alunos = []

        try:
            self.alunos.append(a.Aluno("Fabio", "Teixeira", 10))
            self.alunos.append(a.Aluno("Fabiano", "Teixeira", 8))
            self.alunos.append(a.Aluno("Melissa", "Teixeira", 6))
            self.alunos.append(a.Aluno("Angela", "Teixeira", 7))
            self.alunos.append(a.Aluno("Angela", "Teixeira", -1))
        except:
            pass

        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print("Teste", self._testMethodName, "finalizado.")

    def testMaior(self):
        self.assertEqual(
            10, self.turmaObject.maiorNota.nota, "Erro ao encontrar maior nota"
        )

    def testMenor(self):
        self.assertEqual(
            6, self.turmaObject.menorNota.nota, "Erro ao encontrar menor nota"
        )

    def testIntervalo(self):
        print("Testar se o intervalo de notas está correto.")
        for aluno in self.turmaObject.turma:
            self.assertGreaterEqual(
                aluno.nota, 0, f"Nota menor que 0 encontrada para {aluno.nome}."
            )
            self.assertLessEqual(
                aluno.nota, 10, f"Nota maior que 10 encontrada para {aluno.nome}."
            )


if __name__ == "__main__":
    unittest.main()
