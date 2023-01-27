# best example of destrucotr


class employee:

    #initializing
    def __init__(self) -> None:
        print("EMployee created")

    #callinf destructor
    def __del__(self):
        print("Destructor called")


def create():
    print("Making a function")
    o=employee()
    print("function end")
    return o

obj=create()
print("program end")
