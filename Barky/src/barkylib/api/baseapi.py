from abc import ABC, abstractmethod


class AbstractBookMarkAPI(ABC):
    @abstractmethod
    def one(self, id):
        raise NotImplementedError("Derived classes must implement one")

    @abstractmethod
    def first(self, property, value):
        raise NotImplementedError("Derived classes must implement first")

    @abstractmethod
    def many(self, property, value, sort):
        raise NotImplementedError("Derived classes must implement many")

    @abstractmethod
    def add(self, bookmark):
        raise NotImplementedError("Derived classes must implement add")

    @abstractmethod
    def delete(self, bookmark):
        raise NotImplementedError("Derived classes must implement delete")

    @abstractmethod
    def update(self, bookmark):
        raise NotImplementedError("Derived classes must implement update")
