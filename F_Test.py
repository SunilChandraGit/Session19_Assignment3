import pandas as pd
import numpy as np
import scipy.stats as stat

a = [10, 20, 30, 40, 50]  
b = [5, 10, 15, 20, 25]

var_a = np.var(a)
var_b = np.var(b)

f = var_a/var_b

f < stat.f.ppf(0.95, 4, 4)