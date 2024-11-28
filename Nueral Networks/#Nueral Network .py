#Nueral Network from scratch
import numpy as np

class sigmoid():
    def __init__(self,w,b):    
        return 1/np.exp(-(w*self.val+b))

class Network:
  
    def __init__(self,layers):
     self.layers=[Layer(n,a) for n,a in layers]
     self.n_layers=len(layers)
    
    def forward_prop(self,inputs,n=0):
        outcome=self.layers[n].activate(inputs)
        if(n<self.n_layers):self.forward_prop(outcome*self.layers[n+1].size,1)
        else: return outcome

    def back_prop(self,inputs,outputs):
        outcomes=[]
        for l in inputs:
            outcomes.append(self.forward_prop(l))
        outcomes=np.array(outcomes)
        self.error=sum(outputs-outcomes)
       
        for l in range(len(self.layers),-1):
           for node in self.layers[l]:
            node.dw
            node.db


          
class Layer:
    def __init__(self,nodes,activation):
        self.size=len(nodes)
        self.nodes=[Node(x,y,activation)for x,y in nodes]
         
    def activate(self,inputs):
        activation=0
        count=0
        for x in self.nodes:
            activation+=(x.get(input[count]))
            count+=1
        return np.array(activation)

class Node:

    def __init__(self,w,b,activation):
       self.w=0
       self.b=0
       self.dw,self.db=activation.derivative(w,b)
       self.activation=activation

    def get(self,input):return self.activation(self.w*input+self.b) 
    
    def set(self,del_w,del_b):
        self.w-del_w
        self.b-del_b
        self.dw,self.db=self.activation.derivative(self.w,self.b)

                                