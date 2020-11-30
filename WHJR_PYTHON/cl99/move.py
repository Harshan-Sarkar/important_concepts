import os
import shutil
path = "C://Users//USER//Desktop//WHJR_PYTHON//cl97"
print("before moving files ")
print(os.listdir(path))

source ="C://Users//USER//Desktop//WHJR_PYTHON//cl97//text.txt" 
destination = "C://Users//USER//Desktop//WHJR_PYTHON//"
dest = shutil.move(source, destination)
print("after moving files ")
print(os.listdir(path))