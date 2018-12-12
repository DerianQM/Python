import os

for f in os.scandir():
    if f.is_dir():
        os.rmdir(f)

    
