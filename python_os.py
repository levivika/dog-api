import os
#создать папку
#os.mkdir('folder')
#проверка существования пути
if os.path.exists('folder'):
    with open('folder/file.txt', 'w') as file: #создать файл в папке
        pass



if os.path.exists('folder'):
    print('ok')

#явл ли фолдер файлом
if os.path.isfile('folder'):
    print('+')
else:
    print('-')

#список файлов в папке
print(os.listdir('folder'))


