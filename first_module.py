'''
__name__ is a special variable provided by python to inform whether the code is being
run from the same file or is being imported as module in another file.

When python runs the file directly it set the __name__ variable as '__main__'.
But when we import a module __name__ becomes equal to the name of the
module being imported.
'''

if __name__ == '__main__':
    #This prints __main__ if this is called in the same file
    print(f'\nThis is called directly. The value of __name__ is "{__name__}".\n')

else:
    #This prints the module name ie 'first_module' if imported in another file
    print(f'\nThis is an imported module. The value of __name__ is "{__name__}"\n')