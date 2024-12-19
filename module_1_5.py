immutable_var =([4,5,6],['string','wrong'], 1,2,3,True)
print(type(immutable_var))
print(immutable_var)
print(immutable_var[5])
immutable_var[0][1]=3
print(immutable_var)
immutable_var[1][1]=7
print(immutable_var)
mutable_list =(7,8,'banana','coconut',True)*2
print(mutable_list)
mutable_list =(7,8,'banana','coconut',True)+(1,2,3)
print(mutable_list)