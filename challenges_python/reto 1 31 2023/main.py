class Producto:

    def __init__(self,type_p,size_p,cost_p,product_units):
             self.type_p=type_p
             self.cost_p=cost_p
             self.size_p=size_p
             self.product_units=product_units
             self.type_product=self.type_p+' '+self.size_p
    
    def __str__(self):
        return f'Nombre:{self.type_product} Costo:{self.cost_p} UniPro:{self.product_units}'

    def set_type_p(self,type_p):
        self.type_p=type_p

    def set_cost_p(self,cost_p):
        self.cost_p=cost_p

    def set_size_p(self,size_p):
        self.size_p=size_p

    def set_product_units(self,product_units):
        self.product_units=product_units

    def get_type_p(self):
        return self.type_p

    def get_cost_p(self):
        return self.cost_p

    def get_size_p(self):
        return self.size_p

    def get_product_units(self):
        return self.product_units

    def get_name(self):
        return self.get_type_p()+" "+self.get_size_p()

def add_produt_fn(items,prop):
        ban=0
        for aux in items:
            if aux.type_product == prop.type_product:
                aux.product_units+=prop.product_units
                ban=1
                break

        if ban == 0:
            items.append(prop)

class Almacen:
    def __init__(self,name):
        self.name=name
        self.items=[]
        self.buy_items=[]
    
    def add_produt(self,prop):
        add_produt_fn(self.items,prop)
    

    def buy_product(self,prop):
        for aux in self.items:
            if aux.type_product == prop.type_product:
                if aux.product_units< prop.product_units :
                    print('Error el stock cuenta con con '+aux.product_units)
                    return 0
                else:
                    aux.product_units-=prop.product_units
                    add_produt_fn(self.buy_items, prop)
                    return 1
                break

    def if_buy_product(self,prop):
        for aux in self.items:
            if aux.type_product == prop.type_product:
                if aux.product_units< prop.product_units :
                    return 0
                else:
                    return 1
                break

    def get_item_product(self,num):
        if num>=0 and num < self.log_items():
           return self.items[num]
        else:
            return None

    def delete_product(self,prop):
        for aux in self.items:
            if aux.type_product == prop.type_product:
                self.items.pop(aux)
                break
        return 1

    def log_items(self):
        return self.items.__len__()
    
    def log_item(self,prop):
        for aux in self.items:
            if aux.type_product == prop.type_product:
                return aux.product_units

    def total_buy(self):
        value=0
        for aux in self.items:
            value+=aux.cost_p*aux.product_units
        return value
    
    def print_product_menu(self):
        aux_item=0
        for aux in self.items:
            print(
                '\nNombre producto:'+aux.get_name(),
                '\nTotal de unidades:'+ str(aux.get_product_units()),
                '\nPrecio unitario:'+str(aux.get_cost_p()),
                '\nCodigo de producto:'+str(aux_item),
            )
            aux_item+=1

    def print_product_cost(self):
        for aux in self.items:
            print(
                'Nombre producto:'+aux.get_name(),
                ' Total de unidades:'+ str(aux.get_product_units()),
                ' Precio unitario:'+str(aux.get_cost_p()),
            )
    
    def print_buy_product(self):
        for aux in self.buy_items:
            print(
                'Nombre producto:'+aux.get_name(),
                ' Total de unidades:'+ str(aux.get_product_units()),
                ' Precio unitario:'+str(aux.get_cost_p()),
            )

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

def cargar_menu(almance):
        almance.add_produt(Producto('Burger',"Normal",3,10))
        almance.add_produt(Producto('Burger',"Especial",5,10))
        almance.add_produt(Producto('Burger',"Super Especial",10,10))
        almance.add_produt(Producto('Refresco',"pequeno",1,10))
        almance.add_produt(Producto('Refresco',"grande",3,10))
        almance.add_produt(Producto('Gaseosa',"pequeno",1,10))
        almance.add_produt(Producto('Gaseosa',"grande",3,10))
        almance.add_produt(Producto('Burger',"Normal",3,10))
        almance.add_produt(Producto('Burger',"Especial",5,10))
        almance.add_produt(Producto('Burger',"Super Especial",10,10))

def menu_principal():
    print("\nPor Favor ingrese el numero:")
    print('<1>-Mostrar Menu')
    print('<2>-Pedir orden ')
    print('<3>-Mostrar Resivo')
    print('<4>-Mostrar Consumo')
    print('<5>-Mostrar datos cliente')
    print('<6>-Mostrar Stack del almacen')
    print('<7>-Salir')

def fn_switch(valor,almance,cliente):

    if valor==1:
        almance.print_product_menu()
        return valor

    if valor==2:
        try:
            print("Ingrese producto codigo producto")
            input_cliente_items=int(input())
            print("Ingrese cantidad de producto")
            input_cliente_cant=int(input())
            prop=almance.get_item_product(input_cliente_items)
            #print(almance.get_item_product(input_cliente_items))
            if prop != None:
                aux_prop=Producto(prop.get_type_p(),prop.get_size_p(),prop.get_cost_p(),input_cliente_cant)
                if almance.if_buy_product(aux_prop):
                    if cliente.set_cast(cliente.get_cast()-(prop.get_cost_p()*input_cliente_cant)):
                        almance.buy_product(aux_prop)
                        cliente.add_product(aux_prop)
                        print("Se compro el pedido")
                        cliente.print_Data()
                        cliente.print_Total_cost()
                    else:
                        print('No se puedo comprar el pedido')
            else:
                print("ingreso un codigo no valido")    

        except:
            print("Ingreso mal los datos por favor vuelda a intentar \n")
        return valor

    if valor==3:
        cliente.print_Data()
        cliente.print_Total_cost()
        return valor

    if valor==4:
        print('Consumo de los clientes')
        almance.print_buy_product()
        return valor

    if valor==5:
        print(cliente)
        return valor

    if valor==6:
        almance.print_product_cost()
        return valor

    if valor==7:
        return valor

def carga_cliente(cliente):
    cont=0
    while cont==0 :
        try:
            print("Ingrese su nombre:")
            cliente.set_name(input())
            print("Ingrese su medio de pago")
            cliente.set_type_ps(input())
            print("Ingrese la cantidad de dinero en ese medio de pago")
            cliente.set_cast(float(input()))
            cont+=1
        except:
            print("Ingreso mal los datos por favor vuelda a ingresarlos para poder continuar \n")

def menu():
    almance=Almacen('Nueva Esparta')
    cliente=Cliente('', 0, '')
    cargar_menu(almance)
    input_cliente=0
    print('Bienvenido a la Nueva Esparta por favor ingrese los proximos datos:')
    carga_cliente(cliente)

    while(input_cliente!=7):
        try:
            menu_principal()
            input_cliente=fn_switch(int(input()),almance,cliente)
        except:
            print("Ingreso mal los datos \n")
    return None

if __name__ == "__main__":
   menu()

