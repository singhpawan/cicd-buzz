# simple.py

x = 42

def spam():
    print('x is ', x)

def run():
    print('Calling spam')
    # print('Calling the new spam')
    spam()

run()


# Boiler plate code, it checks the name of the module
if __name__ == '__main__':
    print("Running")
    run()



'''
If you use 

python simple.py # it will run the program 
but when you import. All the python modules know their own names. 



'''
