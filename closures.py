"""
x = 12

def foo():
    global x
    def shrek():
        print(x)

    shrek()


foo()


ou


def foo():
    
    def shrek():
        global x
        print(x)

    shrek()


foo()



"""


def exp(N):

    def eleva(x):
        return x**N
    
    return eleva


p = exp(3)


print(p(2))



