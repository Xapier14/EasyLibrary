# ViewInterface
#   Defines needed functionality for View implementations
from abc import abstractmethod

class ViewInterface:
    @abstractmethod
    def ConstructLayout(self, model):
        raise NotImplementedError("Subclass must implement abstract method")
    def Update(self, model):
        raise NotImplementedError("Subclass must implement abstract method")