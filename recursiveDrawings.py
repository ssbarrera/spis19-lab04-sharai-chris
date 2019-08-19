import turtle 
#naming our cute anonymous turtle: poliwag
poliwag=turtle.Turtle()

def spiral(initialLength, angle, multiplier):
    ''' recursively draw a spiral '''
    #base case for our recursive function 
    if int(initialLength)==1:
        return
    #make poliwag go forward and turn left recursively as 
    #parameter initialLength shrinks until reaches base case
    else:
        poliwag.forward(initialLength)
        poliwag.left(angle)
        spiral(initialLength*multiplier,angle,multiplier)

spiral(300,50,.8)

