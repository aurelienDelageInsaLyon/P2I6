from pair import *
import heapq

class WeightedVertex:

    __slots__=["source","value"]

    def __init__(self, source: Pair, value: float):
        self.source=source;
        self.value=value;
        #print("WARNING: weightedVertex not tested for __eq__, is it an issue?")
        #print("Im concerned about defining __eq__ without cheching self.source==other.source")
        #print("But it seems that it's the way it's done in the Java code.")

    def __eq__(self,other):
        return (self.value==other.value);
    def __hash__(self):
        return (hash(self.source) + hash(self.value));
    def __str__(self):
        return "{"+str(self.source)+" -> " + str(self.value)+ "}";
    def __repr__(self):
        return "{"+str(self.source)+" -> " + str(self.value)+ "}";

    def __lt__(self, other):
        return (self.value < other.value) 

    def __le__(self, other):
        return (self.value <= other.value) 

    def __ge__(self, other):
        return (self.value >= other.value) 

    def __gt__(self, other):
        return (self.value > other.value) 

    def __ne__(self, other):
        return (self.value != other.value) 



#H=["e"]
#pq = heapq.heapify(H);
#heapq.heappush(H,"d")
#heapq.heappush(H,"z")
'''
H=[]
heapq.heappush(H,WeightedVertex(Pair(0,0),  4.5) );
heapq.heappush(H,WeightedVertex(Pair(2,0), -3.5) );
heapq.heappush(H,WeightedVertex(Pair(3,1), -1.5) );
heapq.heappush(H,WeightedVertex(Pair(5,6), 67.5) );
heapq.heappush(H,WeightedVertex(Pair(8,0), 2.5) );

print(heapq.heappop(H));
print(heapq.heappop(H));
print(heapq.heappop(H));
print(heapq.heappop(H));
print(heapq.heappop(H));
'''
