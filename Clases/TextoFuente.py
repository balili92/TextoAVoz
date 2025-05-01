from abc import ABC,abstractmethod

class TextoFuente(ABC):

    def __init__(self,texto):
        super().__init__()
        self.texto = texto

    @abstractmethod
    def obtener_texto():
        pass

