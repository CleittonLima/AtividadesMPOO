from datetime import date

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.preco = preco
        self.tipo = tipo
        self.status_quarto = True

    def quarto_disponivel(self):
        self.status_quarto = True
    
    def quarto_indisponivel(self):
        self.status_quarto = False


class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.reservas = []
    
    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)


class Reserva:
    def __init__(self, quarto, cliente, check_in, check_out):
        self.quarto = quarto
        self.cliente = cliente
        self.check_in = check_in
        self.check_out = check_out


class Hotel:
    def __init__(self):
        self.quartos = []
        self.clientes = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def fazer_reserva(self, cliente_id, quarto_numero, check_in, check_out):
        cliente = next((c for c in self.clientes if c.id == cliente_id), None)
        quarto = next((q for q in self.quartos if q.numero == quarto_numero and q.status_quarto), None)

        if cliente and quarto:
            reserva = Reserva(quarto, cliente, check_in, check_out)
            cliente.adicionar_reserva(reserva)
            quarto.quarto_indisponivel()
            print(f"Reserva feita com sucesso para {cliente.nome} no quarto {quarto.numero}")
        else:
            print("Reserva não pode ser feita. Cliente ou quarto não encontrado/disponível.")


hotel = Hotel()

hotel.adicionar_quarto(Quarto(101, "solteiro", 150.0))
hotel.adicionar_quarto(Quarto(102, "duplo", 200.0))

cliente1 = Cliente("João Silva", 1)
hotel.registrar_cliente(cliente1)

hotel.fazer_reserva(1, 101, date(2024, 7, 20), date(2024, 7, 25))