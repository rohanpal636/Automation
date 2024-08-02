file= open('test.txt')
#print(file.read(6))

#read one single line at a time readline() #[read one single line at a time readline()]
#print(file.readline())
#print(file.readline())

#print line by line using reading method

# line= file.readline()
# while line!="":
#     print(line)
#     line= file.readline()
# print(file.readlines())

for line in file.readlines():
    print(line)


file.close