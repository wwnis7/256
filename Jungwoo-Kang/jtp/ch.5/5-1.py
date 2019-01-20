#class Calculator:
#    def __init__(self):
#        self.value = 0

#    def add(self, val):
#        self.value += val
#        return self.value
#class uprgradecalculator(Calculator):
#    def minus(self,val):
#        self.value -= val
#        return self.value
#cal= uprgradecalculator()

#cal.add(10)
#print(cal.minus(7))

#왜 none으로 뜨지

#2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value +=val
        if self.value >= 100:
             return 100
        else:
             return self.value

max=MaxLimitCalculator()
max.add(50)
print(max.add(44))