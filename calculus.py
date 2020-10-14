def f(x):
    return x**2

def derivative(x):
    h=1./1000.
    rise= f(x+h) - f(x)
    run = h
    slope = rise/run
    return slope

def integral(startingx,endingx,numberofrectangles):
    width =(float(endingx)-float(startingx))/numberofrectangles
    runningsum=0
    for i in range(numberofrectangles):
        height = f(startingx + i*width)
        area = height*width
        runningsum += area
    return runningsum    