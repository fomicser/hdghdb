import random
import turtle
import numpy as np
import pandas as pd

# a = [2, 3, 5, 1, 6, 8, 4, 10, 7, 9]
#
# a = random.randint(100, 999)
#
# b = (a % 10)
# c = (a // 10)
# d = (c % 10)
# c = (c // 10)
# sum = (b + c + d)
# print(a, sum)
#
# rand = random.randint(1, 100000000)
# print(rand)
# while rand != 0:
#     a += (rand % 10)
#     rand //= 10
#
# print(a)
#
# a = random.randint(1, 100)
# s = ((4 * 3.14) / a ** 2)
# v = ((3.14 * a ** 3) / 3)
#

# print(a)
# print(s)
# print(v)
# n = len(a)
#
# for i in range(1, n):
#     for j in range(1, n - i + 1):
#         if a[j] > a[j - 1]:
#             a[j], a[j - 1] = a[j - 1], a[j]
#
# num = int(input("Enter the number: "))
# list1 = []
# for i in range(num):
#     list1.append([])
#     list1[i].append(1)
#     for j in range(1, i):
#         list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
#     if (num != 0):
#         list1[i].append(1)
# for i in range(num):
#     print(" " * (num - i), end=" ", sep=" ")
#     for j in range(0, i + 1):
#         print('{0:6}'.format(list1[i][j]), end=" ", sep=" ")
#     print()
# def polindrom():
#     a = str(input())
#     b = a[::-1]
#
#     if a == b:
#         print("ВЕЛИКИЕ ХЭШ БОБУСЫ ЭТО ЖЕ ПОЛИНДРОМ")
#     else:
#         print('не ну так не интересно')
#
#
# str1 = "sfsdfd gvhugh qwertyuiop[]"
#
#
# def count():
#     c = 0
#     b = 0
#     lst = str1.split(' ')
#     for i in range(len(lst)):
#         c = len(lst[i])
#         if c > b:
#             b = c
#         else:
#             pass
#         if c == 0:
#             print(c)
#
#     return b
#
# print(count())
#
# with open('input.txt') as file:
#     file.read()
# def read_matrix(file):
#     line = file.readline()
#     matrix = []
#     while line != '\n' and line != '':
#         matrix.append([int(x) for x in line.split()])
#         line = file.readline()
#     return matrix
#
# f_in = open("input.txt", 'r')
# a = read_matrix(f_in)
# print(a)
# b = read_matrix(f_in)
# print(b)

# for i in range
#
# import argparse
# import sys
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def conv(x, y):
#     """
#     Вычисляет свертку двух матриц
#     :param x: оригинал
#     :param y: ядро свертки, не должно быть больше оригинала
#     :return: возвращает матрицу-карту признаков
#     """
#     c = []
#     for i in range(len(x) - len(y) + 1):
#         c.append([])
#         for j in range(len(x[0]) - len(y[0]) + 1):
#             c[i].append(calc(x[i:(i + len(y))], y, j))
#     return c
#
#
# def calc(subx, y, s_col):
#     """
#     Вычисляет "наложение" 2 двух матриц одного размера (элементы с одинаковыми индексами перемножаются и добавляются к
#     результату)
#     :param subx: "подматрица" Х того же размера, что и ядро
#     :param y: матрица-ядро свертки
#     :param s_col: index-number of column in matrix 'x'
#     :return: возвращает сумму произведений элементов матриц
#     """
#     summ = 0
#     for i in range(len(y)):
#         for j in range(len(y[0])):
#             summ += subx[i][s_col + j] * y[i][j]
#     return summ
#
#
# def read_matrix(file):
#     """
#     Читает матрицу из заданного файла
#     :param file: файл, из которого нужно читать
#     :return: возвращает матрицу
#     """
#     line = file.readline()
#     matrix = []
#     while line != '\n' and line != '':
#         matrix.append([int(x) for x in line.split()])
#         line = file.readline()
#     return matrix
#
#
# def write_matrix(file, matrix):
#     """
#     Записывает матрицу в заданный файл
#     :param file: файл, в который нужно записать матрицу
#     :param matrix: матрица
#     """
#     for i in range(len(matrix)):
#         file.writelines(' '.join(map(str, matrix[i])) + '\n')
#
#
# def is_correct(matrix):
#     """
#     Проверка матрицы на корректность
#     :param matrix: матрица
#     :return: результат (корректна матрица или нет)
#     """
#     count = len(matrix[0])
#     for i in range(1, len(matrix)):
#         if len(matrix[i]) != count:
#             return False
#     return True
#
#
# def visualize(orig, core, result):
#     """
#     Визуализирует результат операции свертки
#     :param orig: оригинал
#     :param core: ядро
#     :param result: карта признаков
#     """
#     fig = plt.figure(figsize=(10, 7))
#     rows = 1
#     cols = 3
#
#     a = np.array(orig)
#     b = np.array(core)
#     res = np.array(result)
#
#     fig.add_subplot(rows, cols, 1)
#     plt.matshow(a, fignum=False)
#     plt.axis('off')
#     plt.title("Оригинал")
#
#     fig.add_subplot(rows, cols, 2)
#     plt.matshow(b, fignum=False)
#     plt.axis('off')
#     plt.title("Ядро")
#
#     fig.add_subplot(rows, cols, 3)
#     plt.matshow(res, fignum=False)
#     plt.axis('off')
#     plt.title("Карта признаков")
#
#     plt.colorbar()
#     plt.show()
#
#
# def main():
#     parser = argparse.ArgumentParser(description='Вычисляет свертку матриц')
#     parser.add_argument('in_name', type=str, help='название входного файла')
#     parser.add_argument('out_name', type=str, help='название выходного файла')
#     parser.add_argument('show_res', type=bool, help='визуализировать результат?')
#     args = parser.parse_args()
#
#     f_in = open(args.in_name, 'r')
#     f_out = open(args.out_name, 'w')
#
#     a = read_matrix(f_in)
#     b = read_matrix(f_in)
#
#     err_stream = sys.stderr
#
#     if not (is_correct(a) and is_correct(b)):
#         err_stream.write('Матрица некорректна, измените ее')
#         exit(-1)
#
#     if len(b) > len(a) or len(b[0]) > len(a[0]):
#         err_stream.write('ядро свертки больше оригинала. попробуйте изменить размер')
#         exit(-2)
#
#     res = conv(a, b)
#     write_matrix(f_out, res)
#
#     f_in.close()
#     f_out.close()
#
#     if args.show_res:
#         visualize(a, b, res)
#
#
# if __name__ == '__main__':
#     main()


# class account:
#     def __init__(self):
#         self.sallary = 1000
#
#     def give_sallary(self):
#         self.sallary -= 10
#
#
# class amogus:
#     def give_sallary(self):
#         self.balanse += 10
#
#
# def do_work(x, y):
#     for i in range(len(x)):
#         for j in range(len(y)):
#             x[i][j] + y[i][j]
#             print(x)
#             print(y)
#             result = x + y
#             assert isinstance(result, object)
#             print(result)
#
#
# class worker:
#     def read_matrix(self, file):
#         line = file.readline()
#         matrix = []
#         while line != '\n' and line != '':
#             matrix.append([int(x) for x in line.split()])
#             line = file.readline()
#         return matrix
#
#     result = 0
#
# def read_matrix(file):
#     line = file.readline()
#     matrix = []
#     while line != '\n' and line != '':
#         matrix.append([int(x) for x in line.split()])
#         line = file.readline()
#     return matrix
#
#
# def main():
#     matrix_multi = []
#     f_in = open('matrix.txt', 'r')
#     f_out = open('matrix1.txt', 'w')
#     a = read_matrix(f_in)
#     b = read_matrix(f_in)
#
#     for x in range(len(a)):
#         row = []
#         for h in range(len(b[0])):
#             summ = 0
#             for j in range(len(b)):
#                 summ += a[x][j] * b[j][h]
#             row.append(summ)
#         matrix_multi.append(row)
#     print(matrix_multi)
#
# main()
#


# b = 0
# h = input()
# w = input()
# a = (np.random.randint(255, size=(int(h), int(w))))
# print('Исходный:', a)
# print('Уникальные значения', np.unique(a))
# b = len(np.unique(a))
# print('количество уникальных', b)
# str1 = "str1 amogus cheese"
#
# lst = str1.split(' ')
# lst=list(map(len, lst))
# lst1 = np.array(lst)
# print(lst1.mean())
# b = input()
# a = (np.random.randint(15, size=int(3)))
#
#
# def triangle(a, b):
#     a1 = a[b][0]
#     a2 = a[b][1]
#     a3 = a[b][2]
#     if a3 > a1 + a2:
#         print('false')
#     else:
#         print('true')
#
#
# triangle(a,
# a = np.arange(1, 10)
# b = np.arange(-10, 0)[::-1]
# c = ()
# p = 0.2
# c = np.random.choice([True, False], len(b), replace=True, p=[1 - p, p])
# c1 = np.where(c, a, b)
#
# print(c1)
#
# data = np.random.randint(1, 10, size=(10, 5))
# a = 0
# b = 0
# summ = 0
# c = 0
# itg = summm
# df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e'])
# print(df)
# for i in range (10):
#     summ // c = summm
#     for j in range (5):
#         if df.iloc[i, j] > 3:
#             summ += df.iloc[i, j]
#             c += 1
#         else:
#             summ += 0
#
df = ()





def main():
    df = pd.read_csv('titanic_with_labels.csv', index_col=0, delimiter=' ')
    df['sex'] = df['sex'].str.lower()
    df = df[df['sex'].isin('m','м',"ж","мужчина","женщина")]
    
    
    

df = read()
print(df)
