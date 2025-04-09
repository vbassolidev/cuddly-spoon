from time import sleep
class Experimento:
    def __init__(self, nome, complexidade):
        self.nome = nome
        self.complexidade = complexidade

    def __repr__(self):
        return f"{self.nome} (Complexidade: {self.complexidade})"

class Agenda:
    def __init__(self):
        self.experimentos = []

    def adicionar_experimento(self, nome, complexidade):
        novo_experimento = Experimento(nome, complexidade)
        self.inserir_na_lista(novo_experimento, 0)

    def inserir_na_lista(self, experimento, posicao):
        if posicao == len(self.experimentos) or self.experimentos[posicao].complexidade > experimento.complexidade:
            self.experimentos += [None]
            i = len(self.experimentos) - 1
            while i > posicao:
                self.experimentos[i] = self.experimentos[i - 1]
                i -= 1
            self.experimentos[posicao] = experimento
        else:
            self.inserir_na_lista(experimento, posicao + 1)

    def remover_experimento(self, nome):
        for i, exp in enumerate(self.experimentos):
            if exp.nome == nome:
                del self.experimentos[i]
                print(f"Experimento '{nome}' removido com sucesso!")
                return
        print(f"Experimento '{nome}' não encontrado!")

    def buscar_experimento(self, complexidade_minima):
        resultados = [exp for exp in self.experimentos if exp.complexidade >= complexidade_minima]
        return resultados

    def exibir_agenda(self):
        if not self.experimentos:
            print("Nenhum experimento agendado.")
        else:
            for exp in self.experimentos:
                print(exp)

def carregar_experimentos_de_arquivo(nome_arquivo, agenda):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(',')
                    if len(partes) == 2:
                        nome = partes[0].strip()
                        complexidade = int(partes[1].strip())
                        agenda.adicionar_experimento(nome, complexidade)
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado. Nenhum experimento foi carregado.")


def menu():
    agenda = Agenda()

    carregar_experimentos_de_arquivo("experimentos.txt", agenda)

    while True:
        print("\n#############################################\n")
        print("       Menu de Agenda do Cientista Maluco        \n")
        print("1. Adicionar novo experimento")
        print("2. Remover experimento")
        print("3. Buscar experimentos por complexidade")
        print("4. Exibir agenda")
        print("5. Sair")
        print("\n#############################################\n")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            nome = input("Nome do experimento: ")
            complexidade = int(input("Complexidade do experimento (1 a 10): "))
            if complexidade > 10 or complexidade < 1:
                print("\n\n###################################\n")
                print("   Digite um valor entre 1 e 10\n")
                print("###################################")
            else:        
                agenda.adicionar_experimento(nome, complexidade)
                print(f"Experimento '{nome}' adicionado com sucesso!")

        elif opcao == '2':
            print("####################################\n")
            nome = input("Nome do experimento a ser removido: ")
            agenda.remover_experimento(nome)

        elif opcao == '3':
            complexidade_minima = int(input("Digite a complexidade mínima: "))
            resultados = agenda.buscar_experimento(complexidade_minima)
            if resultados:
                print("####################################\n")
                print("\nExperimentos encontrados:")
                for exp in resultados:
                    print(exp)
            else:
                print("Nenhum experimento encontrado com a complexidade mínima especificada.")

        elif opcao == '4':
            print("\n#############################################")
            print("\n           Agenda de experimentos:            \n")
            agenda.exibir_agenda()

        elif opcao == '5':
            print("Saindo...")
            sleep(1.5)
            print("Agenda encerrada!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()