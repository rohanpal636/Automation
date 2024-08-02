ItemsInCart=0
if ItemsInCart!=2:
    # raise Exception("Products cart count not matching")
    pass
assert(ItemsInCart==0)


#try, catch

#The below code will give you error
# with open("testlog.txt", "r") as reader:
#     reader.read()

#but try exception won't
try:
    with open("testlog.txt", "r") as reader:
        reader.read()
except:
    print("Somehow I reached this block because there is failure in try block")

try:
    with open("test.txt", "r") as reader:
        reader.read()
except:
    print("Somehow I reached this block because there is failure in try block")

try:
    with open("testlog.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")

