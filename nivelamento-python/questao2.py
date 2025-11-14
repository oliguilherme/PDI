import os
os.system("clear")

class Parcel:
    def __init__(self, weight):
        self.__weight = self.set_weight(weight)
        self.__tier = self.__set_tier(weight)
        self.__shipping = self.__calculate_shipping(weight, self.get_tier())

    def __calculate_shipping(self, w, t):
        if (t == 1):
            return 12.50
        elif (t == 2):
            return 20.00
        elif (t == 3):
            return 35.00
        elif (t == 4):
            diff = w - 15
            return 35 + (3 * diff)
    
    def get_weight(self):
        return self.__weight
    
    def set_weight(self, w):
        if (w <= 0):
            print("Erro! Peso não pode ser 0 ou negativo!")
            return
        else:
            return w
            
    def get_tier(self):
        return self.__tier
    
    def __set_tier(self, w):
        if (w <= 1):
            return 1
        elif (w <= 5):
            return 2
        elif (w<= 15):
            return 3
        else:
            return 4
    
    def get_shipping(self):
        return self.__shipping


weight = float(input("Digite o peso: "))
parcel1 = Parcel(weight)

print(f"Peso: {parcel1.get_weight()}")
print(f"Faixa: {parcel1.get_tier()}")
print(f"Frete: {parcel1.get_shipping()}")


        


    
        
    



