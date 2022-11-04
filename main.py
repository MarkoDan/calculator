msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

operators = ['+', '-', '*', '/']

while True:
    memory = 0
    m = memory
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(' ')
    if x.isalpha() or y.isalpha():
        print(msg_1)
    elif oper not in operators:
        print(msg_2)
    else:
        x = float(x)
        y = float(y)
        result = 0
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y != 0:
            result = x / y
        
        if y == 0: 
            print(msg_3)
        else:
            print(result)
            choise = input(msg_4)
            if choise == 'y':
                memory = memory + result
            continue_or_not = input(msg_5)
            if continue_or_not == 'y':
                continue
            else:
                print(m)
                break
            



