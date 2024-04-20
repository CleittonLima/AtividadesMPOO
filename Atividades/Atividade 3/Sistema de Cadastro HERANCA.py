class Pessoa():
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

class Aluno(Pessoa):
    def __init__(self, id, nome, curso, endereco):
        super(). __init__(id, nome, endereco)
        self.curso = curso

class Curso():
    def __init__(self, id, nomeCurso):
        self.id = id
        self.nomeCurso = nomeCurso

class Endereco():
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Disciplina():
    def __init__(self, id, nomeDisc, professor, sala):
        self.id = id
        self.nomeDisc = nomeDisc
        self.professor = professor
        self.sala = sala

class Professor(Pessoa):
    def __init__(self, id, nome, endereco):
        super().__init__(id, nome, endereco)

class Sala():
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

class Servidor(Pessoa):
    def __init__(self, id, nome, cargo, departamento):
        super().__init__(id, nome, None)
        self.cargo = cargo
        self.departamento = departamento

class Diretor(Pessoa):
    def __init__(self, id, nome, setor):
        super().__init__(id, nome, None)
        self.setor = setor

class Coordenador(Pessoa):
    def __init__(self, id, nome, cordenador_qual_curso):
        super().__init__(id, nome, None)
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
print("| Aluno (a):", aluno1.nome, "|", "\n| ID:", aluno1.id, "|", "\n| Curso:", curso1.nomeCurso, "|", "\n| Endereço:", aluno1.endereco.rua, ",", aluno1.endereco.cidade, ",", aluno1.endereco.estado, ",", aluno1.endereco.cep, "|")
print()
print("=======<> ABA PROFESSOR <>=======")
print("| Professor (a):", professor1.nome, "|", "\n| ID:", professor1.id, "|",  "\n| Endereço:", professor1.endereco.rua, ",", professor1.endereco.cidade, ",", professor1.endereco.estado, ",", professor1.endereco.cep, "|")
print()
print("=======<> ABA DISCIPLINA <>=======")
print("| Disciplina:", disciplina1.nomeDisc, "|","\n| ID:", disciplina1.id, "|", "\n| Professor:", disciplina1.professor.nome, "|", "\n| Sala:", disciplina1.sala.numero, "|")
print()
print("=======<> ABA SERVIDOR <>=======")
print("| Servidor (a):", servidor1.nome, "|", "\n| ID:", servidor1.id, "|", "\n| Cargo:", servidor1.cargo, "|", "\n| Departamento:", servidor1.departamento, "|")
print()
print("=======<> ABA DIRETOR <>=======")
print("| Diretor (a):", diretor1.nome, "|", "\n| ID:", diretor1.id, "|", "\n| Setor:", diretor1.setor, "|")
print()
print("=======<> ABA COORDENADOR <>=======")
print("| Coordenador (a):", coordenador1.nome, "|", "\n| ID:", coordenador1.id, "|", "\n| Coordenador (a) do Curso:", coordenador1.coordenador_qual_cursos, "|")