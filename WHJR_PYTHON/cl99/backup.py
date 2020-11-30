import os
import shutil
backup_file = input("Enter the path of the file that you want to backup: ")
backup_dest = input("Enter the path where you want to backup: ")
shutil.copy(backup_file, backup_dest)