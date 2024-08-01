import os

fd = os.open('testdata.txt',os.O_RDWR)
os.write(fd,b'Hello I am writing')
os.close(fd)