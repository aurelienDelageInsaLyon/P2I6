import heapq
import math

class SquareGrid:
    """Classe matérialisant un graphe sous forme d'une grille.
       Attributs : 
          width : largeur de la grille
          height : hauteur de la grille
          mountains : ensemble des obstacles dans la grille. 
          forest : ensemble des noeuds (WARNING: comment ça des "noeuds" ??)
          DIRS : tableau des 4 actions possibles: DIRS[0]=droite, DIRS[1]=bas, DIRS[2]=gauche, DIRS[3]=haut 	
    """



    def __init__(self,width: int, height: int):
        """ Constructeur SquareGrid
            Paramètres : 
                * int width : largeur de la grille
                * int height : hauteur de la grille
        """
        self.width=width
        self.height=height
        self.mountains=[]
        self.forest=[]
        self.DIRS=[]

        ######################## instanciate all 4 directions ##########
        self.DIRS.append((1,0))
        self.DIRS.append((0,-1))
        self.DIRS.append((-1,0))
        self.DIRS.append((0,1))
        


    def in_bounds(self,id: tuple):
        """ Fonction vérifiant si on est toujours dans la grille
            paramètres :
                * tuple id : noeud de la grille
            Return :
                * boolean : 0 si on est hors de la grille, sinon 1.
        """ 
        return (0 <= id[0] < self.width and 0 <= id[1] < self.height)



    def passable(self,id: tuple):
        """ Fonction vérifiant si un noeud est accessible ou pas
            paramètres :
                * tuple id : noeud de la grille
            Return : 
                * boolean: 0 si inacessible, 1 sinon
        """ 
        return not(id in self.mountains)



    def cost(self, from_node: tuple, to_node: tuple):
        """ Détermine le coût associé à l'arc qui relie les noeuds "from_node" et "to_node".
            Paramètres : 
                * tuple from_node : noeud de début de l'arc
                * tuple to_node   : noeud de fin de l'arc
            Return :
                * double : coût de l'arc
        """ 
        if (to_node in self.forest):
            return 5
        return 1



    def neighbors(self,id: tuple):
        """ Retourne l'ensemble des voisins d'un noeud donné.
            Paramètres : 
                * tuple id  : noeud donné 
            Return :
                * Liste des noeuds voisins du noeud "id"	
        """ 
        results=[];

        for dir in self.DIRS:
            next= (id[0]+dir[0], id[1]+dir[1])
            if (self.in_bounds(next) and self.passable(next)):
                results.append(next)
        return results
    


    def add_rect(self, x1: int, y1: int, x2: int, y2: int):
        """ Ajoute un rectangle de murs dans la carte
            Paramètres : 
                * x1,y1 : coordonnées du premier sommet du rectangle 
                * x2,y2 : coordonnées du second sommet du rectangle
        """ 
        for i in range(x1,x2):
            for j in range(y1,y2):
                self.mountains.append((i,j))






    def make_diagram1():
        """ Factory : crée une grille 30x15 initialisée avec des obstacles
        """ 
        grid = SquareGrid(30,15)
        grid.add_rect(3, 3, 5, 12)
        grid.add_rect(13, 4, 15, 15)
        grid.add_rect(21, 0, 23, 7)
        grid.add_rect(23, 5, 26, 7)

        return grid



    def make_diagram4():
        """ Factory : crée une grille 10x10 initialisée avec des obstacles
        """ 
        grid = SquareGrid(10,10)
        grid.add_rect(1, 7, 4, 9)

        grid.forest.append((3,4))
        grid.forest.append((3,5))
        grid.forest.append((4,1))
        grid.forest.append((4,2))
        grid.forest.append((4,3))
        grid.forest.append((4,4))
        grid.forest.append((4,5))
        grid.forest.append((4,6))
        grid.forest.append((4,7))
        grid.forest.append((4,8))
        grid.forest.append((5,1))
        grid.forest.append((5,2))
        grid.forest.append((5,3))
        grid.forest.append((5,4))
        grid.forest.append((5,5))
        grid.forest.append((5,6))
        grid.forest.append((5,7))
        grid.forest.append((5,8))
        grid.forest.append((6,2))
        grid.forest.append((6,3))
        grid.forest.append((6,4))
        grid.forest.append((6,5))
        grid.forest.append((6,6))
        grid.forest.append((6,7))
        grid.forest.append((7,3))
        grid.forest.append((7,4))
        grid.forest.append((7,5))

        return grid

    def draw_grid(self,distances, point_to, path):
        """ Affiche la grille, ainsi que le chemin à suivre
        """ 
        for y in range(self.height):
            for x in range(self.width):
                id = (x,y);
                if (id in self.mountains):
                    if distances==None : 
                        print('#', end=" ")
                    else : 
                        print('   #', end=" ")
                elif (point_to!=None and (id in point_to.keys())):
                    p=point_to[id];
                    if (p[0]==x+1):
                        print("\u2192",end=" ")
                    elif (p[0]==x-1):
                        print("\u2190",end=" ")
                    elif (p[1]==y+1):
                        print("\u2193",end=" ")
                    elif (p[1]==y-1):
                        print("\u2191",end=" ")
                    else :
                        print("*", end=" ");
                elif (distances!=None and len(distances)>0 and (id in distances.keys())):
                    if distances[id] == math.inf : 
                        print(f"   \u221E",end=" ");
                    else : 
                        print(f"{distances[id]:4d}",end=" ");
                elif (path != None and (id in path)):
                    print('@',end=" ");
                elif(id in self.forest):
                    print('f',end=" ")
                else:
                    print(".",end=" ");
            print()
        print()



    """
    //+---------------------------------------------------------------------+//
    //      Question 3. Compléter le fonction BFS                            //
    //+---------------------------------------------------------------------+//
    """
    def bfs(self, start: tuple):
        """ Implémentation de l'algorithme BFS
            Paramètres : 
                * tuple start : noeud initial
            Return :
                * Dictionnaire (dict de couples) associant à chaque noeud, le noeud voisin duquel il est accessible selon BFS (son parent dans l'arbre de voisinage)
                  Dans ce dictionnaire, la racine est indiquée par le fait qu'elle est associée à elle-même
        """
        return None



    """
    //+---------------------------------------------------------------------+//
    //      Question 5. Compléter la reconstruction du chemin                //
    //+---------------------------------------------------------------------+//
    """
    def reconstruct_path(self, start: tuple, goal: tuple, came_from:dict):
        """ Reconstruction du chemin de la node à la destination.
            Suit le dictionnaire en partant de la destination et en remontant les noeuds qui ont donné acces 
            de la node à la destination
            Paramètres : 
                * start (tuple) : sommet de départ du chemin (couple x,y de coordonnées)
                * goal (tuple) : sommet de départ du chemin (couple x,y de coordonnées)
                * came_from (dict(tuple)->tuple) : dictionnaire décrivant l'arbre couvrant minimum
            Retun : 
                * List sommet (liste de tuple) : le chemin
        """
        return None

    """
    //+---------------------------------------------------------------------+//
    //      Question 7.  Compléter l'algorithme Dijkstra                     //
    //+---------------------------------------------------------------------+//
    """
    def dijkstra_search(self, start: tuple, goal: tuple):
        """ Implémentation de l'algorithme de Dijkstra
            Paramètres : 
                * start (tuple) : noeud initial (la racine)
                * goal (tuple) : noeud à atteindre
            Return :
                (parents, couts) : 
                    * parents (dict(tuple) -> tuple) : Dictionnaire associant à chaque noeud, le noeud voisin duquel il est accessible selon BFS (son parent dans l'arbre de voisinage)
                      Dans ce dictionnaire, la racine est indiquée par le fait qu'elle est associée à elle-même
                      Ce dictionnaire ne contient pas nécessairement tous les noeud en clefs.
                    * couts (dict(tuple) -> float) : Dictionnaire associant à chaque noeud, sa distance à la racine.
        """
        return None, None

    """
    //+---------------------------------------------------------------------+//
    //      Question 9.         Compléter l'évaluation heuristique.          //
    //+---------------------------------------------------------------------+//
    """
    def heuristic(self, a: tuple, b: tuple):
        """ Calcule et retourne l'heuristique de cout entre les 2 noeuds a et b.
            Paramètres : 
                * a (tuple) et b (tuple) : 2 sommets du graphe
            Return :
                * float : une valeur basée uniquement sur leur distance
        """
        return None

    """
    //+---------------------------------------------------------------------+//
    //      Question 10.  Completer l'algorithme A*                          //
    //+---------------------------------------------------------------------+//
    """
    def a_star_search(self, start: tuple, goal: tuple):
        """ Implémentation de l'algorithme de Dijkstra
            Paramètres : 
                * start (tuple) : noeud initial (la racine)
                * goal (tuple) : noeud à atteindre
            Return :
                (parents, couts) : 
                    * parents (dict(tuple) -> tuple) : Dictionnaire associant à chaque noeud, le noeud voisin duquel il est accessible selon BFS (son parent dans l'arbre de voisinage)
                      Dans ce dictionnaire, la racine est indiquée par le fait qu'elle est associée à elle-même
                      Ce dictionnaire ne contient pas nécessairement tous les noeud en clefs.
                    * couts (dict(tuple) -> float) : Dictionnaire associant à chaque noeud, sa distance à la racine.
        """
        return None, None




def test_bfs():
    print("** breadth-first-search algorithm **");
    grid=SquareGrid.make_diagram1()
    grid.draw_grid(None,None,None)
    parents=grid.bfs((7,8))
    grid.draw_grid(None,parents,None)


def test_dijkstra():
    print("** dijsktra algorithm **")
    grid = SquareGrid.make_diagram4()
    grid.draw_grid(None, None, None)
    start = (1, 4)
    goal = (8, 5)

    came_from, cost_so_far = grid.dijkstra_search(start, goal)
    grid.draw_grid(None, came_from, None)
    print()
    grid.draw_grid(cost_so_far, None, None)
    print()
    path=grid.reconstruct_path(start, goal, came_from)
    grid.draw_grid(None, None, path)


def test_a_star():
    print("** A* algorithm **")
    grid=SquareGrid.make_diagram4()
    grid.draw_grid(None,None,None)
    start = (1, 4)
    goal = (8, 5)

    came_from, cost_so_far = grid.a_star_search(start,goal)
    grid.draw_grid(None,came_from,None)
    print()
    grid.draw_grid(cost_so_far,None,None)
    print()
    path=grid.reconstruct_path(start,goal,came_from)
    grid.draw_grid(None,None,path)



test_bfs()
#test_dijkstra()
#test_a_star()
