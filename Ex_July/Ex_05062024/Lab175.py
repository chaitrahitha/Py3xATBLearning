import  os
print(os.name)
print(os.getcwd())
os.chdir("C:\\Users\\Dell\\PycharmProjects\\Py3xATBLearning\\Ex_July")
print(os.getcwd())
print(os.listdir("C:\\Users\\Dell\\PycharmProjects\\Py3xATBLearning\\Ex_July"))
# os.mkdir("Chaitra")
os.chdir("C:\\Users\\Dell\\PycharmProjects\\Py3xATBLearning\\Ex_July\\Ex_05062024")
print(os.getcwd())
mtime = os.path.getmtime("testdata.txt")
print(mtime)
import time
print(time.gmtime(mtime))