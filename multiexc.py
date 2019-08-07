try:
    a=4
    if a<4:
        b=a/a-3
    print(b)
except(ZeroDivisionError,NameError):
    print("errors are handled")
