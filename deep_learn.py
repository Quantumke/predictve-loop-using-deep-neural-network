"""
Using deep learning we have a third layer(hidden layer)

INPUTS           HIDDEN              OUTPUT
0 ,0,1      O.1, O,2, 0.5, 0.2        0
0, 1,1      0.2, 0.6, 0.7, 0.1	      1
1, 0,1	    0.3, 0.2, 0.3, 0.9	      1
1, 1,1	    0.2, 0.1, 0.3, 0.8	      0

"""
import numpy as np

class deep_learner():
    self.author="Ben Nguru"
    #sigmoid function
    def nonlin(x, deriv=False):
        if (deriv=True):
            returnx*(1-x)
        return 1/(1+np.exp(-x))
   X=np.array([ [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1] ])
    #output  dataset using transpose function
    #after transponse each matrix has 4 rows with one column
    y=np.array([[0].
                [1],
                [1],
                [0]])
    #seed random numbers to make calculations
    np.random.seed(1)
    #initialize weights randomly with mean 0
    syn0=2*np.random.random((3,4))-1
    syn1=2*np.random.random((4,1)) -1
    for j in xrange(60000):
        #foward propagation throuugh three layers
        l0=X
        l1=nonlin(np.dot(l0,syn0))
        l2=nonlin(np.dot(l1,syn1))
        #get error
        l2_error=y-l2
        if(j% 10000) ==:
            print "Error:" + str(np.mean(np.abs(l2_error)))





app=deep_learner()
