# TASK 1
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4], index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame([heights_A,weights_A],index=['Student_height','Student_weight']).T
df_A['Gender'] = ['M','F','M','M','F']
s = pd.Series([165.4,82.7,'F'],index=['Student_height', 'Student_weight', 'Gender'],name='s6')
df_AA = df_A.append(s)
print(df_AA)

# TASK 2
import numpy as np
np.random.seed(100)
heights_B = pd.Series(np.random.normal(170.0,25.0,5),index=['s1','s2','s3','s4','s5'])
np.random.seed(100)
weights_B = pd.Series(np.random.normal(75.0,12.0,5),index=['s1','s2','s3','s4','s5'])
df_B = pd.DataFrame([heights_B,weights_B],index=['Student_height','Student_weight']).T
df_B.index=['s7','s8','s9','s10','s11']
df_B['Gender'] = ['F','M','F','F','M']
df = pd.concat([df_AA,df_B])
print(df)