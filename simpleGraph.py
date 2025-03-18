import networkx as nx
from matplotlib import pyplot as plt

class SimpleGraph:
    """ Représentation d'un Graphe par matrice d'adjacence : 
            edges : liste d'adjacence (Liste 2D d'entiers : 0 ou 1)
            names : tableau associant à chaque numéro de noeud une chaîne de caractère représentant par exemple le nom du noeud.
            vertices : entier représentant le nombre de noeuds du graphe
    """

    def __init__(self, names: [str]):
        ''' Constructeur. Deux configuPeut-être appelé soit avec edges et names, soit avec None.
            Paramètres : 
                names : tableau des noms des noeuds.
        ''' 
        self.names = names
        self.vertices = len(names)
        self.edges = []
        for i in range(len(names)) : 
            self.edges.append([0]*len(names))
    
    def getNeighbors(self,vertex: int):
        ''' retourne la liste d'entiers, correspondant au voisinage du noeud "vertex" en entrée
            param int vertex : noeud donné
            return list of int : liste de voisins du noeud "vertex"
        ''' 
        return self.edges[vertex]


    def addNeighbor(self,source: int, destination: int):
        ''' crée un arc entre le noeud "source" et le noeud "destination"
            Paramètres : 
                * int source : noeud source 
                * int destination : noeud destination 
        '''  
        self.edges[source][destination]=1
        self.edges[destination][source]=1

    def __str__(self):
        ''' retourne une chaîne de caractères décrivant le graphe.
            return String: chaîne de caractères
        ''' 
        show="<graph vertices=\"" + str(self.vertices) + "\">\n"
        for i in range(self.vertices):
            for j in range(self.vertices):
                if (self.edges[i][j]==1):
                    show = show + "\t<arc source=\"" + self.names[i] +  "\" destination=\"" + self.names[j] + "\">\n"
        return show


    def print_nx(self):
        ''' Affichage graphique du graphe
        ''' 
        G=nx.Graph();
        labels={}
        for i in range(self.vertices):
            labels[i] = self.names[i]
        G=nx.relabel_nodes(G,labels)
        for i in range(self.vertices):
            for j in range(i,self.vertices):
                if self.edges[i][j]>0 and i!=j:
                    G.add_edge(i,j)
                    G.add_edge(j,i)
        nx.draw(G, labels=labels,with_labels=True)
        plt.show()



'''
+---------------------------------------------------------------------+
|      Question 2: Instancier et afficher le graphe de la figure 5.   |
+---------------------------------------------------------------------+
'''

