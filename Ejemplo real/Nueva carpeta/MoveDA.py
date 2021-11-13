import glob
import os
import shutil

src_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Ejemplo real\Carpeta uno\FTP\DA_files"
dst_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Ejemplo real\Carpeta dos\Finanzas\DA_files\\"

for i in range(1,13):
    if i<=9:
        print('20210{0}'.format(i))
        name_folder='20210{0}'.format(i)
        if os.path.isdir('C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/DA_files/{0}/'.format(name_folder)):
            print('La carpeta existe.');
            # move file whose name starts with string 'emp'
            pattern = src_folder + "\DA{0}*".format(name_folder)
            for file in glob.iglob(pattern, recursive=True):
                # extract file name form file path
                file_name = os.path.basename(file)
                shutil.copy(file, 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/DA_files/{0}/'.format(name_folder) + file_name)
                print('Copiando:', file)
        else:
            os.mkdir('C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/DA_files/{0}/'.format(name_folder))
            print('La carpeta no existe y creando');
            # move file whose name starts with string 'emp'
            pattern = src_folder + "\DA{0}*".format(name_folder)
            for file in glob.iglob(pattern, recursive=True):
                # extract file name form file path
                file_name = os.path.basename(file)
                shutil.copy(file, 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/DA_files/{0}/'.format(name_folder) + file_name)
                print('Copiando:', file)
    else:
        print('2021{0}'.format(i))
        name_folder='2021{0}'.format(i)
        if os.path.isdir('C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/DA_files/{0}/'.format(name_folder)):
            print('La carpeta existe.');
        else:
            os.mkdir('C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/DA_files/{0}/'.format(name_folder))
            print('La carpeta no existe y creando');

#foldername='202107'

# move file whose name starts with string 'emp'
#pattern = src_folder + "\MOVS_CTAEJE_{0}*".format(foldername)
#for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
   # file_name = os.path.basename(file)
   # shutil.copy(file, dst_folder + file_name)
   # print('Copiando:', file)