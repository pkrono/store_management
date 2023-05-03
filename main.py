class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity=0):
        
        #Run Validations
        assert price >= 0, f"Price {price} is not greater than or equal to 0!"
        assert quantity >= 0, f"Quantity{quantity} is not greater than or equal to 0!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def cal_total_price(self):
        print(self.name)
        return self.price * self.quantity
    
item1 = Item("phone", 100, 5)

m = item1.cal_total_price()
print(m)

item2 = Item("Laptop", 1000, 3)

print(item2.cal_total_price())