import re
import random
import numpy as np
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import Text, Tk
import tkinter.font as tkFont

#Declare variables
primary_color = '#9cc2ff'
secondary_color = "#fff652"
victory_color = "#52ff66"
row_num = 1
i = 0
score = 0


#Create database for words
file = open("/usr/share/dict/words", "r")
words = re.sub("[^\w]", " ",  file.read()).split()
word_db = [word.upper() for word in words if len(word) == 5]
word_db = list(set(word_db))

#Define Functions
def generate_word(word_db: str[list]) -> str:
    return word_db[random.randint(0, len(word_db) - 1)]

def new_game():
    global hidden_word
    hidden_word = generate_word(word_db)
    secret_display["text"] = "* * * * *"
    for entry in entries_list:
        entry["disabledbackground"] = "SystemButtonFace"
        entry["state"] = NORMAL
        entry.delete(0, "end")
        if entry not in row_1:
            entry["state"] = DISABLED
    for button in buttons_list:
        if button == button_1:
            button["state"] = NORMAL
        else:
            button["state"] = DISABLED
    
    if __name__ == "__main__":
        print(hidden_word)

def collect_answ():
    active = False
    char_index = set()
    rounds = 0
    for button, entries in grid_dict.items():
        rounds += 1
        if button["state"] == NORMAL:
            answ = "".join([char.get() for char in grid_dict[button]]).upper()
            button["state"] = DISABLED
            active = True
            for i, entry in enumerate(entries):
                entry["state"] = DISABLED
                if answ[i] == hidden_word[i]:
                    char_index.add(i)
                    entry["disabledbackground"] = primary_color
                    entry["disabledforeground"] = "#131313"
                elif answ[i] in hidden_word:
                    entry["disabledbackground"] = secondary_color
                    entry["disabledforeground"] = "black"
                else: 
                    pass
            if answ == hidden_word:
                tk.messagebox.showinfo(message = "You Win!")
                active = False
                button["state"] = DISABLED
                score_display["text"] += 1
                for entry in entries:
                    entry["disabledbackground"] = victory_color
            elif len(answ) != 5:
                tk.messagebox.showinfo(message = "Error - Each entry box must contain 1 letter")
            elif answ != hidden_word and rounds == 6:
                tk.messagebox.showinfo(message = "Sorry, you lose.")
                button["state"] = DISABLED
            else:
                pass
        elif active:
            button["state"] = NORMAL
            active = False
            for i, entry in enumerate(entries):
                entry["state"] = NORMAL
                if i in char_index:
                    entry.insert(0, answ[i])
                    entry["state"] = DISABLED
                    entry["disabledbackground"] = primary_color
                    entry["disabledforeground"] = "#131313"

#Hidden Word Variable
hidden_word = generate_word(word_db)

#Build Window
window = tk.Tk()
window.geometry("430x450")
window.configure(bg = "#131313")

#Build MyWordle Label
my_wordle = tk.Label(window, text = "MyWordle", bg = primary_color, width = 40, font = 2)
my_wordle.grid(row = 0, column = 0, columnspan = 100, pady=15)

#Build Entries
entry_00 = tk.Entry(master=window, width=5)
entry_01 = tk.Entry(master=window, width=5)
entry_02 = tk.Entry(master=window, width=5)
entry_03 = tk.Entry(master=window, width=5)
entry_04 = tk.Entry(master=window, width=5)

entry_05 = tk.Entry(master=window, width=5, state = DISABLED)
entry_06 = tk.Entry(master=window, width=5, state = DISABLED)
entry_07 = tk.Entry(master=window, width=5, state = DISABLED)
entry_08 = tk.Entry(master=window, width=5, state = DISABLED)
entry_09 = tk.Entry(master=window, width=5, state = DISABLED)

entry_10 = tk.Entry(master=window, width=5, state = DISABLED)
entry_11 = tk.Entry(master=window, width=5, state = DISABLED)
entry_12 = tk.Entry(master=window, width=5, state = DISABLED)
entry_13 = tk.Entry(master=window, width=5, state = DISABLED)
entry_14 = tk.Entry(master=window, width=5, state = DISABLED)

entry_15 = tk.Entry(master=window, width=5, state = DISABLED)
entry_16 = tk.Entry(master=window, width=5, state = DISABLED)
entry_17 = tk.Entry(master=window, width=5, state = DISABLED)
entry_18 = tk.Entry(master=window, width=5, state = DISABLED)
entry_19 = tk.Entry(master=window, width=5, state = DISABLED)

entry_20 = tk.Entry(master=window, width=5, state = DISABLED)
entry_21 = tk.Entry(master=window, width=5, state = DISABLED)
entry_22 = tk.Entry(master=window, width=5, state = DISABLED)
entry_23 = tk.Entry(master=window, width=5, state = DISABLED)
entry_24 = tk.Entry(master=window, width=5, state = DISABLED)

entry_25 = tk.Entry(master=window, width=5, state = DISABLED)
entry_26 = tk.Entry(master=window, width=5, state = DISABLED)
entry_27 = tk.Entry(master=window, width=5, state = DISABLED)
entry_28 = tk.Entry(master=window, width=5, state = DISABLED)
entry_29 = tk.Entry(master=window, width=5, state = DISABLED)

entries_list = [
    entry_00, entry_01, entry_02, entry_03, entry_04, entry_05, entry_06, entry_07, entry_08, entry_09, \
    entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18, entry_19, \
    entry_20, entry_21, entry_22, entry_23, entry_24, entry_25, entry_26, entry_27, entry_28, entry_29
]

#Add Entries to Grid
row_num = 1
i = 0
score = 0

for entry in entries_list:
    entry.grid(row = row_num, column = i, padx = 5, pady = 5)
    i += 1
    if i == 5:
        i = 0
        row_num += 1

#Define Grid Variables
entries_list = [
    entry_00, entry_01, entry_02, entry_03, entry_04, entry_05, entry_06, entry_07, entry_08, entry_09, \
    entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18, entry_19, \
    entry_20, entry_21, entry_22, entry_23, entry_24, entry_25, entry_26, entry_27, entry_28, entry_29
]
row_1 = [entry_00, entry_01, entry_02, entry_03, entry_04]
row_2 = [entry_05, entry_06, entry_07, entry_08, entry_09]
row_3 = [entry_10, entry_11, entry_12, entry_13, entry_14]
row_4 = [entry_15, entry_16, entry_17, entry_18, entry_19]
row_5 = [entry_20, entry_21, entry_22, entry_23, entry_24]
row_6 = [entry_25, entry_26, entry_27, entry_28, entry_29]

#Create Buttons
button_1 = tk.Button(master = window, text = "Submit", command = collect_answ)
button_2 = tk.Button(window,text = "Submit", command = collect_answ)
button_3 = tk.Button(window,text = "Submit", command = collect_answ)
button_4 = tk.Button(window,text = "Submit", command = collect_answ)
button_5 = tk.Button(window,text = "Submit", command = collect_answ)
button_6 = tk.Button(window,text = "Submit", command = collect_answ)
buttons_list = [button_1, button_2, button_3, button_4, button_5, button_6]

#Add Buttons to Grid
for i, button in enumerate(buttons_list):
    button.grid(row = i + 1, column = 6, pady = 5, padx = 5)
    if button != button_1:
        button["state"] = DISABLED

#Miscellaneous Labels and Buttons
secret_label = tk.Label(window, text = "Hidden Word: ", bg = primary_color)
secret_label.grid(row = 7, sticky = "w", column = 1, columnspan = 200, pady = (25, 0))

secret_display = tk.Label(window, text = "* * * * *", bg = "black", fg = "white")
secret_display.grid(row = 7, sticky = "w", column = 3, columnspan = 200, pady = (25,0))

score_label = tk.Label(window, text = "Score: ", bg = primary_color)
score_label.grid(row = 8, sticky = "w", column = 1, columnspan = 200, pady = (10, 0))

score_display = tk.Label(window, text = 0, fg = 'white', bg = 'black')
score_display.grid(row = 8, sticky = "w", column = 3, columnspan = 200, pady = (10, 0))

new_game_button = tk.Button(window, text = "New Game", bg = primary_color, command = new_game)
new_game_button.grid(row = 9, sticky = "w", column = 1, columnspan = 200, pady = (25, 0))

quit_game = tk.Button(window, text = "Quit Game", bg = primary_color, command = window.quit)
quit_game.grid(row = 9, sticky = "w", column = 3, columnspan = 200, pady = (25, 0))


#Define Board Variables
row_1 = [entry_00, entry_01, entry_02, entry_03, entry_04]
row_2 = [entry_05, entry_06, entry_07, entry_08, entry_09]
row_3 = [entry_10, entry_11, entry_12, entry_13, entry_14]
row_4 = [entry_15, entry_16, entry_17, entry_18, entry_19]
row_5 = [entry_20, entry_21, entry_22, entry_23, entry_24]
row_6 = [entry_25, entry_26, entry_27, entry_28, entry_29]

grid_dict = {
    button_1: row_1,
    button_2: row_2,
    button_3: row_3,
    button_4: row_4,
    button_5: row_5,
    button_6: row_6,
}

#Run loop
if __name__ == "__main__":
    window.mainloop()
