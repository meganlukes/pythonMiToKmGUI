import tkinter

window = tkinter.Tk()
window.title("First Title")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))
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

class Bamboo:

   def __init__(self, **kw):
      self.sci_name = kw.get("sci_name")
      self.com_name = kw.get("com_name") #using kw.get("com_name" instead of kw["com_name"] makes this field optional


first_bamboo = Bamboo(sci_name="Bambusa chungii", com_name="Blue Chungii")
print(first_bamboo.com_name)
window.mainloop()    # keeps on screen