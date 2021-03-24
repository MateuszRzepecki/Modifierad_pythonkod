import tkinter.messagebox
import re 
from tkinter import *
from tkinter import messagebox

# Email validation


# ****** GLOBAL VARIABLES ******

objects = []
window = Tk()
window.withdraw()
window.title('Epost Lagring')

class popupWindow(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Skriv Lösenord')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Ditt lösenord: ", font=('Arial', 12), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='?', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Bekräfta', command=self.cleanup, font=('Arial', 12))
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        access = '1234'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 7:
                window.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Fel lösenord', 'Du gav fel lösenord, antal försök: ' + str(7 - self.attempts))

class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class entity_display:

    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('Arial', 12))
        self.label_email = Label(self.window, text=dencryptedE, font=('Arial', 12))
        self.label_pass = Label(self.window, text=dencryptedP, font=('Arial', 12))
        self.deleteButton = Button(self.window, text='X', fg='orange', command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_pass.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Radera', 'Är du säker att du vill radera detta?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


# ******* FUNCTIONS *********


def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = entity_add(window, n, p, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Klart', 'Den här informationen har laggts till, \n' + 'Namn: ' + n + '\nEmail: ' + m + '\nLösenord: ' + p)
    readfile()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


# ******* GRAPHICS *********

m = popupWindow(window)

entity_label = Label(window, text='Lägg till info', font=('Arial', 14))
name_label = Label(window, text='Namn: ', font=('Arial', 12))
email_label = Label(window, text='Email: ', font=('Arial', 12))
pass_label = Label(window, text='Lösenord: ', font=('Arial', 12))
name = Entry(window, font=('Arial', 12))
email = Entry(window, font=('Arial', 12))
password = Entry(window, show='?', font=('Arial', 12))
submit = Button(window, text='Lägg till Epost', command=onsubmit, font=('Arial', 12))

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
email_label.grid(row=2, sticky=E, padx=3)
pass_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_label2 = Label(window, text='Namn: ', font=('Arial', 12))
email_label2 = Label(window, text='Email: ', font=('Arial', 12))
pass_label2 = Label(window, text='Lösenord: ', font=('Arial', 12))

name_label2.grid(row=5)
email_label2.grid(row=5, column=1)
pass_label2.grid(row=5, column=2)

readfile()

window.mainloop()
