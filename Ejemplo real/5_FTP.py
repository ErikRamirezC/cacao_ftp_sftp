import os
import shutil

source_folder1 = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Ejemplo real\Carpeta uno\FTP\LQ_files\\"
source_folder2 = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Ejemplo real\Carpeta uno\FTP\Nuevo_LQ\\"
source_folder3 = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Ejemplo real\Carpeta uno\FTP\SD_files\\"

destination_folder = r"C:\Users\LuisErikRamírez\Documents\python\Ejercicios\Ejemplo real\Carpeta dos\Finanzas\Reportes Operativos\FTP\\"

destination_folder1 = 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/FTP/LQ_files/'
destination_folder2 = 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/FTP/Nuevo_LQ/'
destination_folder3 = 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Ejemplo real/Carpeta dos/Finanzas/Reportes Operativos/FTP/SD_files/'

if os.path.isdir(destination_folder):
    print('La carpeta existe.');
    if os.path.isdir(destination_folder1):
        print('La carpeta cuotas x procesamiento existe.');
        for file_name in os.listdir(source_folder1):
            # construct full file path
            source = source_folder1 + file_name
            destination = destination_folder1 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)
    else:
        for file_name in os.listdir(source_folder1):
            # construct full file path
            source = source_folder1 + file_name
            destination = destination_folder1 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)
    if os.path.isdir(destination_folder2):
        print('La carpeta cuotas de intercambio.');
        for file_name2 in os.listdir(source_folder2):
            # construct full file path
            source2 = source_folder2 + file_name2
            destination = destination_folder2 + file_name2
            # move only files
            if os.path.isfile(source2):
                shutil.copy(source2, destination)
                print('Copiando:', file_name2)
    else:
        os.mkdir(destination_folder2);
        for file_name2 in os.listdir(source_folder2):
            # construct full file path
            source2 = source_folder2 + file_name2
            destination = destination_folder2 + file_name2
            # move only files
            if os.path.isfile(source2):
                shutil.copy(source2, destination)
                print('Copiando:', file_name2)
    if os.path.isdir(destination_folder3):
        print('La carpeta  Flote.');
        for file_name in os.listdir(source_folder3):
            # construct full file path
            source = source_folder3 + file_name
            destination = destination_folder3 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)
    else:
        os.mkdir(destination_folder3);
        for file_name in os.listdir(source_folder3):
            # construct full file path
            source = source_folder3 + file_name
            destination = destination_folder3 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)

else:
    os.mkdir(destination_folder)
    print('La carpeta no existe y creando');
    if os.path.isdir(destination_folder1):
        print('La carpeta cuotas x procesamiento existe.');
        for file_name in os.listdir(source_folder1):
            # construct full file path
            source = source_folder1 + file_name
            destination = destination_folder1 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)
    else:
        os.mkdir(destination_folder1);
        for file_name in os.listdir(source_folder1):
            # construct full file path
            source = source_folder1 + file_name
            destination = destination_folder1 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)
    if os.path.isdir(destination_folder2):
        print('La carpeta cuotas de intercambio existe');
        for file_name2 in os.listdir(source_folder2):
            # construct full file path
            source2 = source_folder2 + file_name2
            destination = destination_folder2 + file_name2
            # move only files
            if os.path.isfile(source2):
                shutil.copy(source2, destination)
                print('Copiando:', file_name2)
    else:
        os.mkdir(destination_folder2);
        for file_name2 in os.listdir(source_folder2):
            # construct full file path
            source2 = source_folder2 + file_name2
            destination = destination_folder2 + file_name2
            # move only files
            if os.path.isfile(source2):
                shutil.copy(source2, destination)
                print('Copiando:', file_name2)
    if os.path.isdir(destination_folder3):
        print('La carpeta  Flote existe');
        for file_name in os.listdir(source_folder3):
            # construct full file path
            source = source_folder3 + file_name
            destination = destination_folder3 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)
    else:
        os.mkdir(destination_folder3);
        for file_name in os.listdir(source_folder3):
            # construct full file path
            source = source_folder3 + file_name
            destination = destination_folder3 + file_name
            # move only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('Copiando:', file_name)