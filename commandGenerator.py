import test

import random
import string

def generateCommand():
    return random.choice(test.wordsWithSemicolons)


def WriteFile(name):
    file = open(name,'w') 

    file.write(test.generateLine('x = ' + str(random.choice([1,2,3,4,5,6,7,8,9]))))
    file.write(test.generateIf('x == ' + str(random.choice([1,2,3,4,5,6,7,8,9])))) 
    file.write(test.generateTab())
    file.write(test.generatePrint("'x is \" + str(x)  + \"")) 

    file.close() 

    # file = open(name, 'r') 
    # print (file.read())
    # file.close()

# count = 0
# while (count < 9):
#     cmd_val = random.choice(test.wordsWithSemicolons)
#     print(cmd_val)
#     count = count + 1