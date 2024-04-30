from tkinter import *
from tkinter import ttk
import twl as twl


letter_points = {
    "a": 1, "e": 1, "i": 1, "o": 1, "n": 2, "r": 2, "s": 2, "t": 2, "d": 3, "g": 3, "l": 3, "b": 4, "h":4, "p": 4, "m": 4, "u": 4, "y": 4, "c": 5, "f": 5, "v": 5, "w": 5, "k": 6, "j": 7, "x": 7, "q": 8, "z": 8  
}

test_matrix = [
    ["t", "s", "s", "o", "k"],
    ["n", "o", "d", "o", "v"],
    ["m", "a", "p", "e", "n"],
    ["s", "t", "e", "x", "g"],
    ["z", "w", "t", "y", "i"]
]
#Initiate letter variables
letter1_1 = ""
letter1_2 = ""
letter1_3 = ""
letter1_4 = ""
letter1_5 = ""


best_word = ""
best_word_score = 0
test_score = 0
#Initiate the GUI
root = Tk()
root.title("Spellcast Cheat")

#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=5, row=5, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)
#letter1_1_entry = ttk.Entry(mainframe, width=7, textvariable=letter1_1)
#letter1_1_entry = ttk.Entry(mainframe, width=7, textvariable=letter1_2)
#letter1_1_entry = ttk.Entry(mainframe, width=7, textvariable=letter1_3)
#letter1_1_entry = ttk.Entry(mainframe, width=7, textvariable=letter1_4)
#letter1_1_entry = ttk.Entry(mainframe, width=7, textvariable=letter1_5)
#root.mainloop()

# Enter in all the letters in the matrix



# Find a path between the letters that spells a word and counts the score
for i in test_matrix:
    current_index = 0
    for j in i:
        if(current_index +1 < len(i)):
            test_word = j+i[current_index+1]
            if twl.check(test_word):
                for k in test_word:
                    test_score += letter_points.get(k)
                if test_score > best_word_score:
                    best_word = test_word
                    best_word_score = test_score
                test_score = 0
        if(current_index - 1 >= 0):
            test_word = j+i[current_index-1]
            if twl.check(test_word):
                for k in test_word:
                    test_score += letter_points.get(k)
                if test_score > best_word_score:
                    best_word = test_word
                    best_word_score = test_score
                test_score = 0


        current_index +=1

     #iterate
print(best_word)
print(best_word_score)
      


#Find another word and compare it to the previous to see if it's a higher score