msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [
    msg_0,
    msg_1,
    msg_2,
    msg_3,
    msg_4,
    msg_5,
    msg_6,
    msg_7,
    msg_8,
    msg_9,
    msg_10,
    msg_11,
    msg_12
]

def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1:
        msg += msg_7
    if (v1 == 0 or v2 == 0) and v3 != "/":
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

memory = 0.0

while True:
    print(msg_0)
    x, oper, y = input().split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        check(x, y, oper)
        result = operations[oper](x, y)
        print(result)
        if input(msg_4) == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12:
                    print(msg_[msg_index])
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break 
            else:
                memory = result
        if input(msg_5) == "n":
            break

    except ValueError:
        print(msg_1)
    except KeyError:
        print(msg_2)
    except ZeroDivisionError:
        print(msg_3)

