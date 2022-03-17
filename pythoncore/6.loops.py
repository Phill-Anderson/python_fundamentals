from xml.dom.minidom import Element


for i in range(10):
    print(i)

x= [20,21,23,25,30,40,31]
for i in x :
    print(i)
for i in range(1,10, 2):
    print(' range: ', i) 

for i in range( len(x) ) :
    print('тухайн индекс=',i)
    print('тухайн утга =',x[i])    

for i, element in enumerate(x):
    print(i, element)


### while loop
i=0
while i < 10 :
    print('run')
    i+=1

while True:
    print('runs ...')
    i+=1
    while True:
        if i == 5:
            break
