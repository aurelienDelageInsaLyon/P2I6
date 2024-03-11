import networkx as nx
from matplotlib import pyplot as plt


class SimpleGraph:
    __slots__=["edges","names","vertices"]
  ##<! matrice d'adjacence, associant à tout noeud un tableau booléen correspondant aux arcs vers d'autres noeuds
    #edges=[];

  ###<! tableau associant à chaque numéro de noeud une chaîne de caractère représentant par exemple le nom du noeud.
    #names=[];

  ###<! entier représentant le nombre de noeuds du graphe
    #vertices=None;

    ''' 
   * \fn constructeur de graphes
   * \param int[][] edges : matrice d'ajacence NxN, où N est le nombre de noeuds du graphe, 
   * 		            et où chaque cellule prend une valeur booléenne: 1 si les noeuds 
   * 		            correspondants sont reliés par un arc; 0 sinon.
   * \param String[] names : tableau des noms des noeuds.
   * \param vertices : nombre N de noeuds
   * \return SimpleGraph 		            
  ''' 
    def __init__(self, edges: [[int]], names: [str], vertices:int=None):
        # constructeur sans nombre de sommets
        if (vertices==None):
            self.edges=edges;
            self.names=names;
            self.vertices=len(names);
        # constructeur avec nombre de sommets
        else:
            self.vertices=vertices;
            self.edges=[[0 for _ in range(vertices)] for _ in range(vertices)]
            self.names=[""+str(i)+"" for i in range(vertices)]
    
    ''' 
   * \fn int[] getNeighbors(int vertex)
   * \description: retourne le tableau de booléens, correspondant au voisinage du noeud "vertex" en entrée
   * \param int vertex : noeud donné
   * \return int[]     : tableau de voisins du noeud "vertex"
''' 
    def getNeighbors(self,vertex: int):
        return self.edges[vertex];

    ''' 
   * \fn void addNeighbor(int source, int destination)
   * \description: crée un arc entre le noeud "source" et le noeud "destination"
   * \param int source : noeud source 
   * \param int destination : noeud destination 
 '''  
    def addNeighbor(self,source: int, destination: int):
        self.edges[source][destination]=1;
        self.edges[destination][source]=1;

    ''' 
   * \fn String toString() 
   * \description : retourne une chaîne de caractères décrivant le graphe.
   * \return String: chaîne de caractères
 ''' 
    def __str__(self):
        show="<graph vertices=\"" + str(self.vertices) + "\">\n";
        for i in range(self.vertices):
            for j in range(self.vertices):
                if (self.edges[i][j]==1):
                    show = show + "\t<arc source=\"" + self.names[i] +  "\" destination=\"" + self.names[j] + "\">\n";
        return show

    def print_nx(self):
        G=nx.Graph();
        labels={}
        for i in range(self.vertices):
            labels[i] = names[i];
        G=nx.relabel_nodes(G,labels)
        for i in range(self.vertices):
            for j in range(i,self.vertices):
                if self.edges[i][j]>0 and i!=j:
                    G.add_edge(i,j);
                    G.add_edge(j,i);
        nx.draw(G, labels=labels,with_labels=True);
        plt.show();

    '''
  //+---------------------------------------------------------------------+//
  //      Question 2: Instancier et afficher le graphe de la figure 5.     //
  //+---------------------------------------------------------------------+//
'''
