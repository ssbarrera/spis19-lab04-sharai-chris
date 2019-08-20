import turtle
crush=turtle.Turtle()
def snowflake(sideLength,levels):   
        snowflakeside(sideLength,levels)
        crush.right(120)
        snowflakeside(sideLength,levels)
        crush.right(120)
        snowflakeside(sideLength,levels)
        return 

def snowflakeside(sideLength,levels):
    if levels==0:
        crush.forward(sideLength)
    else:
        snowflakeside(sideLength/3,levels-1)
        crush.left(60)
        snowflakeside(sideLength/3,levels-1)
        crush.right(120)
        snowflakeside(sideLength/3,levels-1)
        crush.left(60)
        snowflakeside(sideLength/3,levels-1)

snowflake(280,4)


