import numpy as np
from matplotlib import pyplot as plt
#Simple Logistic Regression

class SLgR():

     def __init__(self,x,y):
        #1/1+e^(w*x+b)
        w=1
        b=1
        a=1
        self.threshold=10E-8
        f1=True
        f2=True
        
        while (f1 or f2):
          if f1:
           temp=w
           cost_derivative=a*sum((y-1/(1 + np.exp(w*x+b)))*x)/x.size
           w-=cost_derivative
           if abs(temp-w)<self.threshold:f1=False
          if f2:
              temp=b
              cost_derivative=a*sum((y-1/(1 + np.exp(w*x+b))))/x.size
              b-=cost_derivative
              if abs(temp-b)<self.threshold:f1=False

        plt.scatter(x,y,color="red")
        y_t=1/(1+np.exp(w*x+b))
        plt.scatter(x,y_t,color="blue")
        print("model trained via logistic regression......") 
                        
x=np.array([0,1,2,3,4,5,6,7,8])
y=np.array([1,1,1,1,1,0,0,0,0])
lr=SLgR(x,y)

