# TASK 1
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4], index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame([heights_A,weights_A],index=['Student_height','Student_weight']).T
df_A.to_csv('classA.csv')

# TASK 2
df_A2 = pd.read_csv('classA.csv')
print(df_A2)

# TASK 3
df_A3 = pd.read_csv('classA.csv',index_col=0)
print(df_A3)

# TASK 4
import numpy as np
np.random.seed(100)
heights_B = pd.Series(np.random.normal(170.0,25.0,5),index=['s1','s2','s3','s4','s5'])
np.random.seed(100)
weights_B = pd.Series(np.random.normal(75.0,12.0,5),index=['s1','s2','s3','s4','s5'])
df_B = pd.DataFrame([heights_B,weights_B],index=['Student_height','Student_weight']).T
df_B.to_csv('classB.csv',index=False)

# TASK 5
df_B2 = pd.read_csv('classB.csv')
print(df_B2)

 TASK 6
df_B3 = pd.read_csv('classB.csv',header=None)
print(df_B3)

# TASK 7
df_B4 = pd.read_csv('classB.csv',header=None,skiprows=2)
print(df_B4)