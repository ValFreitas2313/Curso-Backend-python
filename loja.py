from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome: str, preco_base: float):
        self.nome = nome
        self.preco_base = preco_base

    def calcular_preco_final(self) -> float:
        pass


class ProdutoFisico(Produto):
    def __init__(self, nome: str, preco_base: float, custo_frete: float):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete

    def calcular_preco_final(self) -> float:
        return self.preco_base + self.custo_frete


class ProdutoDigital(Produto):
    def __init__(self, nome: str, preco_base, taxa_servico):
        super().__init__(nome, preco_base)

        self.taxa_servico = taxa_servico

    def calcular_preco_final(self) -> float:
        return self.preco_base + self.taxa_servico


if __name__ == "__main__":

    carrinho = [ProdutoFisico("Livro python", 50.0, 10.0), ProdutoFisico("Caneta", 30.0, 8.0),
                ProdutoDigital("E-book Java", 40.0, 5.0), ProdutoDigital(" Curso Online c++", 200.0, 20.0)]

    total = 0

    print("Carrinho de Compras:\n")
    for produto in carrinho:
        preco_final = produto.calcular_preco_final()
        print(f"{produto.nome}: R$ {preco_final:.2f}")
        total += preco_final

    print("\nValor Total de Compras: R${:.2f}".format(total))
