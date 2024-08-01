#Walk me through the directory
import os
for root,dir,files in os.walk("C:\\Users\\Dell\\PycharmProjects\\Py3xATBLearning\\Ex_July\\Ex_05062024"):
    print(f'Current Dir {root}')
    print(f'Sub Dir Dir {dir}')
    print(f'Files dir Dir {files}')
    print(len(files))