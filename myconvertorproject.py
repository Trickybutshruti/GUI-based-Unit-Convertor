from tkinter import *

root = Tk()
root.title("My Project Convertor")
root.geometry("1000x700")
root.maxsize(1000,700)
root.minsize(1000,700)

root.configure(bg='lavender')
def from_kg():
	
	gram = float(e2_value.get())*1000
	pound = float(e2_value.get())*2.20462
	ounce = float(e2_value.get())*35.274
	
	t1.delete("1.0", END)
	t1.insert(END,gram)
	t2.delete("1.0", END)
	t2.insert(END,pound)
	t3.delete("1.0", END)
	t3.insert(END,ounce)
	
	
def from_L():

    millilitre = float(f2_value.get())*1000
    cubic_meter = float(f2_value.get())*0.001
    gallon = float(f2_value.get())*0.264
    
    t4.delete("1.0", END)
    t4.insert(END,millilitre)
    t5.delete("1.0", END)
    t5.insert(END,cubic_meter)
    t6.delete("1.0", END)
    t6.insert(END,gallon)


def from_m():
	
	centimeter = float(g2_value.get())*100
	inch = float(g2_value.get())*39.37
	feet = float(g2_value.get())*3.281
	
	t7.delete("1.0", END)
	t7.insert(END,centimeter)
	t8.delete("1.0", END)
	t8.insert(END,inch)
	t9.delete("1.0", END)
	t9.insert(END,feet)
	
def from_hr():
	
	minute = float(h2_value.get())*60
	second = float(h2_value.get())*3600
	milliseconds = float(h2_value.get())*3600000
	
	t10.delete("1.0", END)
	t10.insert(END,minute)
	t11.delete("1.0", END)
	t11.insert(END,second)
	t12.delete("1.0", END)
	t12.insert(END,milliseconds)



e1 =Label(root, text = "Enter the weight in Kg", font= "Algerian 18 italic bold",bg= "lavender")
e2_value = StringVar()
e2 = Entry(root, textvariable = e2_value, font= "Lucida 16 bold",width= 15,background="alice blue" )
e3 = Label(root, text = 'Gram', font= "Algerian 16 ", bg= "lavender", foreground="Dark blue")
e4 = Label(root, text = 'Pounds', font= "Algerian 16 ", bg= "lavender", foreground="Dark blue")
e5 = Label(root, text = 'Ounce', font= "Algerian 16 ", bg= "lavender", foreground="Dark blue")

t1 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light blue", padx= 10, relief= SUNKEN)
t2 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light pink", relief= SUNKEN)
t3 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light blue", relief= SUNKEN)
b1 = Button(root, text = "Convert", font= "Algerian 14 italic bold", bg="black",foreground="White", command = from_kg)

f1 = Label(root, text = "Enter the volume in L", font= "Algerian 18 italic bold",bg= "lavender")
f2_value = StringVar()
f2 = Entry(root, textvariable = f2_value, font= "Lucida 16 bold",width= 15,background="alice blue")
f3 = Label(root, text = 'millilitre', font= "Algerian 16",bg= "lavender", foreground="Dark blue")
f4 = Label(root, text = 'cubic metre', font= "Algerian 16",bg= "lavender", foreground="Dark blue")
f5 = Label(root, text = 'gallon', font= "Algerian 16", bg= "lavender", foreground="Dark blue")

t4 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light pink", relief= SUNKEN)
t5 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light blue", relief= SUNKEN)
t6 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light pink", relief= SUNKEN)

b2 = Button(root, text = "Convert", font= "Algerian 14 italic bold", bg="black",foreground="White", command = from_L)

g1 = Label(root, text = "Enter the length in m", font= "Algerian 18 italic bold",bg= "lavender")
g2_value = StringVar()
g2 = Entry(root, textvariable = g2_value, font= "Lucida 16 bold",width= 15,background="alice blue")
g3 = Label(root, text = 'centimeter', font= "Algerian 16", bg= "lavender", foreground="Dark blue")
g4 = Label(root, text = 'inch', font= "Algerian 16", bg= "lavender", foreground="Dark blue")
g5 = Label(root, text = 'feet', font= "Algerian 16", bg= "lavender", foreground="Dark blue")

t7 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light blue", relief= SUNKEN)
t8 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light pink", relief= SUNKEN)
t9 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light blue", relief= SUNKEN)

b3 = Button(root, text = "Convert", font= "Algerian 14 italic bold", bg="black",foreground="White", command = from_m)

h1 = Label(root, text = "Enter the time in hr", font= "Algerian 18 italic bold",bg= "lavender")
h2_value = StringVar()
h2 = Entry(root, textvariable = h2_value, font= "Lucida 16 bold",width= 15,background="alice blue")
h3 = Label(root, text = 'minute', font= "Algerian 16",bg= "lavender", foreground="Dark blue")
h4 = Label(root, text = 'second', font= "Algerian 16",bg= "lavender", foreground="Dark blue")
h5 = Label(root, text = 'milliseconds', font= "Algerian 16",bg= "lavender", foreground="Dark blue")

t10 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light pink", relief= SUNKEN)
t11 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light blue", relief= SUNKEN)
t12 = Text(root, height = 2, width = 20, font= "Lucida 16 bold", bg= "light pink", relief= SUNKEN)

b4 = Button(root, text = "Convert", font= "Algerian 14 italic bold", bg="black",foreground="White", command = from_hr)

e1.grid(row = 0, column = 0, padx=25, pady=5)
e2.grid(row = 0, column = 2, padx=25, pady=5)
e3.grid(row = 1, column = 0, padx=25, pady=5)
e4.grid(row = 1, column = 2, padx=25, pady=5)
e5.grid(row = 1, column = 4, padx=25, pady=5)
t1.grid(row = 2, column = 0, padx=25, pady=15)
t2.grid(row = 2, column = 2, padx=25, pady=15)
t3.grid(row = 2, column = 4, padx=25, pady=15)
b1.grid(row = 0, column = 4, padx=25, pady=5)

f1.grid(row = 4, column = 0, padx=25, pady=5)
f2.grid(row = 4, column = 2, padx=25, pady=5)
f3.grid(row = 5, column = 0, padx=25, pady=5)
f4.grid(row = 5, column = 2, padx=25, pady=5)
f5.grid(row = 5, column = 4, padx=25, pady=5)
t4.grid(row = 6, column = 0, padx=25, pady=10)
t5.grid(row = 6, column = 2, padx=25, pady=10)
t6.grid(row = 6, column = 4, padx=25, pady=10)
b2.grid(row = 4, column = 4, padx=25, pady=5)

g1.grid(row = 8, column = 0, padx=25, pady=5)
g2.grid(row = 8, column = 2, padx=25, pady=5)
g3.grid(row = 9, column = 0, padx=25, pady=5)
g4.grid(row = 9, column = 2, padx=25, pady=5)
g5.grid(row = 9, column = 4, padx=25, pady=5)
t7.grid(row = 10, column = 0, padx=25, pady=10)
t8.grid(row = 10, column = 2, padx=25, pady=10)
t9.grid(row = 10, column = 4, padx=25, pady=10)
b3.grid(row = 8, column = 4, padx=25, pady=5)

h1.grid(row = 12, column = 0, padx=25, pady=5)
h2.grid(row = 12, column = 2, padx=25, pady=5)
h3.grid(row = 13, column = 0, padx=25, pady=5)
h4.grid(row = 13, column = 2, padx=25, pady=5)
h5.grid(row = 13, column = 4, padx=25, pady=5)
t10.grid(row = 14, column = 0, padx=25, pady=10)
t11.grid(row = 14, column = 2, padx=25, pady=10)
t12.grid(row = 14, column = 4, padx=25, pady=10)
b4.grid(row = 12, column = 4, padx=25, pady=5)


root.mainloop()
