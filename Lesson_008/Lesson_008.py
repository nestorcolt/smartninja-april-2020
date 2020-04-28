import tkinter

"""
Resources:
https://docs.python.org/3/library/tk.html
"""
##############################################################################################

window = tkinter.Tk()
window.geometry("500x500")

# greeting text
greeting = tkinter.Label(window, text="Guess the secret number!", font=("Helvetica", 18), pady=35)
greeting.pack()

# guess entry field
guess = tkinter.Entry(window)
guess.pack()

window.mainloop()

##############################################################################################
