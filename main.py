import math

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

operators = ['+', '-', '/', '*']
oper = ""
x = ""
y = ""
result = ""
m = 0


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
    else:
        return
    print(msg)


def store_mem(result):
    global m
    if is_one_digit(result):
        msg_index = 10
        while True:
            print(msg_[msg_index])
            user = input()
            if user != "y" and user != "n":
                continue
            if user == "n":
                return
            if user == "y" and msg_index < 12:
                msg_index += 1
                continue
            else:
                break
    m = result


while True:
    print(msg_0)  # Enter an equation
    calc = input().split()
    x = calc[0]
    oper = calc[1]
    y = calc[2]

    if x == "M":
        x = m
    if y == "M":
        y = m

    try:
        x = float(x)
    except ValueError:
        print(msg_1)
        continue
    try:
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    check(x, y, oper)

    if oper in operators:
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
    else:
        print(msg_2)
        continue

    print(result)
    print(msg_4)  # "Do you want to store the result? (y / n):"
    user = input()
    if (user == "y"):
        store_mem(result)
    elif (user != "n"):
        print(msg_4)
    print(msg_5)
    user = input()
    if (user == "y"):
        continue
    elif (user == "n"):
        break
    else:
        print(msg_5)