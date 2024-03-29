import enum
from tkinter import *
from tkinter import messagebox
import words

root = Tk()
word = words.get_word()
root.geometry('225x400')
GREEN = "#20d450"
YELLOW = "#faf614"
BLACK = "#000000"
WHITE = "#FFFFFF"
GREY = "#8f8f8b"

root.config(bg=BLACK)

guessnum = 1

wordInput = Entry(root)
wordInput.grid(row=999, column=1, padx=10, pady=10, columnspan=3)


def getGuess():

    global word
    guess = wordInput.get()

    global guessnum
    guessnum += 1

    if guessnum <= 5:

        if len(guess) == 5:

            if word == guess: #CORRECT
                messagebox.showinfo("correct!", f"correct! the word was {word.title()}")
            else:             #INCORRECT
                for i, letter in enumerate(guess):

                    label = Label(root, text=letter.upper())
                    label.grid(row=guessnum, column=i, padx=10, pady=10)

                    if letter == word[i]: #if they get the letter right
                        label.config(bg=GREEN, fg=BLACK)

                    if letter in word and not letter == word[i]: #not in the correct spot
                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter not in word:
                        label.config(bg=GREY, fg=BLACK)

        else:
            messagebox.showerror("must be 5 letters", " use 5 letters in your guess")
    
    else:
        messagebox.showerror("you lose!", f"You Lose! The word was {word}")



wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=4, columnspan=2)


root.mainloop()
