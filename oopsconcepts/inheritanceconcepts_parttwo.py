from oopsconcepts.classesandobjects import Calculator


class Display(Calculator):

        def __init__(self, a, b):
            super().__init__(a,b)
            print("I am a constructor in Display class")

        def display(self):
            print(f'On Performing the Operations for: {self.firstNumber}, and another number: {self.secondNumber} the Result is: ,${self.add()}')


d1=Display(30,50)
d1.display()