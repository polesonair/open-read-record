import os
import operator

files_list = os.listdir(path='files/')
files_dct = {}

# Добавляем к именам файлов путь к папке
for i in range(len(files_list)):
    files_list[i] = 'files/' + files_list[i]

#  Получаем имена файлов, число строк в файлах, помещаем в словарь имя_файла:число строк
for read_file in files_list:
    with open(read_file, 'r', encoding='utf-8') as current_file:
        current_text = current_file.readlines()
    count = len(current_text)
    files_dct[read_file] = count

files_sorted = sorted(files_dct.items(), key=operator.itemgetter(1))

with open('files/out.txt', 'w', encoding='utf-8') as file_out:
    for i in files_sorted:
        file_out.write(i[0][6:]+'\n')  # Удаляем из имени путьк  фалу и записываем в новый файл
        file_out.write(str(i[1])+'\n')  # Записываем число строк в текущем файле
        # Читаем стрки из файлов и записываем в ноый файл
        with open(i[0], 'r', encoding='utf-8') as reading_file:
            for line in reading_file:
                file_out.write(line)