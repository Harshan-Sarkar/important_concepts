import os
import shutil

# COPY FILES
path = "C://Users//USER//Desktop//WHJR_PYTHON//cl97"
print("before copying files ")
print(os.listdir(path))

source ="C://Users//USER//Desktop//WHJR_PYTHON//cl97//text.txt" 
destination = "C://Users//USER//Desktop//WHJR_PYTHON//cl97//text123.txt"
dest = shutil.copy(source, destination)
print("after copying files ")
print(os.listdir(path))


