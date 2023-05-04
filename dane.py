from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
plik = open("plik.csv", "w+")
plik2 = open("plik1.csv", "w+")

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print (x_train[0][1])
# fig, axs = plt.subplots(0, 0, figsize=(1, 1))
# fig.subplots_adjust(hspace = .5, wspace=.001)
# axs = axs.ravel()
ile = len(x_train)
ile2 = len(x_test)
# print(ile)
splaszczoneTesty = []
splaszczone2 = []
norm = []
stra = ""
for i in range(ile):
    # splaszczone2.append(np.ravel(x_train[i]))
    stra = str(np.ravel(x_train[i]))
    stra = stra.replace('\n', ' ')

    stra = stra.replace('   ', ',')
    stra = stra.replace('  ', ',')

    stra = stra.replace(' ', ',')
    stra = stra.replace(',,', ',')

    stra = stra.replace('[', '')
    stra = stra.replace(']', '\n')
    stra = stra[1:]
    for let in stra:
        if let == "\n":
            plik.write(",'")
            plik.write(str(y_train[i]))
            plik.write("'")

        plik.write(let)
    # plik.write("\n")

for i in range(ile2):
    # splaszczoneTesty.append(np.ravel(x_test[i]))
    stra = str(np.ravel(x_test[i]))
    stra = stra.replace('\n', ' ')

    stra = stra.replace('   ', ',')
    stra = stra.replace('  ', ',')

    stra = stra.replace(' ', ',')
    stra = stra.replace(',,', ',')

    stra = stra.replace('[', '')
    stra = stra.replace(']', '\n')
    stra = stra[1:]
    for let in stra:
        if let == "\n":
            plik2.write(",'")
            plik2.write(str(y_test[i]))
            plik2.write("'")
        plik2.write(let)

    # plik2.write(",'")
    # plik2.write(x_test[i])
    # plik2.write("'")
# plt.imshow(x_train[0], cmap='gray')
# print (y_train[0])
# splaszczone2 = list(map(int, splaszczone2))

# plt.axis('off')
# plt.show()


def maxImin(list, pocz, kon):
    # list = rd.sample(list1, len(list1))
    maxlist = []
    minList = []
    for i in range(kon-1):
        zmienna = int(list[i][0])
        if isinstance(zmienna, (int, float)):
            maxlist.append(zmienna)
            minList.append(zmienna)

    for i in range(len(list)):
        for j in range(kon-1):
            zmienna = int(list[i][j])
            dl = len(maxlist[i])
            maks = int(maxlist[j][dl])
            mins = int(minList[j][dl])
            if isinstance(zmienna, (int, float)):

                if zmienna > maks:
                    maxlist[j][-1] = zmienna
                if zmienna < mins:
                    minList[j][-1] = zmienna
    # print(minList)
    # print(maxlist)

    for i in range(len(list)):
        for j in range(kon-1):
            zmienna = int(list[i][j])
            mins = int(maxlist[j][dl])
            mins = int(minList[j][dl])
            if isinstance(zmienna, (int, float)):
                list[i][j] = (zmienna - mins) / \
                    (mins - mins)
        # print(list)
    return (list)


tabOdl = []
# print(len(splaszczone2[0]))
# for i in range(len(splaszczone2)):
#     for j in range(len(splaszczone2[0])):
#         tabOdl.append(int(splaszczone2[i][j]))
# print(tabOdl)


def tasowanie(list1):
    list = rd.sample(list1, len(list1))
    return (list)


# norm = maxImin(splaszczone2, 1, len(splaszczone2[0]))
# print(norm[0])
