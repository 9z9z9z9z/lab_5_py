from Controller import *


SAVE_PATH = "save.dat"

base = [Equipment("Skies", 300, "SportMaster", "Sport_Equipment", 300, 20, 5),
        Equipment("Tanks", 3000, "Almaz", "War_Equipment", 30000, 2000, 500),
        Food("Chicken", 120, (5, 11, 2022), 10, 15, 10, 5)]

print((base[0] + base[2]).count(1000000, 1, 1))
print(base[2])

base.append(input_Eq("Input tank"))


save(SAVE_PATH, base)
tmp = load(SAVE_PATH)
print("End")
