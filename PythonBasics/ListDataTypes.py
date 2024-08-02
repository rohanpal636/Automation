#List

values = [1,2,"Rohan",4,5,6,7]
print(values[5])
print(values[-1])
print(values[1:5])
values.insert(3,"Pal")
print(values)
values.append("55")
print(values)
values[1]="Shri"
del values[-1]
print(values)

#tuples
val=(1,2,"Rohan",4.5)
print(val[1])

#Dictionary
dic= {"Rohan":1, 2:"Pal", "c":"Hello"}
print(dic)
print(dic[2])

dict={}
dict["Firstname"]= "Rohan"
dict["Lastname"]= "Pal"
dict["Gender"]= "Male"
print(dict)
print(dict["Gender"])

