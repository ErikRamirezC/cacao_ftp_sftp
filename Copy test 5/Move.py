from datetime import date
from shutil import copyfile
import os

today = date.today()

d1 = today.strftime("%Y%m%d")
dia = today.strftime("%d")
mes = today.strftime("%m")
anio = today.strftime("%Y")

#Este es el folder de SharePoint (OneDrive)
dest_folder = 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Copy test 5/Carpeta uno/DA_files/{year}{month}/'.format(month=mes, year=anio)
file1_name = 'DA{year}{month}{day}.txt'.format(year=anio, month=mes, day=dia)

#TODO En vez de esto hay que conectarnos a un FTP y hacer la copia desde ahí
file1_folder_path = 'C:/Users/LuisErikRamírez/Documents/python/Ejercicios/Copy test 5/Carpeta dos/Mov_new/'


file1_path = file1_folder_path + file1_name
print('El archivo a copiar es: {0}'.format(file1_path))
if dia=='01':
               #TODO Valiar que la carpeta exista, si no crearla
               os.mkdir(dest_folder)
               print('Cree la carpeta')
else:
               print('No cree la carpeta')

#TODO Ver como copiar desde el SFTP
#Copio el archivo
copyfile(file1_path, dest_folder + file1_name)