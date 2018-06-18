import numpy as np
from scipy.special import lpmv

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-m", "--m", dest="m")
parser.add_argument("-n", "--n", dest="n")
args = parser.parse_args()

x = np.linspace(-1,1, 100)

m = int(args.m)
n = int(args.n)

for i in x:
    print i, lpmv(n,m,i)
