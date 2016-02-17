# -*- coding: utf-8 -*-
'''
Artificial Neural Network for Classification and Curvefitting problems.

This script is written for activating a simple artificial neural network. (ANN)
Please refer to the step as follows.

1. Import a sample example set from Matlab.
    * You need to understand the structure and the characteristics of the inputs and outputs
2.


                                                                    Written by Hyungwon Yang
                                                                                2016. 02. 07
                                                                                    EMCS Lab
'''

import theano.tensor as T

class ANN_model(object):

    def __init__(self,inX,outY,ihMatrix,hoMatrix,hBiasMatrix,oBiasMatrix,learningRate=0.001):
        self.inputs = inX
        self.targets = outY
        self.ihMatrix = ihMatrix
        self.hoMatrix = hoMatrix
        self.hBiasMatrix = hBiasMatrix
        self.oBiasMatrix = oBiasMatrix
        self.lr = learningRate

    # Feedforward Neural Network.
    def fnn(self,methods):
        '''
        You have to choose the methods.
        methods : classification and curvefitting
        '''
        hid = T.nnet.sigmoid(T.dot(self.inputs,self.ihMatrix) + self.hBiasMatrix)
        if methods is 'classification':
            outputStorage = T.nnet.softmax(T.dot(hid,self.hoMatrix) + self.oBiasMatrix)
            outputActivation = T.argmax(outputStorage,axis=1)

        elif methods is 'curvefitting':
            outputStorage = T.dot(hid,self.hoMatrix) + self.oBiasMatrix
            outputActivation = outputStorage

        # estimated inputs
        return outputStorage, outputActivation

    # Stochastic Gradient Descent.
    def sgd(self,outputStorage):
        cost = T.mean(T.nnet.categorical_crossentropy(outputStorage,self.targets))
        params = [self.ihMatrix,self.hoMatrix,self.hBiasMatrix,self.oBiasMatrix]
        gradient = T.grad(cost=cost, wrt=params)
        updates = []
        for p, g in zip(params, gradient):
            updates.append([p, p - g * self.lr])
        return cost, updates

    def sgd2(self,outputStorage):

        cost = T.mean(T.pow(outputStorage-self.targets,2))/2
        params = [self.ihMatrix,self.hoMatrix,self.hBiasMatrix,self.oBiasMatrix]
        gradient = T.grad(cost=cost,wrt=params)
        updates = []
        for p, g in zip(params, gradient):
            updates.append([p, p - g * self.lr])
        return cost, updates
