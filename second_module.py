#Here when we import the module the value of __init__ 
#becomes the name of the imported module 'first_module'

import first_module

if __name__ == '__main__':
    print(f"\nThis is called directly inside 'second_module'. The value of __name__ is '{__name__}'\n")