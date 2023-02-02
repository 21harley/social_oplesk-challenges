from Almacen import Almacen

class Cliente():
    def __init__(self,name,cast,type_ps):
        self.__name=name
        self.__cast=cast
        self.__type_ps=type_ps
        self.__cars=Almacen('cars')
    
    def __str__(self):
        return f'Nombre:{self.__name} Dinero:{self.__cast} Medio de pago:{self.__type_ps} Total Items:{self.__cars.log_items()}'

    def add_product(self,prop):
        self.__cars.add_produt(prop)

    def delete_product(self,prop):
        self.__cars.delete_product(prop)
    
    def print_Data(self):
        self.__cars.print_product_cost()

    def print_Total_cost(self):
        print('El total a pagar es:'+str(self.__cars.total_buy()))
    
    def print_name(self):
        print('Nombre cliente:'+self.__name)

    def set_name(self,name):
        self.__name=name

    def set_cast(self,cast):
        if cast > 0:
           self.__cast=cast
           return 1
        else:
           print('El cliente no puede tener saldo negativo')
           return 0

    def set_type_ps(self,type_ps):
        self.__type_ps=type_ps

    def get_name(self,name):
        return self.__name

    def get_cast(self):
        return self.__cast