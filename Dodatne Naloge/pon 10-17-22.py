import numpy as np

from random import *

karte = list(range(1, 7)) * 2
shuffle(karte)
peter, pavel = karte[:6], karte[6:]
