class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        print("Deleting price!")
        del self._price 
# Usage
product = Product(5000)
print("Before - product.name: ",product._price)

product._price =1000  # Works
print("After  - product._price: ",product._price)  # Output: Charlie

del product.price