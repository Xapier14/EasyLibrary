from abc import abstractmethod

class ViewInterface:
    @abstractmethod
    def ConstructLayout(self, model):
        raise NotImplementedError("Subclass must implement abstract method")