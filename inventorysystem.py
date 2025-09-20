
class Product:  
    inventory_list = []
    product_count = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
       #self.product_count += 1
    

    @classmethod
    def add_product(cls, name, category, price, supplier, quantity):
        cls.product_count += 1
        addprod = Product(cls.product_count, name, category, price, supplier, quantity)
        cls.inventory_list.append(addprod)
        return "Product added successfully."
    
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory_list:
            if product.product_id == product_id:
                cls.inventory_list.remove(product)
                return "Product deleted successfully."
        return "Product not found."
    
    @classmethod
    def update_product(cls, product_id, quantity, price):
        for product in cls.inventory_list:
            if product.product_id == product_id:
                product.quantity = quantity
                product.price = price
                return "Product updated successfully."
        return "Product not found."
    
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory_list:
            if product.product_id == product_id:
                cls.inventory_list.remove(product)
                return "Product deleted successfully."
        return "Product not found."
    
    @classmethod
    def view_inventory(cls):
        available = []
        for product in cls.inventory_list:
            avail = {
                "Product ID": product.product_id,
                "Name": product.name,
                "Category": product.category,
                "Quantity": product.quantity,
                "Price": product.price,
                "Supplier": product.supplier,
            }
            available.append(avail)
        return available
    
class Order:
   def place_order(order_id, product_id, quantity):
         for product in Product.inventory_list:
              if product.product_id == product_id:
                if product.quantity >= quantity:
                     product.quantity -= quantity
                     return f"Order {order_id} placed successfully."
                else:
                     return "Insufficient stock."
         return "Product not found."



# OUTPUTS
pr1 = Product.add_product("Laptop", "Electronics", 10, 999.99, "TechSupplier")
pr2 = Product.add_product("Smartphone", "Electronics", 20, 699.99, "MobileWorld")
pr3 = Product.add_product("Headphones", "Electronics", 15, 199.99, "SoundCorp")
pr4 = Product.add_product("Monitor", "Electronics", 8, 299.99, "DisplayTech")
upd = Product.update_product(1, 15, 949.99)
dlt = Product.delete_product(1)
view = Product.view_inventory()
order1 = Order.place_order(2, 2, 2)

#PRINTS OF OUTPUTS
print(pr1)
print(pr2)
print(pr3)
print(pr4)
print(upd)
print(dlt)
print(view)
print(order1)



