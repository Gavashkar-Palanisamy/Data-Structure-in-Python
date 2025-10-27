#Dictionary get fucntion.py
dic_1={1:'suriya', 2:'yazhi', 3:'sangeetha'}
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