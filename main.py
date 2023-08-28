# task1
ls = ["Tamerlan", "Selim", "Fazil"]

for i in ls:
    if i == "Selim":
        ls.remove("Selim")
        ls.append("Nihat")

print(ls)


# task2

class Friends:
    def __init__(self, fname, fsurname, fage):
        self.__name = fname
        self.__surname = fsurname
        self.__age = fage

    def GetName(self):
        return self.__name

    def GetSurname(self):
        return self.__surname

    def GetAge(self):
        return self.__age


ls = []
fr1 = Friends("Salim", "Verdiyev", 20)
fr2 = Friends("Mamed", "Mammedov", 16)
fr3 = Friends("Gleb", "Demonov", 15)
ls.append(fr1.GetName())
ls.append(fr2.GetName())
ls.append(fr3.GetName())

name = input("name: ")

for i in ls:
    if name == i:
        print("in list")
        break
    else:
        print("not in list")
