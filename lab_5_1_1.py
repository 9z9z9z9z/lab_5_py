import os.path

from Controller import *


def lab_5_1_1():
    SAVE_PATH = "save.dat"

    if os.path.isfile(SAVE_PATH):
        base = load(SAVE_PATH)
    else:
        base = [Equipment("Skies", -1000, "SportMaster", "Sport_Equipment", 300, 20, 5),
                Equipment("Tanks", 3000, "Almaz", "War_Equipment", 30000, 2000, 500),
                Food("Chicken", 120, (5, 11, 2022), 10, 15, 10, 5)]

    tmp = input_Eq("Input tank:")
    base.append(tmp)

    save(SAVE_PATH, base)
    tmp = load(SAVE_PATH)
    print('\n\n')
    for item in tmp:
        print(item)
    print("End")


lab_5_1_1()
