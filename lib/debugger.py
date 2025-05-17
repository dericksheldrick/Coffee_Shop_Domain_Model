from customer import Customer
from coffee import Coffee
from order import Order
#customer
cust1 = Customer("Dennis")
cust2 = Customer("Brandon")

#coffee
coffee1 = Coffee("Capuccinno")
coffee2 = Coffee("Mocha")


#order
order1 = Order(cust1, coffee1, 5.5)
order2 = Order(cust1, coffee2, 9.5)
order3 = Order(cust2, coffee2, 3.3)
order4 = Order(cust1, coffee1, 5.5)
order5 = Order(cust1, coffee2, 9.5)

# --------------testing------------------------------

print(cust1.name)
print(coffee1.name)
print(order1.price)
print(order1.coffee.name)
print(order1.customer.name)

print("----checking all coffees ordered today---")
for order in Order.all_orders:
    print(f"{order.coffee.name} \n")

# all orders Dennis made 
print("-----Dennis's order-----------")
for order in cust1.orders():
    print(f"{order.coffee.name} at {order.price} \n")
    


print("-----all coffees Dennis ordered-----------")
for coffee in cust1.coffee():
    print(f"{coffee.name} \n")

print("-----all unique customers who ordered coffee1 ordered-----------")
for cust in coffee1.customers():
    print(f"{cust.name} \n")

print("-----number of times the coffee1 was ordered-----------")
print(f"{coffee1.num_orders()} times \n")

print("-----average price for cofee2-----------")
print(f"Average pric of Coffee2: {coffee2.average_price():.1f}  \n")

print("-----Create a new order-----------")
cust2.create_order(coffee1, 5.6)
print(f"{cust1.name} orders {coffee1.name} for 5.6 \n")

print("-----who spend most on coffee-----------")
highest = Customer.most_aficionado(coffee2)
print(f"{highest.name if highest else 'None'}")