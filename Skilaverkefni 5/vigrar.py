import math
class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y):
        # Þinn kóði hér
        self.vec = {"x": x, "y":y}

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        # Þinn kóði hér
        print((self.vec["x"], self.vec["y"]))

    # Fall sem skilar lengd
    def lengd(self):
        # Þinn kóði hér
        l = math.sqrt(math.pow(self.vec["x"], 2) + math.pow(self.vec["y"], 2))
        return round(l, 2)
    # Fall sem skilar hallatölu
    def halli(self):
        # Þinn kóði hér
        
        pass

    # Fall sem skilar þvervigri
    def þvervigur(self):
        # Þinn kóði hér
        pass

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        # Þinn kóði hér
        pass

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        # Þinn kóði hér
        pass

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        pass

# Keyrsluforrit
v1 = Vigur(1,3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: " , end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()
