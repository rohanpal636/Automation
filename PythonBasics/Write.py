# file = open("test.txt")
# file.close()

# read the file store all the line in the list
#reverse the lis
#write the list back to the fikle
with open("test.txt", "r") as reader:
    content= reader.readlines()
    reversed(content)
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)

