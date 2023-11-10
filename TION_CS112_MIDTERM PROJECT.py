from turtle import *
import time
turt = Turtle()
turt.screen.setup(500, 200)

#Setting Variables and Lists to be used. (List starting from 0 Monkey, to 11 Goat)
ZodiacSign = ("Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat")
continuation = True
TurtleTextFont = "Comic Sans MS", 40, "normal" #Font name must be exact, FontSize, Fontstyle(Bold, Italic, etc..)
pencolor("#2041df") #Uses Hexadecimal color codes

#Mainloop of the code
while continuation:
    try:
        #Taking input from the user For a year
        WhatYear = eval(textinput("Zodiac", "Enter a year:"))
        if WhatYear >= 0:
            WhatYear %= 12
            write(ZodiacSign[WhatYear], font=(TurtleTextFont), align="center")
            time.sleep(2)
            continuation = textinput("Continuation", "Continue? (Yes, No)").lower()
            clear()

        #If input is a negative number it will register as invalid
        elif WhatYear < 0:
            write("Negative Number", font=(TurtleTextFont), align="center")
            time.sleep(2)
            continuation = textinput("Continuation", "Continue? (Yes, No)").lower()
            clear()

        #If answer is no exit the loop
        if continuation == "no":
            write("Have a nice day", font=(TurtleTextFont), align="center")
            time.sleep(2)
            break

        elif continuation == "yes":
            continue

    #Takes in to accunt errors when inputting strings instead of integers
    except:
        write("Invalid Input", font=(TurtleTextFont), align="center")
        time.sleep(2)
        clear()
        continue

exit()
done()