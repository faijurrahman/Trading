import os

stream = os.popen('echo something')
output = stream.read()
print(output)



