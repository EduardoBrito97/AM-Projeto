import numpy as np
import scipy
from collections import Counter

class KSS:
    def __init__(self,k):
        self.k = k
    
    def fit(self,X,Y,massType):
        self.X = X
        self.Y = Y

        self.massX = self.calculateMass(X,Y,massType)
    
    def calculateMass(self,X,Y,massType):
        mass = []
        for i in range(len(X)):
            if(massType == 'SEP'):
              mass.append(self.separation(X[i],Y[i],X,Y))
            elif(massType == 'COH'):
              mass.append(self.cohesion(X[i],Y[i],X,Y))
        
        return mass
    
    def separation(self,xq,classe,X,Y):
        sumOfDistances = 0
        distances =  scipy.spatial.distance.cdist(xq.reshape(1,-1), X, 'euclidean')

        for i in range(len(X)):
            if(Y[i] != classe):
                sumOfDistances += distances[0][i]
        
        mass = 1/(np.log2(sumOfDistances))

        return mass

    def cohesion(self,xq,classe,X,Y):
        sumOfDistances = 0
        distances =  scipy.spatial.distance.cdist(xq.reshape(1,-1), X, 'euclidean')

        for i in range(len(X)):
            if(Y[i] == classe):
                sumOfDistances += distances[0][i]
        
        mass = 1/(np.log2(sumOfDistances))

        return mass

    def predict(self,XTest):
        finalOutput = []
        distances = scipy.spatial.distance.cdist( self.X , XTest, 'euclidean')

        for i in range(len(XTest)):
            d = []
            votes = []
            for j in range(len(self.X)):
                strength = (self.massX[j])/((np.power(distances[j][i],2))+0.000000000000001)
                d.append([strength,j])
            d.sort(key=lambda tup: tup[0],reverse=True)
            d = d[0:self.k]
            for distance, j in d:
                votes.append(self.Y[j])
            answer = Counter(votes).most_common(1)[0][0]
            finalOutput.append(answer)
        
        return np.array(finalOutput)