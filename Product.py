class Product:
    def __init__(self, name, price, weight, width=1, depth=1):
        self.__name = name
        self.__price = price
        self.__weight = weight
        self.__width = width
        self.__depth = depth
        self.__volume = self.__depth * self.__weight * self.__width

    def discount(self, percent) -> float:
        ans = round((self.price * (100 - percent) / 100), 2)
        if ans == 0:
            self.__price = 0.01
            return 0.01
        else:
            self.__price = ans
            return ans

    def count(self, weight, width=1, depth=1) -> int:
        box = [weight, width, depth]
        box.sort()
        case = [self.__weight, self.__width, self.__depth]
        case.sort()
        if box[0] < case[0] or box[1] < case[1] or box[2] < case[2]:
            return 0
        else:
            return (weight * width * depth) // self.volume

    @property
    def price(self):
        return self.__price

    @property
    def volume(self):
        return self.__volume

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @price.setter
    def price(self, price):
        self.__price = price

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __add__(self, other):
        return Product(self.__name + "\n\t\t" + other.__name, self.__price + other.__price,
                       self.__weight + other.__weight, self.__width + other.__width, self.__depth + other.__depth)

    def __str__(self):
        return "\n====================================\nName:\t" + self.__name + "\nPrice:\t" + str(self.__price) + \
               "\nVolume:\t" + str(self.__volume) + "\n====================================\n"
