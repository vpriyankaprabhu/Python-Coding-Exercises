#python one.py
# will make or initialise the built in variable __name__ set value to __main__ stating that this script is run directly and is having logic to execute

def my_func():
    print ("Hello World!")

#so at the end of file we will see something like this
if __name__ == "__main__":
    my_func()

# this file executed will be running only one fucntion definition and hence it gets executed 