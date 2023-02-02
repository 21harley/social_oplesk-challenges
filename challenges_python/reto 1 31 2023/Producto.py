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