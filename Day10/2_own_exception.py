# ex 1: raising our own exception.
def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")

enterage(10)        #even
enterage(5)         #odd
enterage(-5)        #ValueError: Only Integers are allowed