# TASK 1
import pandas as pd
import numpy as np
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4], index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame([heights_A,weights_A],index=['Student_height','Student_weight']).T
df_A.loc['s3'] = np.nan
df_A.loc['s5']['Student_weight'] = np.nan
df_A2 = df_A.dropna()
print(df_A2)