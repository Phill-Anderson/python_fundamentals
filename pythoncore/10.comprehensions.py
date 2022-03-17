x = [x  for x in range(10)] # тодорхойлсон утгуудтай массивийг үүсгэнэ
print(x)

x[9] = 100
print(x)

y = [y * 2  for y in range(10)] # тодорхойлсон утгуудтай массивийг үүсгэнэ
print(y)

z = [[ 1 for z in range(100)] for z in range(5) ]
print(z)

v = [ i for i in range(100) if i % 5 == 0 ] #  100 хүртэлх 5 - д тэгш хуваагдах тоогоор дүүргэнэ
print(v)

dictionary = { i for i in range(100) if i % 5 == 0 }
print(dictionary)

tupled = tuple(i for i in range(100) if i % 5 == 0)
print(tupled)