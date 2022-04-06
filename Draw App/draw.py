from turtle import Turtle

TRIANGLE = 3
SQUARE = 4

DRAW_LIST = ['triangle', 'square']
EXIST_LIST = ['stop', 'n', 'nope', 'exit']


class Tim(Turtle):

    def __init__(self, display):
        super().__init__()
        self.should_continue = True
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x=-40, y=0)
        self.display = display
        self.choice = self.display.textinput(title="WHAT DOYOU WANT TO DRAW", prompt='Enter your response;\n')

    def checking_answer(self):
        while self.should_continue:
            def game(number_of_side):
                angle = 360 / number_of_side
                for _ in range(number_of_side):
                    self.forward(100)
                    self.left(angle)

            if self.choice == 'triangle':
                self.pendown()
                game(TRIANGLE)
                break

            elif self.choice.lower() == 'square':
                self.pendown()
                game(SQUARE)
                break
