from shutil import copytree
from time import sleep
from os import mkdir

fold_name = input ("Enter the folder name: ")
src = "Шаблоны\\3608 ОЭ"
dst = "Организации\\" + fold_name
copytree(src, dst)
mkdir(dst+"\\Старый ОРД")
print ("Copying complete...")
sleep(2)


