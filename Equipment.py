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
        return "Equipment\n" + self.name + "\n" + self.__brand + '\n' + str(self.price) + "\n" + self.__type \
               + "\n" + str(self.volume)

    def __str__(self):
        return "\n====================================\nName:\t" + self.name + "\nPrice:\t" + str(self.price) + \
               "\nBrand:\t" + self.__brand +"\nType:\t" + self.__type + "\nDimensions:\t" + str(self.volume) + \
               "\n====================================\n"
