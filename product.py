
class Product:
    product_list = []
    def __init__(self, id, name, desc, price, user_id):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.user_id = user_id
    
    @classmethod
    def add_product(cls, name, desc, price, user_id):
        id = len(cls.product_list)
        cls.product_list.append(Product(id, name, desc, price, user_id))
        return id
    
    @classmethod
    def search(cls, name):
        pass

