import tkinter

window = tkinter.Tk()
window.title("First Title")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))

my_label.pack(expand=True)
#my_label.pack() default to top center, side="left" is left center





window.mainloop()    # keeps on screen