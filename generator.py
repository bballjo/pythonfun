
import test
import commandGenerator

import random
import string

filenames = []
count = 0
while (count < 100):
    string_val = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
    filename = 'candidates/' + string_val + '.py'
    print(string_val)

    commandGenerator.WriteFile(filename)

    # print (commandGenerator.generateCommand())
    filenames += [filename]
    count += 1

for name in filenames:
    exec(compile(open(name, "rb").read(), name, 'exec'))




