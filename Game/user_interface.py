from tkinter import messagebox
from Game import engine
import importlib
import tkinter


importlib.reload(engine)


##############################################################################################

class GameUI:

    def __init__(self):
        self.engine = engine.GameEngine()
        self.player_name_field = None
        self.guess_field = None
        self.main_window = None

    def build(self):
        self.create_main_window()

    def check_guess(self):
        # get game data
        player_name = self.player_name_field.get()
        guess = int(self.guess_field.get())

        # Game starts here
        self.engine.get_player_name(player_name=player_name)
        result = self.engine.play_game(guess=guess)
        messagebox.showinfo("Game Info", result)

        # Closes main window if the secret number is correct
        if self.engine.secret_number == guess:
            self.main_window.destroy()
            return

        # Clean the guess text field after attempt was made
        self.guess_field.delete(0, "end")

    def create_main_window(self):
        # Create the UI main window
        window = tkinter.Tk()
        self.main_window = window
        window.geometry("500x500")

        greeting = tkinter.Label(window, text="Guess the secret number!", font=("Helvetica", 18), pady=35)
        greeting.pack()

        # Instructions
        instruction_name = tkinter.Label(window, text="Guess the magic number between 1 and 30!",
                                         font=("Helvetica", 14),
                                         pady=10)
        instruction_name.pack()

        # name request
        name_label = tkinter.Label(window, text="Enter your name:", font=("Helvetica", 14), pady=10)
        name_label.pack()

        # player entry field
        player = tkinter.Entry(window)
        self.player_name_field = player
        player.pack()

        # name request
        guess = tkinter.Label(window, text="Try your luck!", font=("Helvetica", 14), pady=10)
        guess.pack()

        # guess entry field
        guess = tkinter.Entry(window)
        self.guess_field = guess
        guess.pack()

        spacer = tkinter.Label(window, pady=15)
        spacer.pack()

        submit = tkinter.Button(window, text="Submit", padx=25, pady=25,
                                command=self.check_guess)  # self.check_guess, not self.check_guess()
        submit.pack()
        # Show the main window
        window.mainloop()


##############################################################################################

if __name__ == '__main__':
    game = GameUI()
    game.build()
