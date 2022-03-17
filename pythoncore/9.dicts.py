x={ 'key': 4, 'key1': 10}

x['key2'] = 5
print(x)
print( 'key2' in x ) # x - д key2 гэсэн проферти байгаа юу?

print('обьект доторхи утгууд: ',x.values()) 
print('обьект доторхи утгууд: ',list(x.values()))
print('обьект доторхи keys: ', list(x.keys()))

del x['key'] # key - д хамаарах утгыг обьектоос устгана
print('key - г устгасны дараах x обьект: ',x)

for key , value in x.items():
    print(key, value)

for key in x:
    print('end',key, x[key])    

print('end yu bna ...====>',x.items())    