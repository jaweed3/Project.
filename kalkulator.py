class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def minus(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"
    
    def pangkat(self):
        return self.a ** self.b
    
    def pembagian_bulat(self):
        if self.b != 0:
            return self.a // self.b
        else:
            return "Error: Division by zero"
    
    def modulus(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return "Error: Division by zero"

def main():
    a = int(input("Input Value A --> "))
    b = int(input("Input Value B --> "))
    calc = Kalkulator(a, b)

    option = input("Choose Operation (add, minus, multiply, division, pangkat, pembagian bulat, modulus) --> ").lower()

    if option == "add":
        result = calc.add()
    elif option == "minus":
        result = calc.minus()
    elif option == "multiply":
        result = calc.multiply()
    elif option == "division":
        result = calc.division()
    elif option == "pangkat":
        result = calc.pangkat()
    elif option == "pembagian bulat":
        result = calc.pembagian_bulat()
    elif option == "modulus":
        result = calc.modulus()
    else:
        print("Invalid option")
        return

    print("The Result is -->", result)
    again()

def again():
    loop = input("Again? yes/no --> ").lower()

    if loop == "yes":
        main()

    else:
        print("Goodbye!")
        quit()

if __name__ == "__main__":
    main()