import pickle
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

    def __eq__(self, other):
        return isinstance(other, Quarto) and self.numero == other.numero

class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.reservas = []
        self.compras = []
    
    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)
    
    def remover_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
    
    def adicionar_compra(self, item):
        self.compras.append(item)
    
    def __eq__(self, other):
        return isinstance(other, Cliente) and self.id == other.id

class Reserva:
    def __init__(self, quarto, cliente, check_in, check_out):
        self.quarto = quarto
        self.cliente = cliente
        self.check_in = check_in
        self.check_out = check_out

    def __eq__(self, other):
        return (isinstance(other, Reserva) and
                self.quarto == other.quarto and
                self.cliente == other.cliente and
                self.check_in == other.check_in and
                self.check_out == other.check_out)

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Hotel:
    def __init__(self):
        self.quartos = self.carregar_dados('quartos.pkl')
        self.clientes = self.carregar_dados('clientes.pkl')
        self.reservas = self.carregar_dados('reservas.pkl')
        self.itens = self.carregar_dados('itens.pkl')

    def salvar_dados(self, dados, arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(dados, f)
    
    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
        self.salvar_dados(self.quartos, 'quartos.pkl')
        print(f"Quarto {quarto.numero} adicionado com sucesso.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.salvar_dados(self.clientes, 'clientes.pkl')
        print(f"Cliente {cliente.nome} registrado com sucesso.")

    def remover_quarto(self, numero):
        quarto = next((q for q in self.quartos if q.numero == numero), None)
        if quarto:
            if not any(reserva.quarto == quarto for reserva in self.reservas):
                self.quartos.remove(quarto)
                self.salvar_dados(self.quartos, 'quartos.pkl')
                print(f"Quarto {numero} removido com sucesso.")
            else:
                print(f"Quarto {numero} não pode ser removido porque está reservado.")
        else:
            print("Quarto não encontrado.")

    def editar_quarto(self, numero):
        quarto = next((q for q in self.quartos if q.numero == numero), None)
        if quarto:
            novo_tipo = input(f"Novo tipo (atual: {quarto.tipo}): ")
            novo_preco = float(input(f"Novo preço (atual: {quarto.preco}): "))
            quarto.tipo = novo_tipo
            quarto.preco = novo_preco
            self.salvar_dados(self.quartos, 'quartos.pkl')
            print(f"Quarto {numero} editado com sucesso.")
        else:
            print("Quarto não encontrado.")
    
    def cancelar_reserva(self, cliente_id, quarto_numero):
        cliente = next((c for c in self.clientes if c.id == cliente_id), None)
        quarto = next((q for q in self.quartos if q.numero == quarto_numero), None)
        
        if cliente and quarto:
            reserva = next((r for r in self.reservas if r.cliente == cliente and r.quarto == quarto), None)
            if reserva:
                cliente.remover_reserva(reserva)
                quarto.quarto_disponivel()
                self.reservas.remove(reserva)
                self.salvar_dados(self.clientes, 'clientes.pkl')
                self.salvar_dados(self.quartos, 'quartos.pkl')
                self.salvar_dados(self.reservas, 'reservas.pkl')
                print(f"Reserva para o quarto {quarto.numero} cancelada com sucesso.")
            else:
                print("Reserva não encontrada ou quarto já disponível.")
        else:
            print("Cliente ou quarto não encontrado.")
    
    def fazer_reserva(self, cliente_id, quarto_numero, check_in, check_out):
        cliente = next((c for c in self.clientes if c.id == cliente_id), None)
        quarto = next((q for q in self.quartos if q.numero == quarto_numero and q.status_quarto), None)

        if cliente and quarto:
            reserva = Reserva(quarto, cliente, check_in, check_out)
            cliente.adicionar_reserva(reserva)
            quarto.quarto_indisponivel()
            self.reservas.append(reserva)
            self.salvar_dados(self.clientes, 'clientes.pkl')
            self.salvar_dados(self.quartos, 'quartos.pkl')
            self.salvar_dados(self.reservas, 'reservas.pkl')
            print(f"Reserva feita com sucesso para {cliente.nome} no quarto {quarto.numero}")
        else:
            print("Reserva não pode ser feita. Cliente ou quarto não encontrado/disponível.")

    def adicionar_item(self, item):
        self.itens.append(item)
        self.salvar_dados(self.itens, 'itens.pkl')
        print(f"Item {item.nome} adicionado com sucesso.")
    
    def comprar_item(self, cliente_id, item_nome):
        cliente = next((c for c in self.clientes if c.id == cliente_id), None)
        item = next((i for i in self.itens if i.nome == item_nome), None)
        
        if cliente and item:
            cliente.adicionar_compra(item)
            self.salvar_dados(self.clientes, 'clientes.pkl')
            print(f"Compra de {item.nome} registrada para {cliente.nome}.")
        else:
            print("Cliente ou item não encontrado.")
    
    def exibir_dados(self):
        print("\n>>>> Dados do Hotel <<<<\n")
        print("Quartos:")
        for quarto in self.quartos:
            status = "Disponível" if quarto.status_quarto else "Indisponível"
            print(f"Número: {quarto.numero}, Tipo: {quarto.tipo}, Preço: {quarto.preco}, Status: {status}")
        
        print("\nClientes:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}, ID: {cliente.id}")
            print("Reservas:")
            for reserva in cliente.reservas:
                print(f"  Quarto {reserva.quarto.numero}, Check-in: {reserva.check_in}, Check-out: {reserva.check_out}")
            print("Compras:")
            for compra in cliente.compras:
                print(f"  Item: {compra.nome}, Preço: {compra.preco}")
        print("\n")


def menu():
    hotel = Hotel()

    while True:
        print("\n>>>>>>> MENU HOTEL <<<<<<<\n")
        print("1- Adicionar Quarto")
        print("2- Registrar Cliente")
        print("3- Fazer Reserva")
        print("4- Cancelar Reserva")
        print("5- Remover Quarto")
        print("6- Editar Quarto")
        print("7- Adicionar Item")
        print("8- Comprar Item")
        print("9- Exibir Dados do Hotel")
        print("10- Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            numero = int(input("Número do quarto: "))
            tipo = input("Tipo do quarto (ex: solteiro, duplo, suite): ")
            preco = float(input("Preço do quarto: "))
            quarto = Quarto(numero, tipo, preco)
            hotel.adicionar_quarto(quarto)

        elif opcao == "2":
            nome = input("Nome do cliente: ")
            id = int(input("ID do cliente: "))
            cliente = Cliente(nome, id)
            hotel.registrar_cliente(cliente)

        elif opcao == "3":
            cliente_id = int(input("ID do cliente: "))
            quarto_numero = int(input("Número do quarto: "))
            check_in = date.fromisoformat(input("Data de check-in (YYYY-MM-DD): "))
            check_out = date.fromisoformat(input("Data de check-out (YYYY-MM-DD): "))
            hotel.fazer_reserva(cliente_id, quarto_numero, check_in, check_out)

        elif opcao == "4":
            cliente_id = int(input("ID do cliente: "))
            quarto_numero = int(input("Número do quarto: "))
            hotel.cancelar_reserva(cliente_id, quarto_numero)

        elif opcao == "5":
            numero = int(input("Número do quarto a remover: "))
            hotel.remover_quarto(numero)

        elif opcao == "6":
            numero = int(input("Número do quarto a editar: "))
            hotel.editar_quarto(numero)

        elif opcao == "7":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            item = Item(nome, preco)
            hotel.adicionar_item(item)

        elif opcao == "8":
            cliente_id = int(input("ID do cliente: "))
            print("\nItens disponíveis para compra:")
            for item in hotel.itens:
                print(f"Nome: {item.nome}, Preço: {item.preco}")
            item_nome = input("Nome do item a comprar: ")
            hotel.comprar_item(cliente_id, item_nome)

        elif opcao == "9":
            hotel.exibir_dados()

        elif opcao == "10":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

menu()