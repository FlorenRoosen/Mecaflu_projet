import numpy as np

def getCoeff(num_left,num_right,num_down,num_up,num_cent,type_cent,cl_cent):
    #est appellée por chaque noeud

    if type_cent == 1:

        #a vaut 1 1 1 1 -4 pour le cas général
        a = np.array([1, 1, 1, 1, -4])

        #b = 0 dans le cas général
        b = 0

        #j

        j = np.array([num_left, num_right, num_down, num_up, num_cent])

    elif type_cent == 2:
        #assigner la deuxième valeur de b sur b2 (valeur de cl_cent à la positiona actuelle ?)

        b = cl_cent

        a = np.array([1])

        j = np.array([num_cent])

    else:
        a = np.array([0, 0, 0, 0, 0])

        j = np.array([0, 0, 0, 0, 0])

        b = 0

    a = np.vstack(a)

    j = np.vstack(j)

    return j,a,b

