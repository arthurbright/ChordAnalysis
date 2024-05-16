from gencols import gencols
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from tqdm import tqdm
import numpy as np

size = input("enter # of samples: ")
filename = input("enter name of dataset: ")
x_train = []
y_train = []
for i in tqdm(range(int(size))):
  columns, basefreq, ans = gencols(1)
  x_train.append(columns[0])
  y_train.append(ans)
x_train = np.array(x_train)
y_train = np.array(y_train)

ds = TensorDataset(torch.Tensor(x_train), torch.Tensor(y_train))

torch.save(ds, f'{filename}.pt')