class Aluno():
    def __init__(self, id, nome, curso, endereço):
        self.id = id
        self.nome = nome
        self.curso = curso
        self.endereço = endereço

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

#FALTA CRIAR INSTÂNCIAS E PRINTAR
#VER SE PRECISA COLOCAR PRIVACIDADES
#REVISAR SE ESTÁ TUDO CERTO