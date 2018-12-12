import os

subdir = [f.path for f in os.scandir()if f.is_dir()]
print(subdir) 
