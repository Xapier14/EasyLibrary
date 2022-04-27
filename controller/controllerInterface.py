from abc import abstractmethod


class ControllerInterface:
    @abstractmethod
    def __init__(self, view):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def InitializeComponents():
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def EventLoop(event, values, model):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def Show(self, model):
        raise NotImplementedError("Subclass must implement abstract method")