def add(num1,  num2):
    res = num1 + num2
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

def multiply(num1, num2):
    res = num1 * num2
    return res

def div(num1, num2):
    if(num2 == 0):
        return "Division by Zero is not possible."
    else:
        res = num1 /num2
        return res