x = [ 0,1,2,3,4,5,6,7,8,9 ]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"

# [start:stop:step]
slicedx = x[0:4:2]
print(slicedx)

slicedy = y[1:4:2]
print('taslasan array =',slicedy)

sliceds = s[0:5:2]
print('taslasan string = ',sliceds)

z = x[::-1]
print('ene yu we?', z) # массивийг reverse хийнэ
c = x[::2]
print('::2 ', c) # 2 2 -оор алгасаж авна
