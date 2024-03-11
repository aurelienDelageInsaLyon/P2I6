from pair import *
import heapq
from weightedVertex import *

class SquareGrid:

    __slots__=["width","height","walls","montagne","DIRS"]
  ##<! largeur de la grille
    #width=-1;

  ###<! hauteur de la grille
    #height=-1;

  ###<! ensemble des obstacles dans la grille. 
    #walls=[];

  ###<! ensemble des noeuds 
  ### WARNING: comment ça des "noeuds" ??
    #montagne=[];

  ###<! tableau des 4 actions possibles: DIRS[0]=droite, DIRS[1]=bas, DIRS[2]=gauche, DIRS[3]=haut 	
    #DIRS=[]; #### directions tabular

    """ 
   * \fn SquareGrid(ine width, int height) : constructeur SquareGrid
   * \param int width : largeur de la grille
   * \param int height : hauteur de la grille
"""  

    def __init__(self,width: int, height: int):
        self.width=width;
        self.height=height;
        self.walls=[]
        self.montagne=[]
        self.DIRS=[]

        ######################## instanciate all 4 directions ##########
        self.DIRS.append(Pair(1,0));
        self.DIRS.append(Pair(0,-1));
        self.DIRS.append(Pair(-1,0));
        self.DIRS.append(Pair(0,1));
        
    """ 
   * \fn boolean in_bounds(Pair id) : fonction vérifiant si on est toujours dans la grille
   * \param Pair id : noeud de la grille
   * \return boolean : 0 si on est hors de la grille, sinon 1.
""" 
    def in_bounds(self,id: Pair):
        tmp = (0 <= id.x and id.x < self.width and 0 <= id.y and id.y < self.height);
        return tmp;

    """ 
   * \fn boolean passable(Pair id) : fonction vérifiant si un noeud est accessible ou pas
   * \param Pair id : noeud de la grille
   * \return boolean: 0 si inacessible, 1 sinon
 """ 
    def passable(self,id: Pair):
        return not(id in self.walls);

    """ 
   * \fn double cost(Pair from_node, Pair to_node) : détermine le coût associé à l'arc qui relie les noeuds "from_node" et "to_node".
   * \param Pair from_node : noeud de début de l'arc
   * \param Pair to_node   : noeud de fin de l'arc
   * \return double        : coût de l'arc
""" 
    def cost(self, from_node: Pair, to_node: Pair):
        if (to_node in self.montagne):
            return 5
        return 1;

    """ 
   * \fn HashSet<Pair> neighbors(Pair id) : retourne l'ensemble des voisins d'un noeud donné.
   * \param Pair id  : noeud donné 
   * \return Array : ensemble des noeuds voisins du noeud "id"	
""" 
    def neighbors(self,id: Pair):
        results=[];

        for dir in self.DIRS:
            next= Pair(id.x+dir.x, id.y+dir.y)
            if (self.in_bounds(next) and self.passable(next)):
                results.append(next);
        return results;
    

    """ 
   * \fn void add_rect(int x1, int y1, int x2, int y2)
   * \param int x1 : coordonnée X du premier noeud 
   * \param int y1 : coordonnée Y du premier noeud
   * \param int x2 : coordonnée X du second noeud
   * \param int y2 : coordonnée Y du second noeud
""" 
    def add_rect(self, x1: int, y1: int, x2: int, y2: int):
        for i in range(x1,x2):
            for j in range(y1,y2):
                self.walls.append(Pair(i,j));

    """ 
   * \fn static SquareGrid make_diagram1() : crée une grille 30x15
""" 
    def make_diagram1():
        grid = SquareGrid(30,15);
        grid.add_rect(3, 3, 5, 12);
        grid.add_rect(13, 4, 15, 15);
        grid.add_rect(21, 0, 23, 7);
        grid.add_rect(23, 5, 26, 7);

        grid.draw_grid(None,None,None);

        return grid;

    """ 
   * \fn static SquareGrid make_diagram4() : crée une grille 10x10
""" 
    def make_diagram4():

        grid = SquareGrid(10,10);
        grid.add_rect(1, 7, 4, 9);

        grid.montagne.append(Pair(3,4));
        grid.montagne.append(Pair(3,5));
        grid.montagne.append(Pair(4,1));
        grid.montagne.append(Pair(4,2));
        grid.montagne.append(Pair(4,3));
        grid.montagne.append(Pair(4,4));
        grid.montagne.append(Pair(4,5));
        grid.montagne.append(Pair(4,6));
        grid.montagne.append(Pair(4,7));
        grid.montagne.append(Pair(4,8));
        grid.montagne.append(Pair(5,1));
        grid.montagne.append(Pair(5,2));
        grid.montagne.append(Pair(5,3));
        grid.montagne.append(Pair(5,4));
        grid.montagne.append(Pair(5,5));
        grid.montagne.append(Pair(5,6));
        grid.montagne.append(Pair(5,7));
        grid.montagne.append(Pair(5,8));
        grid.montagne.append(Pair(6,2));
        grid.montagne.append(Pair(6,3));
        grid.montagne.append(Pair(6,4));
        grid.montagne.append(Pair(6,5));
        grid.montagne.append(Pair(6,6));
        grid.montagne.append(Pair(6,7));
        grid.montagne.append(Pair(7,3));
        grid.montagne.append(Pair(7,4));
        grid.montagne.append(Pair(7,5));

        grid.draw_grid(None,None,None);

        return grid;

    """ 
   * \fn void draw_grid() : affiche la grille, ainsi que le chemin à suivre
""" 
    def draw_grid(self,distances, point_to, path):
        for y in range(self.height):
            for x in range(self.width):
                id = Pair(x,y);
                if (id in self.walls):
                    print('#', end=" ")
                elif (point_to!=None and (id in point_to.keys())):
                    p=point_to[id];
                    if (p.x==x+1):
                        print("\u2192",end=" ")
                    elif (p.x==x-1):
                        print("\u2190",end=" ")
                    elif (p.y==y+1):
                        print("\u2193",end=" ")
                    elif (p.y==y-1):
                        print("\u2191",end=" ")
                    else :
                        print("*", end=" ");
                elif (distances!=None and len(distances)>0 and (id in distances.keys())):
                    #fstrin
                    print(f"{distances[id]:4d}",end=" ");
                elif (path != None and (id in path)):
                    print('@',end=" ");
                #elif(id in self.montagne):
                #    print('f',end=" ")
                else:
                    print(".",end=" ");
            print("\n",end="");
        print("\n",end="");

    """
  //+---------------------------------------------------------------------+//
  //      Question 3. Compléter le fonction BFS                            //
  //+---------------------------------------------------------------------+//
  /**
   * \fn Dictionnaire<Pair,Pair> breadth_first_search(Pair start) : algorithme BFS
   * \param Pair start : noeud initial
   * \return HashMap<Pair,Pair> : dictionnaire stockant à tout noeud, le noeud voisin duquel il est accessible selon BFS
   * \description de l'algorithme:
   * 	1. initialiser la dictionnaire capable de stocker pour tout noeud rencontré, le noeud duquel il est accessible selon BFS
   * 	2. initialiser la file où seront stockés les noeuds au fur et à mesure qu'on les découvre 
   * 	3. Récupérer le premier noeud de la file, et supprimer le  de cette file
   * 	4. Parcourir l'ensemble des voisins de ce noeud
   *	5. Pour chaque voisin, vérifier qu'il n'a pas encore été traité (il ne doit pas être présent dans le dictionnaire)
   *	6. S'il n'est pas présent dans le dictionnaire, ajouter le dans la file et dans le dictionnaire, puis retourner en 3.
   */
"""
    def bfs(self, start: Pair):
        return
    """
  //+---------------------------------------------------------------------+//
  //      Question 5. Compléter la reconstruction du chemin                //
  //+---------------------------------------------------------------------+//
  /**
   * \fn Vector<Pair> reconstruct_path(Pair start, Pair goal, HashMap<Pair, Pair> came_from) : chemin de la source à la destination.
   * \description: suivre le dictionnaire en partant de la destination et en remontant les noeuds qui ont donné acces 
   * 		   de la source à la destination
   */ 
"""
    def reconstruct_path(self, start: Pair, goal: Pair, came_from):
        return
    """
  //+---------------------------------------------------------------------+//
  //      Question 7.  Compléter l'algorithme Dijkstra                     //
  //+---------------------------------------------------------------------+//
"""
    def dijkstra_search(self, start: Pair, goal: Pair, came_from, cost_so_far):
        return;
    """
  //+---------------------------------------------------------------------+//
  //      Question 9.         Compléter l'évaluation heuristique.          //
  //+---------------------------------------------------------------------+//
"""
    def heuristic(self, a: Pair, b: Pair):
        return 0.0 
    """
  //+---------------------------------------------------------------------+//
  //      Question 10.  Completer l'algorithme A*                          //
  //+---------------------------------------------------------------------+//
"""
    def a_star_search(self, start: Pair, goal: Pair, came_from, cost_so_far):
        return;



def test_bfs():
    print("** breadth-first-search algorithm **");
    grid=SquareGrid.make_diagram1();
    parents=grid.bfs(Pair(7,8));
    grid.draw_grid(None,parents,None);
    return;

def test_dijkstra():
    print("** dijsktra algorithm **");
    grid=SquareGrid.make_diagram4();
    start=Pair(1,4);
    goal=Pair(8,5);

    came_from={};
    cost_so_far={};
    grid.dijkstra_search(start,goal,came_from,cost_so_far);
    grid.draw_grid(None,came_from,None);
    print("\n",end="");
    grid.draw_grid(cost_so_far,None,None);
    print("\n",end="");
    path=grid.reconstruct_path(start,goal,came_from);
    grid.draw_grid(None,None,path);

def test_a_star():
    print("** A* algorithm **");
    grid=SquareGrid.make_diagram4();
    goal=Pair(1,4);
    start=Pair(8,5);

    came_from={};
    cost_so_far={};
    grid.a_star_search(start,goal,came_from,cost_so_far);
    grid.draw_grid(None,came_from,None);
    print("\n",end="");
    grid.draw_grid(cost_so_far,None,None);
    print("\n",end="");
    path=grid.reconstruct_path(start,goal,came_from);
    grid.draw_grid(None,None,path);
    return;





test_bfs();
test_dijkstra();
test_a_star();
