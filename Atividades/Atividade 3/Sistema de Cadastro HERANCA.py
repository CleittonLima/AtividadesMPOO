class Aluno():
    def __init__(self, id, nome, curso, endereco):
        self.id = id
        self.nome = nome
        self.curso = curso
        self.endereco = endereco

class Curso(Aluno):
    def __init__(self, id, nome):
        super().__init__(id, nome, None, None)

class Endereco():
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Disciplina(Aluno):
    def __init__(self, id, nome, professor, sala):
        super().__init__(id, nome, None, None)
        self.professor = professor
        self.sala = sala

class Professor(Aluno):
    def __init__(self, id, nome, endereco):
        super().__init__(id, nome, None, endereco)

class Sala():
    def __init__(self, numero, capacidade, disciplina = None):
        self.numero = numero
        self.capacidade = capacidade
        self.disciplina = disciplina

class Servidor(Aluno):
    def __init__(self, id, nome, cargo, departamento):
        super().__init__(id, nome, None, None)
        self.cargo = cargo
        self.departamento = departamento

class Diretor(Aluno):
    def __init__(self, id, nome, setor):
        super().__init__(id, nome, None, None)
        self.setor = setor

class Coordenador(Aluno):
    def __init__(self, id, nome, cordenador_qual_curso):
        super().__init__(id, nome, None, None)
        self.coordenador_qual_cursos = cordenador_qual_curso


curso1 = Curso(1, "Sistemas de Informação")
endereco1 = Endereco("Rua Fulano de Tal", 101, "Serra Talhada", "Pernambuco", "12345-678")
endereco2 = Endereco("Rua ABC", 123, "Triunfo", "Pernambuco", "87654-321")
sala1 = Sala(12, 40)
professor1 = Professor(2, "Prof. Maria Cicera", endereco2)
disciplina1 = Disciplina(3, "MPOO", professor1, sala1)
aluno1 = Aluno(1, "Jonas", curso1, endereco1)
servidor1 = Servidor(4, "Micaele", "Secretária", "Recursos Humanos")
diretor1 = Diretor(5, "Kaline", "Departamento de TI")
coordenador1 = Coordenador(6, "Cleiton", "Sistemas de Informação")

print("=======<> ABA ALUNO <>=======")
print("Aluno (a):", aluno1.nome, "|  ID:", aluno1.id, "|", "| Curso:", curso1.nome, "| Endereço:", aluno1.endereco.rua, ",", aluno1.endereco.cidade, ",", aluno1.endereco.estado)
print()
print("=======<> ABA PROFESSOR <>=======")
print("Professor (a):", professor1.nome, "|  ID:", professor1.id, "|",  "| Endereço:", endereco2.rua, ",", endereco2.cidade, ",", endereco2.estado)
print()
print("=======<> ABA DISCIPLINA <>=======")
print("Disciplina:", disciplina1.nome,"|  ID:", disciplina1.id, "|", "| Professor:", disciplina1.professor.nome, "| Sala:", disciplina1.sala.numero)
print()
print("=======<> ABA SERVIDOR <>=======")
print("Servidor (a):", servidor1.nome, "|  ID:", servidor1.id, "|", "Cargo:", servidor1.cargo, "|", "Departamento:", servidor1.departamento)
print()
print("=======<> ABA DIRETOR <>=======")
print("Diretor (a):", diretor1.nome, "|  ID:", diretor1.id, "|", "Setor:", diretor1.setor)
print()
print("=======<> ABA COORDENADOR <>=======")
print("Coordenador (a):", coordenador1.nome, "|  ID:", coordenador1.id, "|", "Coordenador (a) do Curso:", coordenador1.coordenador_qual_cursos)