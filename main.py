from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)

phone1 = Phone("jscPhoneV10", 500, 5, 1)
print(phone1.cal_total_price())
print(Phone.all)
