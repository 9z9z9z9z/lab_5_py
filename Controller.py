from Equipment import *
from Food import *
import pickle


def input_int(mes = None) -> int:
    while True:
        try:
            print(mes)
            return int(input("\nInput integer number:\t"))
        except TypeError:
            print("Incorrect input")
            raise TypeError
        except ValueError:
            raise ValueError
            print("Incorrect input")


def input_float(mes = None) -> float:
    while True:
        print(mes)
        try:
            return float(input("Input fractional number:\t"))
        except TypeError:
            print("Incorrect input")
            raise TypeError
        except ValueError:
            print("Incorrect input")
            raise ValueError


def input_Eq(mes = None) -> Equipment:
    name = input("Input name of equipment:\t")
    price = input_int("Input price:\t")
    type = input("Input type:\t")
    flag = True
    weight = 0
    width = 0
    depth = 0
    while flag:
        tmp = input("Input:\tweight/width/depth:\n").split("/")
        try:
            weight = int(tmp[0])
            width = int(tmp[1])
            depth = int(tmp[2])
            flag = False
        except Exception:
            flag = True
    return Equipment(name, price, type, weight, width, depth)


def input_Food(mes = None) -> Food:
    name = input("Input name of product:\t")
    price = input_int("Input price:\t")
    tmp = input("Input data of creating (xx.xx.xxxx:\t").split('.')
    data = (int(tmp[0]), int(tmp[1]), int(tmp[2]))
    storage_data = input_int("Input storage data:\t")
    weight = 0
    width = 0
    depth = 0
    flag = True
    while flag:
        tmp = input("Input:\t weight/width/depth\n").split("/")
        try:
            weight = int(tmp[0])
            width = int(tmp[1])
            depth = int(tmp[2])
            flag = False
        except Exception:
            flag = True
    return Food(name, price, data, storage_data, weight, width, depth)


def save(path, base) -> None:
    try:
        with open(path, "wb") as file:
            for item in base:
                pickle.dump(item, file)
    except IOError:
        print("\nIOError.\nThere are no save file.")
    except TypeError:
        print("\nTypeError.\nInvalid value.")
    except Exception:
        print("\nSomething went wrong...\n")


def load(path) -> list:
    global name, price, type, brand, data, storage_data
    base = []
    try:
        with open(path, "rb") as file:
            l = pickle.load(file)
            base.append(l)
            while True:
                l = pickle.load(file)
                base.append(l)
    except EOFError:
        return base
    except IOError:
        print("\nThere are no save files in such directory\n.")
        raise IOError

