#two.py

import one

def my_func_two():
    print ("Hello World! from two.py")

print("Top level, in two.py !")

#so at the end of file we will see something like this
if __name__ == "__main__":
    two.my_func_two()
    print("two.py my_func_two() is called directly!")
else:
    print("two.py my_func_two() is imported!.")