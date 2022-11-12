#10 - 11 - 2022

class Decimal():
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico
    
    def convertirABinario(self):
        conversion = bin(self.valorNumerico)
        return conversion[2:]

    def convertirAOctal(self):
        conversion = oct(self.valorNumerico)
        return conversion[2:]

    def convertirAHexadecimal(self):
        conversion = hex(self.valorNumerico)
        return conversion[2:]

if __name__ == "__main__":
    decimal1 = Decimal(8)
    decimal2 = Decimal(15)

    print("Decimal 8")
    print(decimal1.convertirABinario())
    print(decimal1.convertirAOctal())
    print(decimal1.convertirAHexadecimal())

    print("Decimal 15")
    print(decimal2.convertirABinario())
    print(decimal2.convertirAOctal())
    print(decimal2.convertirAHexadecimal())

'''
Crear las clases Octal, Hexadecimal y Binario
e incluyan los metodos necesarios para convertir 
a los otros sistemas numericos
'''

class Octal():
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico
    
    def convertirABinario(self):
        conversion1 = int(str(self.valorNumerico), 8)
        conversion2 = bin(conversion1)
        return conversion2[2:]

    def convertirADecimal(self):
        conversion = int(str(self.valorNumerico), 8)
        return conversion

    def convertirAHexadecimal(self):
        conversion1 = int(str(self.valorNumerico), 8)
        conversion2 = hex(conversion1)
        return conversion2[2:]


class Hexadecimal():
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico
    
    def convertirABinario(self):
        conversion1 = int(str(self.valorNumerico), 16)
        conversion2 = bin(conversion1)
        return conversion2[2:]

    def convertirADecimal(self):
        conversion = int(str(self.valorNumerico), 16)
        return conversion

    def convertirAOctal(self):
        conversion1 = int(str(self.valorNumerico), 16)
        conversion2 = oct(conversion1)
        return conversion2[2:]


class Binario():
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico
    
    def convertirAOctal(self):
        conversion1 = int(str(self.valorNumerico), 2)
        conversion2 = oct(conversion1)
        return conversion2[2:]

    def convertirADecimal(self):
        conversion = int(str(self.valorNumerico), 2)
        return conversion

    def convertirAHexadecimal(self):
        conversion1 = int(str(self.valorNumerico), 2)
        conversion2 = hex(conversion1)
        return conversion2[2:]


if __name__ == "__main__":
    octal1 = Octal(10) #8
    octal2 = Octal(17) #15
    hexadecimal1 = Hexadecimal("56") #38
    hexadecimal2 = Hexadecimal("6C") #108
    binario1 = Binario("11011") #27
    binario2 = Binario("1001000") #72

    print("Octal 10")
    print(octal1.convertirABinario())
    print(octal1.convertirADecimal())
    print(octal1.convertirAHexadecimal())

    print("Octal 17")
    print(octal2.convertirABinario())
    print(octal2.convertirADecimal())
    print(octal2.convertirAHexadecimal())

    print("Hexadecimal 56")
    print(hexadecimal1.convertirABinario())
    print(hexadecimal1.convertirADecimal())
    print(hexadecimal1.convertirAOctal())

    print("Hexadecimal 6C")
    print(hexadecimal2.convertirABinario())
    print(hexadecimal2.convertirADecimal())
    print(hexadecimal2.convertirAOctal())