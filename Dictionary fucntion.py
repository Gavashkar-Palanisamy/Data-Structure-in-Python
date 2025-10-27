#Dictionary get fucntion.py
dic_1={1:'suriya', 2:'yazhi', 3:'sangeetha'}
dic_2={'1':'ram', '2':'3'}
print(dic_1.get(3))

#keys:
dic_1={1:'suriya', 2:'yazhi', 3:'sangeetha'}
print(dic_1.keys())

#value:
dic_1={1:'suriya', 2:'yazhi', 3:'sangeetha'}
print(dic_1.values()) 

print("\nKeys and Values:")
for k, v in dic_1.items():
    print(k, ":", v)

#merge dict
#value:
dic_1={1:'suriya', 2:'yazhi', 3:'sangeetha'}
print(dic_1.values()) 

print("\nKeys and Values:")
#method 1
dic_4={**dic_1, **dic_2}
print(dic_4)

#method 2
dic_5= dic_1 | dic_2
print(dic_5)

#method 2
dic_1 |= dic_2
print(dic_1)