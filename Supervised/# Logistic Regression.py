import numpy as np
from matplotlib import pyplot as plt
#Simple Logistic Regression

class SLgR():

     def __init__(self,a,t):
        #1/1+e^(w*x+b)
        self.a=a
        self.threshold=t
     def fit(self,x,y):    
        f1=True
        f2=True
        self.w=1
        self.b=1
        while (f1 or f2):
          if f1:
           temp=self.w
           cost_derivative=self.a*sum((y-1/(1 + np.exp(self.w*x+self.b)))*x)/x.size
           self.w-=cost_derivative
           if abs(temp-self.w)<self.threshold:f1=False
          if f2:
              temp=self.b
              cost_derivative=self.a*sum((y-1/(1 + np.exp(self.w*x+self.b))))/x.size
              self.b-=cost_derivative
              if abs(temp-self.b)<self.threshold:f1=False
     def plotex(self,x):      
        plt.scatter(x,y,color="red")
        y_t=1/(1+np.exp(self.w*x+self.b))
        plt.scatter(x,y_t,color="blue")
        print("model trained via logistic regression......") 
        plt.show()          
     def __predict__(self,x):  
        return 1/(1+np.exp(self.w*x+self.b))          

x=np.array([0,1,2,3,4,5,6,7,8])
y=np.array([1,1,1,1,1,0,0,0,0])
lr=SLgR(x,y)



