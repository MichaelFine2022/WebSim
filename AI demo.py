import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
import pandas

def stripAdj(path):
    data = pandas.read_csv(path)
    data = data.drop(columns=['Adj Close'])
    print(data)

class stockSet(Dataset):
    def __init__(self):
        xy = np.loadtxt('ZYXI.csv',delimiter=",",dtype=np.float64, skiprows=1)
        self.x = torch.from_numpy(xy[:, 1:])
        self.y = torch.from_numpy(xy[:,[0]])
        self.n_samples = xy.shape[0]
        
    def __getitem__(self, index):
        return self.x[index], self.y[index]
    
    def __len__(self):
        return self.n_samples
stripAdj('ZYXI.csv')
dataset = stockSet()
first_data = dataset[0]
Date,Open,High,Low,Close,Volume = first_data
print(Date, Open)