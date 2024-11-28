#python one.py
# will make or initialise the built in variable __name__ set value to __main__ stating that this script is run directly and is having logic to execute

def my_func():
    print ("Hello World! from one.py")

print("Top level, in one.py !")

#so at the end of file we will see something like this
if __name__ == "__main__":
    my_func()
    print("one.py my_func() is called directly!")
else:
    print("one.py my_func() is imported!.")

# this file executed will be running only one fucntion definition and hence it gets executed 