class Coffee:
    all_coffees =[]

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is str and  len(value) >= 3:
           self._name = value 
        else:
           raise ValueError("Coffee name must contain atleast 3 characters")
        

    def orders(self): # relationship
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self): #relationship
        for order in self.orders():
            return list({order.customer})
        
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            return total / len(orders)
        return 0.0