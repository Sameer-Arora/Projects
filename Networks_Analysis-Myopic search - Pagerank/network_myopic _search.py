import random as r
import matplotlib.pyplot as pl
import networkx as nx
# Programme to compare the time taken by myopic search in the ring type graphs .
# IN THIS EXPERIMENT WE WILL TAKE THE NODES IN DIFFERNT RING GRAPHS 100-1000 AND CALCULATE THE AVERAGE TIME NEEDED TO REACH 
# DIAMETRICALLY OPPOSITE POINTS IN THE GRAPH. 



for num in [100,200,300,400,500,600,700,800,900,1000]:
    g=nx.cycle_graph(num)    #cycle graph represented in networkx
    #t1=r.sample(g.nodes(),1)
    #s1=input("enter the start number:")
    #t=input("enter the end number:")
    j=num/10;              #adding 10% edges in the graph.
    for i in range(j):
        a=r.sample(g.nodes(),1)
        b=r.sample(g.nodes(),1)
        g.add_edge(a[0],b[0])
    
    average=0;
    for point in range(0,num/2):
        no_steps=0
        s=point
        if s>=num/2:
            t=s-num/2           #t being the diametrically opposite point.
        else:
            t=s+num/2
            
        while s!=t:
            near_nei=g.neighbors(s)[0]      #going to nearest neighbour of s.
            for i in g.neighbors(s):
                if abs(t-i)<abs(t-near_nei):
                       near_nei=i
             # print s,"->",ner_nei   
                s=near_nei
                no_steps+=1
        #print  num,point,no_steps
        average+=no_steps      
    
    average/=float(num)/2 
    print  "NUMBER OF NODES IN GRAPH:- ",num,"AVERAGE NUMBER OF STEPS TAKEN:- ",average
       
