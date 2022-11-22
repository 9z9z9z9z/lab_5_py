from Product import Product


class Equipment(Product):
    def __init__(self, name, price, brand, type, weight, width=1, depth=1):
        super(Equipment, self).__init__(name, price, weight, width, depth)
        self.__type = type
        self.__brand = brand

    @property
    def type(self): return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def brand(self): return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    def to_string(self):
        return "Equipment\n" + str(self.name) + "\n" + str(self.__brand) + '\n' + str(self.price) + "\n" + str(self.__type) \
               + "\n" + str(self.volume)

    def __str__(self):
        ret = "\n====================================\nName:\t" + str(self.name) + "\nPrice:\t" + str(self.price) + \
               "\nBrand:\t" + str(self.__brand) +"\nType:\t" + str(self.__type) + "\nDimensions:\t" + str(self.volume) + \
               "\n====================================\n"
        return ret
