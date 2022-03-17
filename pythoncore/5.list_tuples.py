x = [4, True , 'hi']
x.append('hello') # 1 өгөгдөл нэмнэ
print( x )
x.extend(['add new data', 22, False]) # олон өгөгдөл нэмнэ
print(x)
print(' энэ юу вэ? ',x.pop()) #x.pop() - list - ээс төгсгөлийн элемэнтийг авна
print(x[2])

x[0] = 'hey hey hey'
print(x)
y = x # x list - ийг өөрийг нь зааж бна
z = x[:] # x list - ийн хуулбарыг үүсгэж бна
print(z)

# tuples
tupleList = (0,1,2,3,5,10,20,30)
tupleList[0] = 5 # tuple обьектийг өөрчилж (CRUD) болохгүй бөгөөд өөрчлөх цорын ганц боломж нь түүнийг дахин тодорхойлж үүсгэх юм
print(tupleList)

