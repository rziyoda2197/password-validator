import re

class ParolValidatsiya:
    def __init__(self, uzunlik=8, belgilar=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        self.uzunlik = uzunlik
        self.belgilar = belgilar

    def validatsiya(self, parol):
        if len(parol) < self.uzunlik:
            return False
        if not re.search(r"[A-Z]", parol):
            return False
        if not re.search(r"[a-z]", parol):
            return False
        if not re.search(r"[0-9]", parol):
            return False
        if not re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", parol):
            return False
        return True

parol_validatsiya = ParolValidatsiya()
print(parol_validatsiya.validatsiya("Parol123!"))  # True
print(parol_validatsiya.validatsiya("parol123!"))  # False
print(parol_validatsiya.validatsiya("Parol"))  # False
print(parol_validatsiya.validatsiya("Parol123"))  # False
print(parol_validatsiya.validatsiya("Parol123!@#"))  # False
