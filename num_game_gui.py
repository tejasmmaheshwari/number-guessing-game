import tkinter as tk
from tkinter import messagebox
import random


# -----------------------------
# Game Settings
# -----------------------------

MIN_NUMBER = 1
MAX_NUMBER = 100


# -----------------------------
# Main Game Window
# -----------------------------

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#1e1e2e")


# -----------------------------
# Game Variables
# -----------------------------

secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
attempts = 0


# -----------------------------
# Functions
# -----------------------------

def make_guess():
    global attempts

    user_input = guess_entry.get()

    # Check for empty input
    if user_input == "":
        feedback_label.config(
            text="Enter a number first!",
            fg="#f9e2af"
        )
        return

    # Convert input into an integer
    try:
        guess = int(user_input)

    except ValueError:
        feedback_label.config(
            text="Please enter a whole number.",
            fg="#f38ba8"
        )
        guess_entry.select_range(0, tk.END)
        return

    # Check number range
    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        feedback_label.config(
            text="Choose a number from 1 to 100.",
            fg="#f9e2af"
        )
        guess_entry.select_range(0, tk.END)
        return

    # Count the attempt
    attempts += 1

    # Correct answer
    if guess == secret_number:

        feedback_label.config(
            text="🎉 CORRECT!",
            fg="#a6e3a1"
        )

        attempts_label.config(
            text=f"Attempts: {attempts}"
        )

        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the number!\n\n"
            f"The number was {secret_number}.\n"
            f"Attempts: {attempts}"
        )

        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")

        return

    # Too high
    elif guess > secret_number + 10:

        feedback_label.config(
            text="TOO HIGH!",
            fg="#f38ba8"
        )

        hint_label.config(
            text="Try going more than 10 numbers lower."
        )

    # High but close
    elif guess > secret_number:

        feedback_label.config(
            text="HIGH — You're close!",
            fg="#fab387"
        )

        hint_label.config(
            text="Try a little lower."
        )

    # Too low
    elif guess < secret_number - 10:

        feedback_label.config(
            text="TOO LOW!",
            fg="#f38ba8"
        )

        hint_label.config(
            text="Try going more than 10 numbers higher."
        )

    # Low but close
    else:

        feedback_label.config(
            text="LOW — You're close!",
            fg="#fab387"
        )

        hint_label.config(
            text="Try a little higher."
        )

    # Update attempts
    attempts_label.config(
        text=f"Attempts: {attempts}"
    )

    # Clear input
    guess_entry.delete(0, tk.END)
    guess_entry.focus()


def new_game():
    global secret_number, attempts

    # Generate a new number
    secret_number = random.randint(
        MIN_NUMBER,
        MAX_NUMBER
    )

    # Reset attempts
    attempts = 0

    # Reset the interface
    feedback_label.config(
        text="Make your first guess!",
        fg="#cdd6f4"
    )

    hint_label.config(
        text="You have unlimited attempts."
    )

    attempts_label.config(
        text="Attempts: 0"
    )

    guess_entry.config(state="normal")
    guess_button.config(state="normal")

    guess_entry.delete(0, tk.END)
    guess_entry.focus()


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="NUMBER GUESS",
    font=("Arial", 28, "bold"),
    bg="#1e1e2e",
    fg="white"
)

title_label.pack(pady=(40, 5))


subtitle_label = tk.Label(
    root,
    text="Can you find the hidden number?",
    font=("Arial", 12),
    bg="#1e1e2e",
    fg="#a6adc8"
)

subtitle_label.pack()


# -----------------------------
# Number Range
# -----------------------------

range_label = tk.Label(
    root,
    text="NUMBER RANGE   1 — 100",
    font=("Arial", 11, "bold"),
    bg="#313244",
    fg="#cdd6f4",
    padx=20,
    pady=8
)

range_label.pack(pady=25)


# -----------------------------
# Instruction
# -----------------------------

instruction_label = tk.Label(
    root,
    text="Enter your guess",
    font=("Arial", 14),
    bg="#1e1e2e",
    fg="white"
)

instruction_label.pack(pady=(5, 10))


# -----------------------------
# Guess Input
# -----------------------------

guess_entry = tk.Entry(
    root,
    font=("Arial", 22, "bold"),
    justify="center",
    width=10,
    bg="#313244",
    fg="white",
    insertbackground="white",
    relief="flat"
)

guess_entry.pack(ipady=10)

guess_entry.focus()


# -----------------------------
# Guess Button
# -----------------------------

guess_button = tk.Button(
    root,
    text="GUESS",
    command=make_guess,
    font=("Arial", 13, "bold"),
    bg="#89b4fa",
    fg="#11111b",
    activebackground="#74c7ec",
    relief="flat",
    cursor="hand2",
    width=18,
    pady=10
)

guess_button.pack(pady=20)


# -----------------------------
# Feedback
# -----------------------------

feedback_label = tk.Label(
    root,
    text="Make your first guess!",
    font=("Arial", 18, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)

feedback_label.pack(pady=15)


# -----------------------------
# Attempts
# -----------------------------

attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 12),
    bg="#1e1e2e",
    fg="#a6adc8"
)

attempts_label.pack(pady=5)


# -----------------------------
# Hint
# -----------------------------

hint_label = tk.Label(
    root,
    text="You have unlimited attempts.",
    font=("Arial", 10),
    bg="#1e1e2e",
    fg="#6c7086"
)

hint_label.pack(pady=10)


# -----------------------------
# New Game Button
# -----------------------------

new_game_button = tk.Button(
    root,
    text="NEW GAME",
    command=new_game,
    font=("Arial", 11, "bold"),
    bg="#45475a",
    fg="white",
    activebackground="#585b70",
    relief="flat",
    cursor="hand2",
    width=15,
    pady=8
)

new_game_button.pack(pady=15)


# -----------------------------
# Enter Key Support
# -----------------------------

root.bind(
    "<Return>",
    lambda event: make_guess()
)


# -----------------------------
# Start Game
# -----------------------------

root.mainloop()