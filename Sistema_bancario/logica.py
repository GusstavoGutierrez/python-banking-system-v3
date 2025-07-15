from datetime import datetime, date
from abc import ABC, abstractmethod

LIMITE_SAQUES_DIARIOS = 3
LIMITE_TRANSACOES_DIA = 10
AGENCIA_PADRAO = "0001"

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar(self):
        print("\n================ EXTRATO ================\n")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in self.transacoes:
                print(t)
        print("==========================================\n")

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {self.valor:.2f}"

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if (
            self.valor > 0 and
            self.valor <= conta.saldo and
            self.valor <= conta.limite_por_saque and
            conta.numero_saques_diarios < LIMITE_SAQUES_DIARIOS
        ):
            conta.saldo -= self.valor
            conta.numero_saques_diarios += 1
            conta.historico.adicionar_transacao(self)
            return True
        return False

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {self.valor:.2f}"

class Conta:
    def __init__(self, cliente, numero):
        self.agencia = AGENCIA_PADRAO
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.numero_saques_diarios = 0
        self.data_ultima_transacao = None
        self.transacoes_hoje = 0
        self.limite_por_saque = 500.0
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        transacao = Saque(valor)
        return transacao.registrar(self)

    def depositar(self, valor):
        transacao = Deposito(valor)
        return transacao.registrar(self)

    def exibir_extrato(self):
        print(f"\nUsuário: {self.cliente.nome} | Conta: {self.numero}")
        self.historico.mostrar()
        print(f"\nSaldo: R$ {self.saldo:.2f}")

    def resetar_contadores_diarios(self):
        hoje = date.today()
        if self.data_ultima_transacao is None or self.data_ultima_transacao != hoje:
            self.data_ultima_transacao = hoje
            self.transacoes_hoje = 0
            self.numero_saques_diarios = 0

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ").strip()
        if self.filtrar_usuario(cpf):
            print("\nJá existe usuário com esse CPF!")
            return
        nome = input("Informe o nome completo: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
        usuario = Usuario(nome, nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print("\nUsuário criado com sucesso!")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta_usuario(self, usuario):
        numero_conta = len(self.contas) + 1
        conta = Conta(usuario, numero_conta)
        self.contas.append(conta)
        usuario.contas.append(conta)
        print(f"\nConta criada com sucesso! Agência: {conta.agencia} Conta: {conta.numero}")

    def listar_contas_usuario(self, usuario):
        if not usuario.contas:
            print("\nUsuário não possui contas.")
            return
        for conta in usuario.contas:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Titular: {usuario.nome}")

    def selecionar_conta_usuario(self, usuario):
        if not usuario.contas:
            print("\nUsuário não possui contas. Crie uma conta primeiro!")
            return None
        print("\nContas disponíveis:")
        for conta in usuario.contas:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero}")
        try:
            numero = int(input("Digite o número da conta para logar: "))
        except ValueError:
            print("Número inválido.")
            return None
        for conta in usuario.contas:
            if conta.numero == numero:
                print(f"\nConta {numero} logada com sucesso!")
                return conta
        print("Conta não encontrada.")
        return None

def main():
    banco = Banco()
    usuario_logado = None
    conta_logada = None

    MenuUSER = """
[n] Novo usuario
[l] Logar usuario
[s] Sair
=>"""

    menuCONTA = """
[c] Nova conta
[lc] Logar em conta
[l] Listar contas
[v] Voltar
=>"""

    menuACOES = """
[d] Depositar
[s] Sacar
[e] Extrato
[v] Voltar
=>"""

    while True:
        usuario_logado = None
        conta_logada = None
        opcao = input(MenuUSER).strip().lower()

        if opcao == "n":
            banco.criar_usuario()
        elif opcao == "l":
            cpf = input("Informe o CPF do usuário: ").strip()
            usuario = banco.filtrar_usuario(cpf)
            if usuario:
                usuario_logado = usuario
                print(f"\nUsuário {usuario.nome} logado com sucesso!")
                while True:
                    conta_logada = None
                    op_conta = input(menuCONTA).strip().lower()
                    if op_conta == "c":
                        banco.criar_conta_usuario(usuario_logado)
                    elif op_conta == "lc":
                        conta_logada = banco.selecionar_conta_usuario(usuario_logado)
                        if conta_logada:
                            while True:
                                conta_logada.resetar_contadores_diarios()
                                op_acao = input(menuACOES).strip().lower()
                                if op_acao == "d":
                                    if conta_logada.transacoes_hoje >= LIMITE_TRANSACOES_DIA:
                                        print("\nLimite diário de transações atingido!")
                                        continue
                                    try:
                                        valor = float(input("Informe o valor do depósito: ").replace(",", "."))
                                    except ValueError:
                                        print("\nOperação falhou! Valor inválido. Tente novamente.")
                                        continue
                                    if conta_logada.depositar(valor):
                                        conta_logada.transacoes_hoje += 1
                                        conta_logada.data_ultima_transacao = date.today()
                                        print("\nDepósito realizado com sucesso!")
                                    else:
                                        print("\nOperação falhou! O valor informado é inválido (deve ser maior que zero).")
                                elif op_acao == "s":
                                    if conta_logada.transacoes_hoje >= LIMITE_TRANSACOES_DIA:
                                        print("\nLimite diário de transações atingido!")
                                        continue
                                    try:
                                        valor = float(input("Informe o valor do saque: ").replace(",", "."))
                                    except ValueError:
                                        print("\nOperação falhou! Valor inválido. Tente novamente.")
                                        continue
                                    if conta_logada.sacar(valor):
                                        conta_logada.transacoes_hoje += 1
                                        conta_logada.data_ultima_transacao = date.today()
                                        print("\nSaque realizado com sucesso!")
                                    else:
                                        print("\nOperação falhou! Verifique saldo, limite ou número de saques diários.")
                                elif op_acao == "e":
                                    conta_logada.exibir_extrato()
                                elif op_acao == "v":
                                    break
                                else:
                                    print("\nOpção inválida.")
                    elif op_conta == "l":
                        banco.listar_contas_usuario(usuario_logado)
                    elif op_conta == "v":
                        break
                    else:
                        print("\nOpção inválida.")
            else:
                print("\nUsuário não encontrado.")
        elif opcao == "s":
            print("\nObrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()
