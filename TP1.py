
import numpy as np

#premier TP relatif au projet

#interface des 2 fonctions à coder :

#fonction get_coeff

#getcoef( num_left , num_right , num_down , num_up , num_centre , type_centre , cl_cent)

#return j , a , b

#vecteurs colone il faut les transposer

# a vecteur colonne des coefficients, j numéro des colonnes différents coefficients, b pour ajd qqc à la matrice b dans le cas dirichlet ??

#type centre pour cas dirichlet

#num_left = numérotation de l'indicde'


#fonction Laplacien (domaine, condition limite, numérotation des noeuds)

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

def Laplace()
    #apelle getcoeff à chaque noeud

    #parcourir le dom : double boucle

    a,b = np.size(dom)

    for i in range(b):
        for j in range(a):
            type_cent = dom[i][j
            if type_cent == 1 or 2:

                #définir toutes les valeurs

                cl_cent_val = cl_cent[i][j]
                num_centre = num[i][j]
                num_left = num[i-1][j]
                num_right =
                num_down =
                num_up =

                j, a, b = getCoeff(num_left,num_right,num_down,num_up,num_cent,type_cent,cl_cent_val)

                #résoudre le système



if __name__ == '__main__':

    #récupérer les données de l'exercice

    dom = np.loadtxt('1-dom.txt', dtype=int)

    num = np.loadtxt('1-num.txt', dtype=int)

    cl_cent = np.loadtxt('1-cl.txt', dtype=int)

    print(cl_cent, dom, num)

    Laplace(dom, num, cl_cent)

    #récupérer la matrice de l'exercice

    scipy.sparse.csc_matrix()

    scipy.sparse.linalg.spsolve(A, b)




#But : renvoyer la fonction de courant return phi (x dans la matrice à gauche)