# ☕ Coffee Shop Domain Model
This project uses Python and Object-Oriented Programming (OOP) to model a coffee shop system. It simulates how customers place orders for different types of coffee, tracks spending, and supports business logic such as identifying top spenders.
---

## 📁 Project Structure
```
coffeeshop_codechallenge/
│
├── lib/
│ ├── customer.py # Customer class logic
│ ├── coffee.py # Coffee class logic
│ ├── order.py # Order class for connecting customers and coffees
│ └── debugger.py # Testing file to manually test interactions
│
└── README.md # Project documentation
```
---
## 🧠 Concepts Covered
- **Composition**: An `Order` is composed of a `Customer` and a `Coffee`
- **Encapsulation**: Getters and setters validate input and protect internal data
- **Class Attributes**: Tracks all customers and orders using class-level lists
- **Many-to-Many Relationships**: Customers and Coffees are connected through Orders
- **Class Methods**: `Customer.most_aficionado(coffee)` identifies the top spender
- **Data Validation**: Ensures name, price, and relationships are always valid

 ---
 ## 👨‍💻 Classes Overview
 ### 🔹 Customer
- `name`: Customer name (1–15 characters)
- `orders()`: All orders made by this customer
- `coffee()`: Unique coffees this customer ordered
- `create_order(coffee, price)`: Create a new order
- `most_aficionado(coffee)`: Class method to find the biggest spender on coffee

 ---
### 🔹 Coffee
- `name`: Coffee name
- `orders()`: All orders for this coffee
- `customers()`: Unique customers who ordered this coffee
- `average_price()`: Average price for all orders of this coffee

---
### 🔹 Order
- `customer`: Instance of `Customer`
- `coffee`: Instance of `Coffee`
- `price`: Float (1.0 to 10.0)
- Class attribute `all_orders` stores all Order instances

---
## 🧪 Testing

Run the `debugger.py` file inside the `lib/` folder to test the model:

```bash
python3 lib/debugger.py
```

## ✍️ Author

Built by [Derick Sheldrick](https://github.com/dericksheldrick) as part of a software engineering learning project.

 
