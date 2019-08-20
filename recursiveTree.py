import turtle

flounder=turtle.Turtle()
flounder.speed(2)
flounder.left(90)
def tree(trunkLength,height):
    if height==0:
        return
    else:
        flounder.forward(trunkLength)
        flounder.left(45)
        tree(trunkLength*.5,height-1)
        flounder.right(90)
        tree(trunkLength*.5,height-1)
        flounder.left(45)
        flounder.backward(trunkLength)
tree(200,4)
turtle.done()
