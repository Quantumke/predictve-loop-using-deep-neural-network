"""
In the matrix below try to predict the output column:
INPUTS       OUTPUTS
0 0 1          0
1 1 1          1
1 0 1          1
0 1 1          0
 use BackPropagation"""
import numpy as np
class predictloop():
    def __init__(self, *args, **kwargs):
        self.author="Benson Nguru"
        self.nonlin()
    #sigmoid function
    def nonlin(x, deriv=False):
        if(deriv=True):
            return x *(1-x)
        return 1/(1+np.exp(-x))
    #input dataset
    X=np.array([ [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1] ])
    #output  dataset
    y=np.array([[0,0,1,1]]).T
    #seed random numbers to make calculations
    np.random.seed(1)
    #initialize weights randomly with mean 0
    syn0=2*np.random.random((3,1))-1
    for iter in xrange(10000):
        #foward propagation
        l0=X
        l1=nonlin(np.dot(l0,syn0))
        #calculate error
        l1_error=y-l1
        #multiply error bu slope of sigmoid at values l1
        l1_delta=l1_error*nonlin(l1,True)
        
        





app = predictloop()
