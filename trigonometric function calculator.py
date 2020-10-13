def main():
    import math
    trig = input('which trigonometric function you want to calculate? ')
    if trig == 'sine' or trig == 'sin':
        a = eval(input('What is the angle measure? '))
        result = math.sin(math.radians(a))
        print('The answer is '+str(round(result,3)))
        main()
    
    elif trig == 'cosine' or trig == 'cos':
        a = eval(input('What is the angle measure? '))
        result = math.cos(math.radians(a))
        print('The answer is '+str(round(result,3)))    
        main()
        
    elif trig == 'tangent' or trig == 'tan':
        a = eval(input('What is the angle measure? '))
        result = math.tan(math.radians(a))
        print('The answer is '+str(round(result,3)))    
        main()      
        
    else:
        print('Sorry wrong input')
        main()
        
main()        
