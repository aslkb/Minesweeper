import tkinter
from PIL import ImageTk, Image
import random


xrand = [150, 197, 244, 291]
yrand = [50, 97, 144, 191]

okno = tkinter.Tk()
okno.geometry("450x450")
okno.config(background="white")
okno.resizable(False, False)

zemlya = Image.open("zemlya.png")
zemlya = zemlya.resize((40, 40))
zemlyaTk1 = ImageTk.PhotoImage(zemlya)

flag = Image.open("flajok.jpg")
flag = flag.resize((40, 40))
flagTK = ImageTk.PhotoImage(flag)

bob = Image.open("BUMBUM.jpg")
bob = bob.resize((40, 40))
bobTK = ImageTk.PhotoImage(bob)


# lose = Image.open("BIGGEST L.jpg")
# loseTK = ImageTk.PhotoImage(lose)
# lblLose = tkinter.Label(image=loseTK)


def bob(x, y):
    global btnZemlya
    if x == 150 and y == 50:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget1()
    elif x == 197 and y == 50:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget2()
    elif x == 244 and y == 50:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget3()
    elif x == 291 and y == 50:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget4()
    elif x == 150 and y == 97:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget5()
    elif x == 197 and y == 97:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget6()
    elif x == 244 and y == 97:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget7()
    elif x == 291 and y == 97:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget8()
    elif x == 150 and y == 144:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget9()
    elif x == 197 and y == 144:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget10()
    elif x == 244 and y == 144:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget11()
    elif x == 291 and y == 144:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget12()
    elif x == 150 and y == 191:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget13()
    elif x == 197 and y == 191:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget14()
    elif x == 244 and y == 191:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget15()
    elif x == 291 and y == 191:
        btnZemlya = tkinter.Button(command=BOOM, image=zemlyaTk1)
        btnZemlya.place(x=x, y=y)
        forget16()


def retry():
    lblLose.place_forget()
    x = random.choice(xrand)
    y = random.choice(yrand)
    lblbob.place(x=x, y=y)
    btnZemlya.place_forget()
    bob(x, y)
    btnZemlya1.place(x=150, y=50)
    btnZemlya2.place(x=197, y=50)
    btnZemlya3.place(x=244, y=50)
    btnZemlya4.place(x=291, y=50)
    btnZemlya5.place(x=150, y=97)
    btnZemlya6.place(x=197, y=97)
    btnZemlya7.place(x=244, y=97)
    btnZemlya8.place(x=291, y=97)
    btnZemlya9.place(x=150, y=144)
    btnZemlya10.place(x=197, y=144)
    btnZemlya11.place(x=244, y=144)
    btnZemlya12.place(x=291, y=144)
    btnZemlya13.place(x=150, y=191)
    btnZemlya14.place(x=197, y=191)
    btnZemlya15.place(x=244, y=191)
    btnZemlya16.place(x=291, y=191)

ls = []

def forget1():
    btnZemlya1.place_forget()
    ls.append(1)
    print(len(ls))

def forget2():
    btnZemlya2.place_forget()
    ls.append(1)
    print(len(ls))

def forget3():
    btnZemlya3.place_forget()
    ls.append(1)
    print(len(ls))


def forget4():
    btnZemlya4.place_forget()
    ls.append(1)
    print(len(ls))



def forget5():
    btnZemlya5.place_forget()
    ls.append(1)
    print(len(ls))



def forget6():
    btnZemlya6.place_forget()
    ls.append(1)
    print(len(ls))



def forget7():
    btnZemlya7.place_forget()
    ls.append(1)
    print(len(ls))


def forget8():
    btnZemlya8.place_forget()
    ls.append(1)
    print(len(ls))


def forget9():
    btnZemlya9.place_forget()
    ls.append(1)
    print(len(ls))


def forget10():
    btnZemlya10.place_forget()
    ls.append(1)
    print(len(ls))


def forget11():
    btnZemlya11.place_forget()
    ls.append(1)
    print(len(ls))


def forget12():
    btnZemlya12.place_forget()
    ls.append(1)
    print(len(ls))


def forget13():
    btnZemlya13.place_forget()
    ls.append(1)
    print(len(ls))


def forget14():
    btnZemlya14.place_forget()
    ls.append(1)
    print(len(ls))


def forget15():
    btnZemlya15.place_forget()
    ls.append(1)
    print(len(ls))


def forget16():
    btnZemlya16.place_forget()
    ls.append(1)
    print(len(ls))

lblFlag1 = tkinter.Label(image=flagTK)
lblFlag2 = tkinter.Label(image=flagTK)
lblFlag3 = tkinter.Label(image=flagTK)
lblFlag4 = tkinter.Label(image=flagTK)
lblFlag5 = tkinter.Label(image=flagTK)
lblFlag6 = tkinter.Label(image=flagTK)
lblFlag7 = tkinter.Label(image=flagTK)
lblFlag8 = tkinter.Label(image=flagTK)
lblFlag9 = tkinter.Label(image=flagTK)
lblFlag10 = tkinter.Label(image=flagTK)
lblFlag11 = tkinter.Label(image=flagTK)
lblFlag12 = tkinter.Label(image=flagTK)
lblFlag13 = tkinter.Label(image=flagTK)
lblFlag14 = tkinter.Label(image=flagTK)
lblFlag15 = tkinter.Label(image=flagTK)
lblFlag16 = tkinter.Label(image=flagTK)

lblFlag1.place(x=150, y=50)
lblFlag2.place(x=197, y=50)
lblFlag3.place(x=244, y=50)
lblFlag4.place(x=291, y=50)
lblFlag5.place(x=150, y=97)
lblFlag6.place(x=197, y=97)
lblFlag7.place(x=244, y=97)
lblFlag8.place(x=291, y=97)
lblFlag9.place(x=150, y=144)
lblFlag10.place(x=197, y=144)
lblFlag11.place(x=244, y=144)
lblFlag12.place(x=291, y=144)
lblFlag13.place(x=150, y=191)
lblFlag14.place(x=197, y=191)
lblFlag15.place(x=244, y=191)
lblFlag16.place(x=291, y=191)

lblbob = tkinter.Label(image=bobTK)
x = random.choice(xrand)
y = random.choice(yrand)
lblbob.place(x=x, y=y)


btnZemlya1 = tkinter.Button(image=zemlyaTk1, command=forget1)
btnZemlya2 = tkinter.Button(image=zemlyaTk1, command=forget2)
btnZemlya3 = tkinter.Button(image=zemlyaTk1, command=forget3)
btnZemlya4 = tkinter.Button(image=zemlyaTk1, command=forget4)
btnZemlya5 = tkinter.Button(image=zemlyaTk1, command=forget5)
btnZemlya6 = tkinter.Button(image=zemlyaTk1, command=forget6)
btnZemlya7 = tkinter.Button(image=zemlyaTk1, command=forget7)
btnZemlya8 = tkinter.Button(image=zemlyaTk1, command=forget8)
btnZemlya9 = tkinter.Button(image=zemlyaTk1, command=forget9)
btnZemlya10 = tkinter.Button(image=zemlyaTk1, command=forget10)
btnZemlya11 = tkinter.Button(image=zemlyaTk1, command=forget11)
btnZemlya12 = tkinter.Button(image=zemlyaTk1, command=forget12)
btnZemlya13 = tkinter.Button(image=zemlyaTk1, command=forget13)
btnZemlya14 = tkinter.Button(image=zemlyaTk1, command=forget14)
btnZemlya15 = tkinter.Button(image=zemlyaTk1, command=forget15)
btnZemlya16 = tkinter.Button(image=zemlyaTk1, command=forget16)

btnZemlya1.place(x=150, y=50)
btnZemlya2.place(x=197, y=50)
btnZemlya3.place(x=244, y=50)
btnZemlya4.place(x=291, y=50)
btnZemlya5.place(x=150, y=97)
btnZemlya6.place(x=197, y=97)
btnZemlya7.place(x=244, y=97)
btnZemlya8.place(x=291, y=97)
btnZemlya9.place(x=150, y=144)
btnZemlya10.place(x=197, y=144)
btnZemlya11.place(x=244, y=144)
btnZemlya12.place(x=291, y=144)
btnZemlya13.place(x=150, y=191)
btnZemlya14.place(x=197, y=191)
btnZemlya15.place(x=244, y=191)
btnZemlya16.place(x=291, y=191)

btnAgain = tkinter.Button(background="green", text="Retry?", command=retry)
btnAgain.place(x=220, y=250)


def BOOM():
    lblLose.place(x=152, y=50)
    btnZemlya.place_forget()
    ls.clear()


bob(x, y)

lose = Image.open("BIGGEST L.jpg")
loseTK = ImageTk.PhotoImage(lose)
lblLose = tkinter.Label(image=loseTK)

# winner = Image.open("WINWIN.png")
# winner = winner.resize((185, 185))
# winTk = ImageTk.PhotoImage(winner)
# lblWin = tkinter.Label(image=winTk)

okno.mainloop()
