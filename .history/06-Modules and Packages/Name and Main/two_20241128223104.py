#two.py

import one

def my_func_two():
    print ("Hello World! from two.py")

print("Top level, in two.py !")

#so at the end of file we will see something like this
if __name__ == "__main__":
    my_func()
    print("one.py my_func() is called directly!")
else:
    print("one.py my_func() is imported!.")