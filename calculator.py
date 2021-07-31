from tkinter import *


def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


def backspace(event):
    cur_index_of_cursor =screen.index(INSERT) # To get the position of the cursor
    c = list(scvalue.get())
    try:
        c.pop(cur_index_of_cursor-1)
    except:
        pass
    c = str(c)
    a = c.replace(',', '')
    a = a.replace('\'', '')
    a = a.replace('[', '')
    a = a.replace(']', '')
    a = a.replace(' ', '')
    scvalue.set(a)

root = Tk()
root.geometry("700x600")
root.title('Calculator by Shrikant_k')
root.wm_iconbitmap("calculator.ico")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=10, pady=12, padx=14)


f1 = Frame(root, bg="grey")
b = Button(f1, text="7", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=14)
b.bind("<Button-1>", click)
b = Button(f1, text="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=14)
b.bind("<Button-1>", click)
b = Button(f1, text="9", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=14)
b.bind("<Button-1>", click)
b = Button(f1, text="-", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=14)
b.bind("<Button-1>", click)
b = Button(f1, text="+", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=14)
b.bind("<Button-1>", click)
f1.pack()


f1 = Frame(root, bg="grey")
b = Button(f1, text="4", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=12)
b.bind("<Button-1>", click)
b = Button(f1, text="5", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="6", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="/", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=15)
b.bind("<Button-1>", click)
b = Button(f1, text="*", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=12)
b.bind("<Button-1>", click)
f1.pack()


f1 = Frame(root, bg="grey")
b = Button(f1, text="1", font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="2", font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="3", font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="C", font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="=", font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=11)
b.bind("<Button-1>", click)
f1.pack()


f1 = Frame(root, bg="grey")
b = Button(f1, text=".", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="0", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="%", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="(", font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text=")", font="lucida 35 bold")
b.pack(side=LEFT, padx=13, pady=11)
b.bind("<Button-1>", click)
b = Button(f1, text="<-", font="lucida 35 bold")
b.pack(side=RIGHT, padx=13, pady=11)
b.bind("<Button-1>", backspace)
f1.pack()


root.mainloop()
