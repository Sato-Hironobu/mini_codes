
def gcd(a, b): return a if b == 0 else gcd(b, a % b)

class Quotient():

        
    def __init__(self, numerator, denominator):
        
        GCD = gcd(numerator, denominator)
        self.numerator = numerator // GCD
        self.denominator = denominator // GCD

    def __add__(self, other):
        
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Quotient(numerator, denominator)

    def __sub__(self, other):
        
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Quotient(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Quotient(numerator, denominator)

    def __truediv__(self, other):
        
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Quotient(numerator, denominator)

    def __str__(self):
        
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):

        return f"Quotient({self.numerator/self.denominator})"

    def to_float(self):
        
        return self.numerator / self.denominator

    def to_percent(self):

        return self.numerator * 100 / self.denominator


class SaltWater():

    def __init__(self, name, amount, solute):
        
        self.name = name
        self.amount = Quotient(amount, 1)
        self.solute = Quotient(solute, 1)
        self.concentration = Quotient(solute, amount)

    def add_to(self, other, amount):

        amount = Quotient(amount, 1)
        
        self.amount -= amount
        self.solute -= amount * self.concentration
        
        other.amount += amount
        other.solute += amount * self.concentration
        other.concentration = other.solute / other.amount

        if self.amount.to_float() == 0:
        	self.concentration = None

    def show_property(self):
        
        print(f"=====Property of {self.name}=====")
        print(f"amount:        {self.amount.to_float()} gram")
        print(f"solute:        {self.solute.to_float()} gram")
        if self.concentration:
        	print(f"concentration: {self.concentration.to_percent()}%")
        

def test():

    BeakerA = SaltWater("BeakerA", 200, 16)
    BeakerB = SaltWater("BeakerB", 400, 8)

    print("<<<<<Before operation>>>>>") 
    BeakerA.show_property()
    BeakerB.show_property()

    BeakerA.add_to(BeakerB, 200)
    print("<<<<<After operation>>>>>") 
    BeakerA.show_property()
    BeakerB.show_property()

if __name__ == "__main__":

    test()
