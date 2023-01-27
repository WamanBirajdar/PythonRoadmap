# factorial program using decorators

memory={}
def memoize_factorial(f):
    def inner(num):
        if num not in memory:
            memory[num]=f(num)
            print("result saved in memory")
        else:
            print("returing result from saved memory")
        return memory[num]

    return inner


@memoize_factorial
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)


print(fact(5))
print(fact(5))
