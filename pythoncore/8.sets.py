x = set()
s = { 4,32, 2, 2 }
print(s)
s.add(5)
print(s) 

print('обьект дотор тухайн утга бна уу', 12 in s )  # тухайн обьект дотор тухайн утга байгаа эсэхийг boolean утга буцаана

s2 = [4,32, 2,2]
print('s2 array дотор тухайн утга бна уу? : ', 2 in s2  )

s3 = { 4,2, 12, 32, 42 }
union = s.union(s3)
print('хооронд нь нэгтгэсэн обьектууд: ' ,union)
difference = s.difference(s3)
print('обьектуудын хоорондох ялгаа:', difference)
intersection = s.intersection(s3)
print('intersection : ', intersection)