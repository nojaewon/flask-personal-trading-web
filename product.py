
class Product:
    id_generator = 0;
    product_list = []
    keyword_list={}
    def __init__(self, id, name, desc, price, keyword, user_id, select_id):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.keyword = keyword
        self.user_id = user_id
        self.selected_id = int(select_id);
    
    @classmethod
    def add_product(cls, name, desc, price, keyword, user_id, selected_id):
        id = cls.id_generator
        cls.id_generator += 1
        if(keyword in cls.keyword_list.keys()):
            cls.keyword_list[keyword].append(id)
            cls.product_list.append(Product(id, name, desc, price, keyword, user_id, selected_id))
        else:
            cls.keyword_list[keyword]=[]
            cls.keyword_list[keyword].append(id)
            cls.product_list.append(Product(id, name, desc, price, keyword, user_id, selected_id))
        return id
    
    @classmethod
    def search(cls, id):
        for product in cls.product_list:
            if id == product.id:
                return product
        return None
    
    @classmethod
    def delete(cls, id):
        for idx, product in enumerate(cls.product_list):
            if id == product.id:
                cls.product_list.pop(idx)

    def __repr__(self):
        return self.name

