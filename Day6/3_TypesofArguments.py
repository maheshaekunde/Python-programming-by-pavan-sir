# ex 1: Positional arguments
# def func(i,j):
#     print(i,j)
#
# func(10,20)     #10 20


# ex 2: Keyword arguments
# def func(i,j):
#     print(i,j)
#
# func(j=10,i=30)     #30 10

# ex 3: default values assigned to positional arguments
# def func(i, j=10):
#     print(i,j)
#func(30,40)        #30, 40
# func(20)        #20 10


# ex 3: default values assigned to keyword arguments
# def func(i, j=10):
#     print(i,j)
#
# func(i=20)      #20 10


# ex 4: keyword arguments
# def greeting(name,mssg):
#     print(mssg+" "+name)
#
# greeting("hello","john")        #john hello
# greeting(name="scott", mssg="goodmorning")      #goodmorning scott


# ex 5: mix position and keyword argument
# def func(a,b,c):
#     print(a,b,c)
#
# # func(c=10,20,30)  #SyntaxError: positional argument follows keyword argument
# func(10,20,c=30)     #10 20 30
# func(10,b=20,30)      #SyntaxError: positional argument follows keyword argument

# ex 6: function can return multiple values.
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(10,20))       #(20, 10)