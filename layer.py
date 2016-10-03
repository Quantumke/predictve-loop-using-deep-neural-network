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





app = predictloop()
