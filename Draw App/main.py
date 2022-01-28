from turtle import Screen
from draw import Tim

restart = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('DRAW APP')


"""ALL OOP CODES GOES IN HERE """
tim = Tim(screen)


tim.checking_answer()



screen.exitonclick()