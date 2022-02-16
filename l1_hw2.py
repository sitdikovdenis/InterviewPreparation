# 2. Дополнить следующую функцию недостающим кодом:
# def print_directory_contents(sPath):
# """
# Функция принимает имя каталога и распечатывает его содержимое
# в виде «путь и имя файла», а также любые другие
# файлы во вложенных каталогах.
#
# Эта функция подобна os.walk. Использовать функцию os.walk
# нельзя. Данная задача показывает ваше умение работать с
# вложенными структурами.
# """

import os


def print_directory_contents(sPath):
    file_and_dirs = os.listdir(sPath)
    for file_or_dir in file_and_dirs:
        path = f'{sPath}/{file_or_dir}'
        print(path)
        if os.path.isdir(path):
            print_directory_contents(path)


print_directory_contents('/home/sitdikovdr/gb_learning/course_2')
