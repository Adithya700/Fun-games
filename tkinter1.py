import tkinter as tk
from tkinter import font, messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.max_attempts = 5
        self.secret_number = 0
        self.attempts = 0
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x400")  # Optional: set window size

        # Main frame to center content
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(expand=True, fill='both')

        # Define fonts
        self.btn_font = font.Font(family='Arial', size=14, weight='bold')

        # Widgets
        self.label_title = tk.Label(self.main_frame, text="🎯 Guess the Number between 1 and 100")
        self.label_title.pack(pady=10)

        self.entry_guess = tk.Entry(self.main_frame)
        self.entry_guess.pack()

        self.button_guess = tk.Button(self.main_frame, text="Guess", command=self.check_guess, width=10, height=2, font=self.btn_font)
        self.button_guess.pack(pady=5)

        self.label_feedback = tk.Label(self.main_frame, text="")
        self.label_feedback.pack()

        self.label_attempts = tk.Label(self.main_frame, text=f"Attempts remaining: {self.max_attempts - self.attempts}")
        self.label_attempts.pack()

        self.frame_buttons = tk.Frame(self.main_frame)
        self.frame_buttons.pack(pady=10)

        self.play_again_button = tk.Button(self.frame_buttons, text="Play Again", command=self.reset_game, state='disabled', width=12, height=2, font=self.btn_font)
        self.play_again_button.pack(side='left', padx=5)

        self.exit_button = tk.Button(self.frame_buttons, text="Exit", command=master.quit, width=8, height=2, font=self.btn_font)
        self.exit_button.pack(side='left', padx=5)

        self.max_attempts = 5
        self.attempts = 0
        self.secret_number = 0

        self.reset_game()

    def reset_game(self):
        self.max_attempts = 5
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.label_feedback.config(text="")
        self.label_attempts.config(text=f"Attempts remaining: {self.max_attempts - self.attempts}")
        self.entry_guess.delete(0, tk.END)
        self.button_guess.config(state='normal')
        self.play_again_button.config(state='disabled')

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return

        self.attempts += 1
        attempts_left = self.max_attempts - self.attempts

        if guess < self.secret_number:
            self.label_feedback.config(text="Too low! Try again.")
        elif guess > self.secret_number:
            self.label_feedback.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"🎉 Correct! You guessed it in {self.attempts} attempts!")
            self.end_game()
            return

        self.label_attempts.config(text=f"Attempts remaining: {attempts_left}")

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"😢 You lose! The number was {self.secret_number}.")
            self.end_game()

    def end_game(self):
        self.button_guess.config(state='disabled')
        self.play_again_button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()