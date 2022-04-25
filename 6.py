#1
import re
text="""Хотя никогда зачастую
лучше, если прямо сейчас.
Если реализацию сложно
объяснить — идея плоха.
Если реализацию легко объяснить
— идея, возможно, хороша.
Пространства имен — отличная
штука! Будем делать их побольше!
"""
result = re.findall('^Если', text, re.MULTILINE)
print(result)

#2
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

class Form(Rectangle):
    def area(self):
        return (self.w * self.h)

rec = Rectangle(20,40)
print(Form.area(rec))