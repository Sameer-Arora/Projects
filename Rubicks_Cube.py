from copy import deepcopy

def move_x1(l):        
  l1=deepcopy(l)
  a=l1[2][1]
  b=l1[2][3]
  l1[2][1]=l1[4][0]
  l1[2][3]=l1[4][1]
  l1[4][0]=l1[3][0]
  l1[4][1]=l1[3][2]
  l1[3][0]=l1[5][2]
  l1[3][2]=l1[5][3]
  l1[5][2]=a 
  l1[5][3]=b
  return l1
  
  
  
def move_x2(l): 
  l1=deepcopy(l)
  a=l1[2][0]
  b=l1[2][2]
  l1[2][0]=l1[4][2]
  l1[2][2]=l1[4][3]
  l1[4][2]=l1[3][1]
  l1[4][3]=l1[3][3]
  l1[3][1]=l1[5][0]
  l1[3][3]=l1[5][1]
  l1[5][0]=a 
  l1[5][1]=b
  return l1
  
def move_y1(l):
  l1=deepcopy(l)
  a=l1[1][1]
  b=l1[1][3]
  l1[1][1]=l1[4][2]
  l1[1][3]=l1[4][0]
  l1[4][2]=l1[0][2]
  l1[4][0]=l1[0][0]
  l1[0][0]=l1[5][0]
  l1[0][2]=l1[5][2]
  l1[5][0]=b 
  l1[5][2]=a
  return l1
  
def move_y2(l):  
  l1=deepcopy(l)
  a=l1[1][0]
  b=l1[1][2]
  l1[1][0]=l1[4][3]
  l1[1][2]=l1[4][1]
  l1[4][3]=l1[0][3]
  l1[4][1]=l1[0][1]
  l1[0][3]=l1[5][3]
  l1[0][1]=l1[5][1]
  l1[5][1]=b 
  l1[5][3]=a
  return l1
  
def move_z1(l):
  l1=deepcopy(l)
  a=l1[3][1]
  b=l1[3][3]
  l1[3][1]=l1[0][1]
  l1[3][3]=l1[0][3]
  l1[0][1]=l1[2][1]
  l1[0][3]=l1[2][3]
  l1[2][1]=l1[1][1]
  l1[2][3]=l1[1][3]
  l1[1][1]=a 
  l1[1][3]=b
  return l1
  
def move_z2(l):   
  l1=deepcopy(l)
  a=l1[3][0]
  b=l1[3][1]
  l1[3][0]=l1[0][0]
  l1[3][1]=l1[0][1]
  l1[0][0]=l1[2][0]
  l1[0][1]=l1[2][1]
  l1[2][0]=l1[1][0]
  l1[2][1]=l1[1][1]
  l1[1][0]=a 
  l1[1][1]=b
  return l1

def arr(l):
    l1=move_x1(l)
    #print l,l1 ,"\n"
    l2=move_x2(l)
    #print l,l1,l2,"\n"
    l3=move_y1(l)
    #print l,l1,l2,l3,"\n"
    l4=move_y2(l)
    #print l,l1,l2,l3,l4,"\n"
    l5=move_z1(l)
    #print l,l1,l2,l3,l4,l5,"\n"
    l6=move_z2(l)
    #print l,l1,l2,l3,l4,l5,l6,"\n"
    arrn=[ l1 , l2 , l3 , l4 , l5 , l6 ]
    return arrn
    
root=[ [1,1,1,1] ,[2,2,2,2] ,[3,3,3,3] ,[4,4,4,4] ,[5,5,5,5] ,[6,6,6,6] ]  

# print arr(root),'\n\n'

class strct():
    def __init__(self,name,parent):
        self.name =name 
        self.parent = parent
        

def path(pt):
  global node_visited
  
  while(pt.parent!=pt.name):
    print pt.name,"->",pt.parent,"\n"
    for i in node_visited:
      if pt.parent==i.name:
        pt=i
      
    

node_visited=[]

def bfs( key ,st):
  global node_visited
  
  node=st
  l=[ node ]        #current level
  l1=[l]                 #list of all my nodes at each level
  node_visited=[st]

                       
  while len(l)>0:
    l2=[]  #next level
   
    for i in l:
     # print i.name,'\n', i.parent,"\n"
              
      for j in arr(i.name):     #check for nearest neighbours.
        node=strct(j,i.name)
        if node.name==key:

          path(node)
          return 
        
        elif node.name  not in node_visited:
          node_visited.append( node )
          l2.append( node )   # node is a neighboue of i[0].
         
           
    if len(l2)>0:   
      l1.append(l2)
    l=l2  
 
  
  return 

start=strct(root,root)
bfs(move_x2(move_z2(move_y2(root))),start)

  






















    
    
