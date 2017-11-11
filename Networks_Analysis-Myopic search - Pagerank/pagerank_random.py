import matplotlib.pyplot as pl
import networkx as nx
import random as ra

g=nx.DiGraph()
g=nx.read_adjlist('impressed.txt',nodetype=int)

a=nx.adj_matrix(g)

walk=[]
m=g.order()
k=ra.randint(1,m)
walk.append(k)
for i in range(1000000):
    n=nx.neighbors(g,k)
    l=ra.sample(n,1)
    walk.append(l[0])
    k=l[0]
    
##print walk
p={}              #my dictionary of pagerank
q={}              #in-built dictioary of page rank
for i in range(g.order()):  
    p[i+1]=0
    
for i in walk:
    p[i]+=1

print p,'my_solution'

i=0
for key, value in sorted(p.iteritems(), key=lambda (k,v): (v,k)):
    ##q[key]=value
    i+=1
    if i>40:                   #to find the top 10.
        print "%d: %d" % (key, value)

q=nx.pagerank(g)
 
i=0   
for key, value in sorted(q.iteritems(), key=lambda (k,v): (v,k)):
    ##q[key]=value
    i+=1
    if i>40:
        print "%f: %f" % (key, value)
        
        

