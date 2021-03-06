import os
import platform
import sys

# Write code to get your OS name
# Read about how to use the platform module
# to achieve this.
def getOSName():
    '''
    >>> name = getOSName()
    >>> name in {'Linux', 'Windows', 'Darwin'}
    True
    '''
    return platform.system()

# Write code to find the function name
# given a function call.
def findFunc(block):
    '''
    >>> findFunc('\n  rectangle(50,100)')
    'rectangle'
    >>> findFunc('add(50,100)')
    'add'
    >>> findFunc('      onlyTwo(5,10,13)')
    'onlyTwo'
    '''
    word = ""

    for i in range(len(block)):
      if block[i].isalpha():
        word += block[i]
      elif word != '':
        break

    return word

# Write filterErrors, which takes a
# list of strings as an input and
# outputs a list containing only
# the strings that DONT have the
# substring 'ok' in them.
def filterErrors(strList):
    '''
    >>> S = ['hello', 'error in module 5', 'test ok', 'everying ok']
    >>> filterErrors(S)
    ['hello', 'error in module 5']
    '''
    new_list = []
    for each in strList:
      if 'ok' not in each:
        new_list.append(each)

    return new_list

# This function is a crucial part of parsing the
# block of text from each doctest.
# It takes in a string that represents
# ONE test that failed.
def findError(block):
    # split the block by '\n', generating. a list of lines
    li = block.split('\n')
    # strip the white space from each line of text in the list
    for i in range(len(li)):
      li[i] = li[i].strip(' ')
    # Look for the line that contains 'Error:' in the list of lines.
    for i in range(len(li)):
      if 'Error:' in li[i]:
    # Then, parse the line number that the error occurred on (this will be
    # two lines before the line where 'Error:' occurs) You will have to split this
    # line by a comma and then strip the white space to revtrieve the actual line number.
        s = li[i-2].split(',')
        line = s[1].strip(' ')
        line += ' '
        line_number = int(line[line.index(' ')+1:line.rindex(' ')])
    # In addition, you should parse the line of code that caused the error and the
    # type of error itself, which will be the next two lines after the line number line.
    # If you are confused, debug your code and print out what each block looks like to
    # get a better idea of what's happening.
    # You should return a 3-tuple in the form of:
    #      (line number, code, error_type)
        code = li[i-1].strip(' ')
        error_type = li[i].strip(' ')
        return (line_number, code, error_type)

# Write the function to run the doctest in
# the terminal. You should output the results
# of the doctest to a text file, which is what
# the docFilename variable represents.
# This function does not need any outputs.
# Make use of the OS module.
def runDoctest(pyfile, docFilename):
    # IMPORTANT: you should write the command-line command
    # in accordance to the operating system you're using.
    # Use the getOSName() function in here.
    # You will either use python or python3 based on your OS.
    oper_sys = getOSName()
    if oper_sys == 'Darwin':
      a = 'python3 -m doctest -v ' + pyfile + ' > ' + docFilename
    else:
      a = 'python -m doctest -v ' + pyfile + ' > ' + docFilename
    os.popen(a)


# Write the function to get the output of the doctest
# Essentially, you have to read the text file that
# contains the result of the doctest.
def getDoctestOutput(docFilename):
    # Read in the doctest output from the file
    doc = ''
    doctest = open(docFilename, "r")
    for each in doctest:
      doc += each
    # Split your full doctest string by the string 'Trying:'
    doc = doc.split('Trying:')
    # Filter the errors, store in new list
    error_list = filterErrors(doc)
    # Initialize a new list, and
    # for each error in the error list,
    # append a 4-tuple in the form of:
    #      (function, line number, code, error_type)
    li = []
    for each in error_list:
      k = findError(each)
      func = findFunc(each)
      if k != None:
        li.append((func,k[0],k[1],k[2]))
    # Return that list of tuples
    # return li
    return li

# Write a main function that puts together all of your code.
# In this function, you should prompt for a Python file name to
# doctest and then choose a file name to store the output in.
# Then, you should run the doctest then retrieve the errors.
# If no error was found, return 'No errors found.' Otherwise,
# for each error, format an output to present the errors that occured
# and their associated function / line numbers / code / type.
def main():
    f = input('Enter file to doctest: ')
    runDoctest(f, 'out.txt')
    li = getDoctestOutput('out.txt')
    for each in li:
      print()
      print('Error in function: ' + each[0])
      print('Line {}:'.format(each[1]))
      print()
      print('\t' + each[2])
      print()
      print(each[3])
      print()
      print('------------')

# Uncomment the code below to make your program run.

main()











