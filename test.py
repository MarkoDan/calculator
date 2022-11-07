def calc(x, y, op):
    global result
    if op == "+":
        result = float(x) + float(y)
    elif op == "-":
        result = float(x) - float(y)
    elif op == "*":
        result = float(x) * float(y)
    elif op == "-":
        result = float(x) / float(y)
    return result


memory = 0.0
result = 0.0
start = True

while start:
    print("Enter an equation")
    x, op, y = input().split()
    if x == "M":
        x = memory
    elif y == "M":
        y = memory
    try:
        float(x), float(y)
        if op in "+-*/":
            if op == "/" and float(y) == 0.0:
                print("Yeah... division by zero. Smart move...")
            else:
                calc(x, y, op)
                print(result)
                print("Do you want to store the result? (y / n):")
                ans1 = input()
                if ans1 == "y":
                    memory = result
                print("Do you want to continue calculations? (y / n):")
                ans2 = input()
                if ans2 == "n":
                    start = False
                    break
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
