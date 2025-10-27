#set function
set_1={1, 2, 3, 4, 5}
set_2={5, 7, 3, 2, 1, 0}
set_3={5, 7, 8, 9}
temp=set_1.union(set_2)
print(temp)
diff=set_1.difference(temp)
print(temp)
print(set_1.union(set_2).intersection(set_3))