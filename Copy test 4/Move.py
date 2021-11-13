import glob
import os
import shutil

src_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Copy test 4\Carpeta uno\MOVS_CTAEJE_files"
dst_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Copy test 4\Carpeta dos\Mov_new\\"

foldername='202107'

# move file whose name starts with string 'emp'
pattern = src_folder + "\MOVS_CTAEJE_{0}*".format(foldername)
for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.copy(file, dst_folder + file_name)
    print('Copiando:', file)