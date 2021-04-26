from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, implementation):
        if not isinstance(implementation, Caracteristicas):
            raise TypeError(
                "O parâmetro implementation precisa ser um objeto da classe Caracteristicas")
        self.implementation = implementation

    @abstractmethod
    def operation(self):
        pass


class CocaCola(Produto):
    def operation(self):
        return (f"CocaCola tamanho:"
                f"{self.implementation.operation_implementation()}")


class Pepsi(Produto):
    def operation(self):
        return (f"Pepsi tamanho:"
                f"{self.implementation.operation_implementation()}")


class Fanta(Produto):
    def operation(self):
        return (f"Fanta tamanho:"
                f"{self.implementation.operation_implementation()}")


class Dolly(Produto):
    def operation(self):
        return (f"Dolly tamanho:"
                f"{self.implementation.operation_implementation()}")