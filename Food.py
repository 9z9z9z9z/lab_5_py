import string
from Product import Product


class Food(Product):
    def __init__(self, name, price, data, storage_data, weight, width=1, depth=1):
        super(Food, self).__init__(name, price, weight, width, depth)
        self.__data = data
        self.__storage_data = storage_data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if data < 0:
            raise Exception("Invalid data")
        else:
            self.__data = data

    @property
    def storage_data(self):
        return self.__storage_data

    @storage_data.setter
    def storage_data(self, value):
        if value < 0:
            raise Exception("Invalid data")
        else:
            self.__storage_data = value

    def discount(self, percent) -> float:
        if self.__storage_data < 2:
            ans = round((self.price * (100 - 2 * percent) / 100), 2)
        else:
            ans = round((self.price * (100 - percent) / 100), 2)
        if ans == 0:
            return 0.01
        else:
            return ans

    def to_string(self) -> string:
        tmp = str(self.__data).replace(")", "").replace("(", "").split(", ")
        str_data = ".".join(tmp)
        return "Food\n" + self.name + '\n' + str(self.price) + '\n' + str_data + '\n' + \
               str(self.__storage_data) + '\n' + str(self.volume)

    def __str__(self):
        tmp = str(self.__data).replace(")", "").replace("(", "").split(", ")
        str_data = ".".join(tmp)
        return "\n====================================\nName:\t" + self.name + "\nPrice:\t" + str(self.price) + \
               "\nData:\t" + str_data + "\nStorage data:\t" + str(self.__storage_data) \
               + "\nDimensions:\t" + str(self.volume) + "\n====================================\n"
