from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def made(self):
        pass

class Table(Product):
    name = "Computer table"
    def made(self):
        print("Chinese noname table: "+self.name)

class Chair(Product):
    name = "Simple chair"
    def made(self):
        print("Chinese noname chair: "+self.name)

class TableGrone(Product):
    name = "Table grone"
    def made(self):
        print("Swedish IKEA table: "+self.name)

class ChairRomuald(Product):
    name = "Chair romuald"
    def made(self):
        print("Swedish IKEA chair: "+self.name)

class Factory(ABC):

    @abstractmethod
    def get_furniture(type_of_furniture):
        pass

class ChineseDesignFactory(Factory):
    def get_furniture(type_of_furniture):
        if type_of_furniture == "table":
            return Table()
        if type_of_furniture == "chair":
            return Chair()

    def create_furniture(self):
        return Chair()

class SwedishDesignFactory(Factory):
    def get_furniture(type_of_furniture):
        if type_of_furniture == "table":
            return TableGrone()

        if type_of_furniture == "chair":
            return ChairRomuald()

class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "chinese":
            return ChineseDesignFactory
        if type_of_factory == "swedish":
            return SwedishDesignFactory

if __name__=='__main__':
    fp = FactoryProducer()

    fac = fp.get_factory("chinese")
    table = fac.get_furniture("table")
    table.made()
    chair = fac.get_furniture("chair")
    chair.made()
    print("====================")

    fac2 = fp.get_factory("swedish")
    table = fac2.get_furniture("table")
    table.made()
    chair = fac2.get_furniture("chair")
    chair.made()
