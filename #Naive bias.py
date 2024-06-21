#naive bias
import numpy as np
import matplotlib.pyplot as pl

class Nb():
    
    def __init(self,x,y):
      self.hash={"true":{},"false":{}}
      self.prior=sum(y)/y.size()
      self.false=0
      self.true=0
      counter=0
      while(counter<y.size()):
         i
         if y[counter]==1:
            self.hash["true"][x[counter]]+=1
            self.true+=1
         else:
            self.hash["false"][x[counter]]+=1 
            self.false+=1  
         counter+=1   
      self.size=counter   
      for x in hash:
         hash[x]+=1
         hash[x]/=counter
      
    def predict(self,x:str):
     try :
       hash[x]
       return self.hash[x]      
     except:
        return 1/self.size
    
    def net_score(self,x:np.array):
       res=0
       for l in x:
         res+=self.hash[l.lower().strip()]
       return res 


if __name__ == '__main__':
    tx=np.array(["lmao","lel","binod","all","good","dear","son","sister","discount","mc","name"])  
    yx=np.array([1,1,1,0,0,0,0,0,1,1,0])
    tsx=np.array(["sab","badiya","good"])

    