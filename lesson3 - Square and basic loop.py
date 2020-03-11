import turtle
from turtle import *

######## צבעים במסך #########
######## colors #########
turtle.bgcolor("blue")
pencolor("red")

######## ריבוע ###########
########Square###########
def square():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)

#####################
# תרגיל - תכין מלבן
# תרגיל - תכין משולש
#####################

# צפה בדוגמה הבאה
def mehomash():
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)

# תראה איך ניתן לבצע זאת בצורה קצרה יותר
def mehomash_loop():
    for i in range(6):
        forward(100)
        left(60)

# תרגיל הכן את המרובע שעשינו קודם עם לולאה
# square()
# mehomash()
# mehomash_loop()

#########רשום מתחת לשורה זו את הקוד שלך במקום הקוד שמכין ריבוע ############

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)








######## שורה אחרונה #########
######## last line #########
mainloop()