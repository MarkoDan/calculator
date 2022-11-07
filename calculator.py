msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

operators = ['+', '-', '*', '/']

memory = 0.0
result = 0.0

def main():

    while True:
        print(msg_0)
        x, oper, y = input().split()
        if x == 'M':
            x = memory
        elif y == 'M':
            y = memory

        try:
            float(x), float(y)
            if oper in operators:
                if oper == '/' and float(y) == 0.0:
                    print(msg_3)
                else:
                    calc(x, y, oper)
                    print(result)
                    answer = input(msg_4)
                    if answer == 'y':
                        memory = result
                    answer2 = input(msg_5)
                    if answer2 == 'n':
                        break
            else:
                print(msg_2)
        except ValueError:
            print(msg_1)

def calc(x, y, oper):
    global result
    if oper == "+":
        result = float(x) + float(y)
    elif oper == "-":
        result = float(x) - float(y)
    elif oper == "*":
        result = float(x) * float(y)
    elif oper == "-":
        result = float(x) / float(y)
    return result


if __name__ == '__main__':
    main()



