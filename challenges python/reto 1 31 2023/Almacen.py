from Producto import Producto

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