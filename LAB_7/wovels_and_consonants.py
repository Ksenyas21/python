# -*- coding: utf8 -*-

from tkinter import *


class Blocks:
    def __init__(self, master):
        self.lab1 = Label(master, width=20, text=' Enter word:', pady=10)
        self.ent1 = Entry(master, width=20)

        self.but = Button(master,
                          text="Show result", pady=10)

        self.num1 = Label(master, width=40, pady=20, text='Vowels:')
        self.num2 = Label(master, width=40, pady=20, text='Consonants:')

        self.but['command'] = self.count_v2
        self.lab1.pack()
        self.ent1.pack()
        self.but.pack()
        self.num1.pack()
        self.num2.pack()

    def count_v2(self):
        word = self.ent1.get()
        num1 = 0
        num2 = 0
        for letter in word:
            if letter.isalpha():
                if letter.lower() in 'aeiouy':

                    num1 += 1
                    self.num1['text'] = 'Vowels: ' + str(num1)
                else:

                    num2 += 1
                    self.num2['text'] = 'Consonants: ' + str(num2)



root = Tk()
root.title('V 7')

main = Blocks(root)

root.mainloop()
