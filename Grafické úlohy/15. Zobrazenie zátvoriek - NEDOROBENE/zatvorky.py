import tkinter as tk

MENIC = {
    "(": 0,
    ")": 1
}

class Stack:
    def __init__(self):
        self.data: list[int] = []
    
    def push(self, cislo: int):
        self.data.append(cislo)
    
    def pop(self) -> int:
        if len(self.data) != 0:
            posledny_znak: int = self.data.pop(-1)
            return posledny_znak
        else:
            return False

vyraz = input(f"Zadaj matematický príklad: ")
zasobnik = Stack()

for znak in vyraz:
    if znak == "(":
        zasobnik.push(MENIC[znak])
    
    elif znak == ")":
        posledny_znak = zasobnik.pop()
        if posledny_znak == 0:
            print("ok")
        else:
            print("NAPICU")