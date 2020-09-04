# TASK 1
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4], index=['s1','s2','s3','s4','s5'])
print(heights_A.shape)

# TASK 2 
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
print(weights_A.dtype)

# TASK 3
df_A = pd.DataFrame([heights_A,weights_A],index=['Student_height','Student_weight']).T
print(df_A.shape)

# TASK 4
import numpy as np
np.random.seed(100)
heights_B = pd.Series(np.random.normal(170.0,25.0,5),index=['s1','s2','s3','s4','s5'])
np.random.seed(100)
weights_B = pd.Series(np.random.normal(75.0,12.0,5),index=['s1','s2','s3','s4','s5'])
print(heights_B.mean())

# TASK 5
df_B = pd.DataFrame([heights_B,weights_B],index=['Student_height','Student_weight']).T
print(df_B.columns)

# TASK 6
p = pd.Panel({'ClassA':df_A,'ClassB':df_B})
print(p.shape)