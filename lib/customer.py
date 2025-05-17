class Customer:
    all_customers = [] #will store the list of all customers

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
       if type(value) is str and 1 <= len(value) <= 15:
           self._name = value 
       else:
           raise ValueError("Name must be a string and betweeon 1 to 15 characters")
       
    def orders(self):
        from order import Order #importing the order from orders file

        return [order for order in Order.all_orders if order.customer == self]
    
    def coffee(self):
        return list({order.coffee for order in self.orders()}) # return the set of unique coffees
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price) #Composition
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        highest_customer = None
        highest_spend = 0

        for customer in cls.all_customers: # loop through the list of customers 
            total_spent = 0

            for order in Order.all_orders: # loop through list of all orders
                if order.customer == customer and order.coffee == coffee: # if 
                    total_spent += order.price
            
            if total_spent > highest_spend:
                highest_spend = total_spent
                highest_customer = customer

        return highest_customer if highest_spend > 0 else None

