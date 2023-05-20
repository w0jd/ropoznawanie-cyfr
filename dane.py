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
for i in range(28):
    for j in range(28):
        print("dupa")
        plik.write('"')

        plik.write(str(i)+str(j))
        plik.write('"')
        plik.write(",")
plik.write('"')

plik.write("label")
plik.write('"')

plik.write("\n")

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
            plik.write(",")
            plik.write('"')
            plik.write(str(y_train[i]))
            plik.write('"')

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
            plik2.write(",")
            plik2.write('"')
            plik2.write(str(y_test[i]))
            plik2.write('"')
        plik2.write(let)

    plik2.write(",'")
    plik2.write(x_test[i])
    plik2.write("'")
# plt.imshow(x_train[0], cmap='gray')
# print (y_train[0])
# splaszczone2 = list(map(int, splaszczone2))

# plt.axis('off')
# plt.show()
