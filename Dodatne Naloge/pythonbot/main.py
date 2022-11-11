from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from code import predict
s = "abcabcbb"
test = ''
test = test + s[0]

for crka in range(len(s)):
    if test[crka - 1] != s[crka]:
        test = test + s[crka]
    print(test)

