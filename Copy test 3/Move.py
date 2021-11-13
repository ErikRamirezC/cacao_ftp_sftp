import os
import shutil

source_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Copy test 3\Carpeta uno\\"
destination_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Copy test 3\Carpeta dos\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('Copiando:', file_name)