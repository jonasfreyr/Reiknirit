class Stak:
    def __init__(self):
        self.formerki = "+"
        self.value = 1
        self.x = False
        self.veldi = 1


class Fall:
    def __init__(self, f):
        self.fall = []

        self.make(f)

    def make(self, f):
        s = ""
        fall = []
        for a in f:
            if a in ["+", "-"]:
                fall.append(s)
                s = ""
            s += a

        fall.append(s)
        fall.remove("")

        for a in fall:
            s = Stak()
            x_found = False
            x = False
            if "x" in a:
                x = True
            for b in a:
                if b == "x":
                    x_found = True

                if b in ["-", "+"]:
                    s.formerki = b

                elif b.isdigit() and (x is False or x_found is False):
                    s.value = b

                elif b.isdigit() and (x_found is True):
                    s.veldi = b

            self.fall.append(s)


    def get_fall(self):
        pass

'''
fallF = input("Sláðu inn fall f(x) = ")
fallG = input("Sláðu inn fall g(x) = ")

efrimork = input("Sláðu inn x fyrir efri mörk svæðis: ")
nedrimork = input("Sláðu inn x fyrir neðri mörk svæðis: ")
'''

f = Fall("-x2+5x-3")
f.get_fall()


