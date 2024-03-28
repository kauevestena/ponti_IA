import sys
sys.path.append('..')
sys.path.append('.')
from lib import *

import matplotlib.pyplot as plt

import torch
from PIL import Image
# setup device to use
device = torch.device("cuda")