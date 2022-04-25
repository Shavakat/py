#1
class Soda:
    def __init__(self, dobavka=0):
        self.dobavka = dobavka
    def show_my_drink(self):
        if self.dobavka != 0:
           print(f'«Газировка и {self.dobavka}» ')
        else:
            print('«Обычная газировка»')

soda = Soda()
print(soda.show_my_drink())

#2
import turtle
t=turtle.Pen()
t.up()
t.forward(20)
t.left(90)
t.forward(30)
t.color('yellow')
t.down()
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.up()
t.left(90)
t.forward(20)
t.right(90)
t.forward(30)
t.right(180)
t.down()
t.color('green')
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.up()
t.right(180)
t.forward(101)
t.down()
t.color('red')
t.right(45)
t.forward(70)
t.right(90)
t.forward(70)
t.right(135)
t.forward(100)