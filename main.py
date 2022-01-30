from tkinter import *

window = Tk()
window.title("First Title")
window.minsize(width=500, height=500)

#Label

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)
# my_label.pack() default to top center, side="left" is left center


#Unlimited Arguments
# def add(*args):
#     print(args[1])
#     num = 0
#     for n in args:
#         num += n
#     return num
# new = add(2, 5, 6, 8)
# print(new)

def calculate(n, **kwargs):
   # print(kwargs)
   # print(kwargs["name"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
   n += kwargs["add"]
   n *= kwargs["multiply"]
   print(n)

# calculate(name="Megan", number=28)
# calculate(3, add=3, multiply=2)

# class Bamboo:
#
#    def __init__(self, **kw):
#       self.sci_name = kw.get("sci_name")
#       self.com_name = kw.get("com_name") #using kw.get("com_name" instead of kw["com_name"] makes this field optional
#
#
# first_bamboo = Bamboo(sci_name="Bambusa chungii", com_name="Blue Chungii")
# print(first_bamboo.com_name)


#Button

def button_clicked():
   print("Clack")

   word = entry_field.get()
   my_label.config(text=word)

button = Button(text="Clickety", command=button_clicked)
button.pack(expand=True)


#entry
entry_field = Entry(width=20)
entry_field.insert(END, string="New Label")
entry_field.pack(expand=True)

textbox = Text(height=5, width=30)   #height is number of lines
textbox.focus()
textbox.insert(END, "Example of multiline entry box")
print(textbox.get("1.0", END)) #starting from the first line at character 0
textbox.pack(expand=True)

def spinbox_used():
   print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack(expand=True)

def checkbutton_used():
   print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack(expand=True)



window.mainloop()    # keeps on screen

