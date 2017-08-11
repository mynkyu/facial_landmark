import time

start = time.time()

import cv2
import argparse
import itertools
import os

import numpy as np
from PIL import Image
np.set_printoptions(precision=2)

fileDir = os.path.dirname(os.path.realpath(__file__))

x=x.convert('L')
