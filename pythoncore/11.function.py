def myFunction(x, y):
    print('өгсөн утгууд: ',x,y)
    return x*y

val = myFunction(5,6)
print(val)

def example(x,y):
    print(x,y)
    return x+y, x-y, x/y

val1, val2, val3 = example(10, 5) # олон утга буцаадаг функцыг ингэж задалж бна
print(val1, val2, val3)    

def func(x,y, z = None):
    print(x,y,z)

func('hello', 'world')