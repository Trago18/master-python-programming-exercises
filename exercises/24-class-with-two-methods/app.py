
class myClass:
    def __init__(self):
    	self.txt = ''

    def getString(self):
        self.txt = input()

    def printString(self):
        print(self.txt.upper())

c1 = myClass()
c1.getString()
c1.printString()