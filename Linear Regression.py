import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class LR:
  def __init__(self): 
    self.w=1
    self.b=1
    self.a=0.07
    self.tdx=np.array([1,2,3,4,5,6,-1,-2,-3,-4])
    self.tdy=np.array([0,0,0,0,0,0,1,1,1,1])
    plt.scatter(self.tdx,self.tdy)

  def uw(self):
          derivative=np.dot((1/(1+np.exp(self.w*self.tdx+self.b)))-self.tdy,self.tdx)
          Error=derivative/self.tdy.size
            
          if not((abs(Error)<10e-2 and Error>0)):
             temp=    self.w
             self.w-= self.a*Error
             if temp==self.w:return True
             return False
          return True
 
 
  def ub(self):
         derivative=sum((1/(1+np.exp(self.w*self.tdx+self.b)))-self.tdy)
         Error=derivative/self.tdy.size

         if not ((abs(Error)<10e-3 and Error!=0)):
            temp=self.b  
            self.b-=self.a*Error
            if temp==self.b:return True
            return False
         return True
 
  def predict(self,x):
      return 1/(1-(1-np.e**(self.w*x+self.b)))
     
  def calibrate(self):
     ew=self.uw()
     eb=self.ub()
     arr=np.arange(min(self.tdx),max(self.tdx))
     print(self.w,self.b)
    
     while((ew & eb)==False):        
         ew=self.uw()
         eb=self.ub()
         print(self.w,self.b)
         plt.scatter(self.tdx,self.tdy)
         plt.scatter(self.tdx,1/(1+np.exp(self.w*self.tdx+self.b)),color="red")     
         plt.plot(arr,1/(1+np.e**self.w*arr+self.b),color="yellow")
         plt.pause(10e-10) 
         plt.clf()    
     plt.show()      
        
class PRM:
 def __init__(self,tdx,tdy): 
  self.w=1
  self.b=1
  self.a=0.01
  self.tdx=tdx
  self.tdy=tdy
  plt.scatter(tdy,tdx,color="red")

 def uw(self):
          derivative=np.dot((self.w*self.tdx+self.b)-self.tdy,self.tdx)
          Error=derivative/self.tdy.size

          if not((abs(Error)<10e-17 and Error>0) or pd.isna(Error)):
             temp=self.w
             self.w-=self.a*Error
             if temp==self.w:return True
             return False
          return True
 
 def scale(self):
     mean=(sum(self.tdy)/self.tdy.size) 

 def ub(self):
         Error=((self.w*self.tdx +self.b)-self.tdy)
         Error=sum(Error)/self.tdy.size
         if not ((abs(Error)<10e-17 and Error!=0)):
            temp=self.b  
            self.b-=self.a*Error
            if temp==self.b:return True
            return False
         return True
    
 def calibrate(self):
     ew=self.uw()
     eb=self.ub()
     while((ew & eb)==False):        
         ew=self.uw()
         eb=self.ub()   
     plt.scatter(self.w*self.tdx+self.b,self.tdx)
            
     plt.show()     

 def predict(self,x):return self.w*x+self.b   


tdx=[1,2,3,4,5,6,7,8]
tdy=[1,1,1,10,14,11,15,17]

#tdx=[1,2,3,4,5,6,7,8]
#tdy=[8,7,6,5,4,3,2,1]
model1=LR()
model1.calibrate()
#model=PRM(np.array(tdx),np.array(tdy))
#print(model.w,model.b)
#model.calibrate()



                           
    

#y'=wx+self.b
#error_=self.w()