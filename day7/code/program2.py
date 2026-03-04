# import a module with an alias
# - alias: 
#   - temporary name assigned to the module
#   - instead of using the module name to access the member, use alias
# - famous aliases
#   - import numpy as np
#   - import pandas as pd
#   - import matplotlib.pyplot as plt
#   - import seaborn as sns
#   - import pytorch as pt
#   - import tensorflow as tf

import math_operations as mo

# import the functions from math_operations module
mo.add(40, 60)
mo.subtract(40, 60)
mo.divide(40, 60)
mo.multiply(40, 60)
print(f"PI = {mo.PI}")