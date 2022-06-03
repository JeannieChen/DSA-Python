def func3():
    print("3")

def func2():
    func3()
    print("2")

def func1():
    func2()
    print("1")

func1()
