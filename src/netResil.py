import numpy as np
import torch
import dataReader

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

if __name__ == '__main__':
  cifar = unpickle("../cifar-10-batches-py/test_batch")
  dics = unpickle("../cifar-10-batches-py/batches.meta")
  labels = np.array(cifar[b'labels'])
  data   = np.array(cifar[b'data'])
  label_names = np.array(dics[b'label_names'])
  cf = dataReader.cifarData()
  cf._init_(label_names,labels,data)
  print(cf.getData(0))