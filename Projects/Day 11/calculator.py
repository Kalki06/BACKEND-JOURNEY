def add(num1, num2):
    res = num1 + num2
    return(res)

def sub(num1, num2):
    res = num1 - num2
    return(res)

def multiply(num1, num2):
    res = num1 * num2
    return(res)

def div(num1, num2):
    try:
        res = num1/ num2
        return res
    except ZeroDivisionError:
        return "Division by Zero is not possible !! "
    
