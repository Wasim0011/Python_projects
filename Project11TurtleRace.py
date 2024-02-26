import random
from turtle import Turtle, Screen
width, height=700, 600
colour_list=["red", "green", "pink", "yellow", "black", "brown", "blue", "orange", "aquamarine1", "coral"]
def no_of_turtle():
    count=0
    while True:
        count=input("How many turtles you want to race(2-10): ")
        if count.isdigit(): #for checking digit input
            count=int(count)
        else:
            print("Please enter a numeric value between 2 to 10")
            continue
        if 2<=count<=10:
            return count
        else:
            print("Input is not given range...Try again!!")

turtles=no_of_turtle()
print(turtles)
tom=Turtle()
s1=Screen()
s1.setup(width, height)  #setting screen size(width, height)
x_spacing=width//(turtles+1)
turtle_list=[]
for i in range(1, turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colour_list[i-1])
    new_turtle.left(90)
    new_turtle.penup()
    new_turtle.goto(-width//2+(i*x_spacing), -height//2+30)
    turtle_list.append(new_turtle)

def race():
    is_race_on=True
    while is_race_on:
        for t in turtle_list:
            distance=random.randrange(1, 20)
            t.forward(distance)
            x,y=t.pos()
            if y>=(height//2-25):
                print(f"The winner is {t.pencolor()} turtle")
                is_race_on=False

race()

s1.mainloop()
