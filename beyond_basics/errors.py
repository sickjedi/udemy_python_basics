def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Bullshit division!"


print(divide(1, '0'))
