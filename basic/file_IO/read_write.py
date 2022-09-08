# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

def writing_test():
    with open('newfile.txt', 'a') as f:
        f.write('first line')
        f.write('second line')
# writing_test()
