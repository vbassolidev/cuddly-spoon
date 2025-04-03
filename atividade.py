class Experimento:
    def __init__(self, nome, complexidade):
        self.nome = nome
        self.complexidade = complexidade

class No:
    def __init__(self, experimento):
        self.experimento = experimento
        self.proximo = None

class ListaLinear:
    def __init__(self):
        self.inicio = None

    def inserir(self, experimento):
        novo_no = No(experimento)
        self.inicio = self._inserir_ordenado_recursivo(self.inicio, novo_no)

    def _inserir_ordenado_recursivo(self, atual, novo_no):
        # Caso base: lista vazia ou encontramos posição de inserção
        if atual is None:
            return novo_no
        elif novo_no.experimento.complexidade < atual.experimento.complexidade:
            novo_no.proximo = atual
            return novo_no
        else:
            atual.proximo = self._inserir_ordenado_recursivo(atual.proximo, novo_no)
            return atual

    def remover(self, nome):
        self.inicio = self._remover_recursivo(self.inicio, nome)

    def _remover_recursivo(self, atual, nome):
        if not atual:
            return None
        if atual.experimento.nome == nome:
            return atual.proximo
        atual.proximo = self._remover_recursivo(atual.proximo, nome)
        return atual

    def buscar_por_complexidade(self, complexidade):
        return self._buscar_recursivo(self.inicio, complexidade)

    def _buscar_recursivo(self, atual, complexidade):
        if not atual:
            return None
        if atual.experimento.complexidade == complexidade:
            return atual.experimento
        return self._buscar_recursivo(atual.proximo, complexidade)

    def exibir_lista(self):
        atual = self.inicio
        print('')
        print('#######################################################')
        print("Lista de Experimentos (ordem crescente de complexidade):")
        while atual:
            print(f"- {atual.experimento.nome} (Complexidade: {atual.experimento.complexidade})")
            atual = atual.proximo
# Interface console
def menu():
    lista = ListaLinear()

    while True:
        print("            MENU (AGENDA DO CIENTISTA MALUCO)")
        print("\n#######################################################")
        print("1. Adicionar experimento")
        print("2. Remover experimento")
        print("3. Buscar por complexidade")
        print("4. Exibir lista")
        print("5. Sair")
        print("#######################################################\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do experimento: ")
            if nome == "":
                print("Preencha com um nome válido!")
            complexidade = 1
            int(input("Complexidade (1 a 10): "))
            exp = Experimento(nome, complexidade)
            lista.inserir(exp)
        elif opcao == "2":
            nome = input("Nome do experimento a remover: ")
            lista.remover(nome)
        elif opcao == "3":
            c = int(input("Complexidade a buscar: "))
            resultado = lista.buscar_por_complexidade(c)
            if resultado:
                print(f"Encontrado: {resultado.nome} (Complexidade: {resultado.complexidade})")
            else:
                print("Experimento não encontrado.")
        elif opcao == "4":
            lista.exibir_lista()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

menu()