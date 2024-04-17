class Aluno():
    def __init__(self, id, nome, curso, endereco):
        self.id = id
        self.nome = nome
        self.curso = curso
        self.endereco = endereco

class Curso():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Endereco():
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Disciplina():
    def __init__(self, id, nome, professor, sala):
        self.id = id
        self.nome = nome
        self.professor = professor
        self.sala = sala

class Professor():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Sala():
    def __init__(self, numero, capacidade, disciplina = None):
        self.numero = numero
        self.capacidade = capacidade
        self.disciplina = disciplina

curso1 = Curso(1, "Sistemas de Informação")
endereco1 = Endereco("Rua Fulano de Tal", 101, "Serra Talhada", "Pernambuco", "12345-678")
endereco2 = Endereco("Rua ABC", 123, "Triunfo", "Pernambuco", "87654-321")
professor1 = Professor(1, "Prof. Erisvaldo")
sala1 = Sala(12, 40)
disciplina1 = Disciplina(1, "MPOO", professor1, sala1)
aluno1 = Aluno(1, "Cleiton", curso1, endereco1)

print("=======<> ABA ALUNO <>=======")
print("Aluno:", aluno1.nome, "| Curso:", curso1.nome, "| Endereço:", aluno1.endereco.rua, ",", aluno1.endereco.cidade, ",", aluno1.endereco.estado)
print()
print("=======<> ABA PROFESSOR <>=======")
print("Professor:", professor1.nome, "| Endereço:", endereco2.rua, ",", endereco2.cidade, ",", endereco2.estado)
print()
print("=======<> ABA DISCIPLINA <>=======")
print("Disciplina:", disciplina1.nome, "| Professor", disciplina1.professor.nome, "| Sala:", disciplina1.sala.numero)