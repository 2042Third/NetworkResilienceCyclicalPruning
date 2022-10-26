import numpy as np
import torch
import dataReader

class cifarData:
    label_dict = np.array([])
    labels = np.array([])
    data = np.array([])
    
    def _init_(self,label_dictIn,labelsIn,dataIn):
        self.label_dict = label_dictIn
        self.labels = labelsIn
        self.data = dataIn
    # 1 to 10000
    def getName(self, indx):
        return self.label_dict[self.getLabel(indx)]
    # 1 to 10000
    def getData(self, indx):
        return self.data[indx]
    def getLabel(self, indx):
        return self.labels[indx]