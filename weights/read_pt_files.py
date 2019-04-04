import os
import argparse
import math
import torch
parser   = argparse.ArgumentParser()
parser.add_argument('-file', type=str, default='',help='')

FLAGS, unparsed = parser.parse_known_args()
dataset = FLAGS.file
vocab = torch.load(FLAGS.file)
print(vocab)


