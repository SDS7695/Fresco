 TASK 1
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4], index=['s1','s2','s3','s4','s5'])
print(heights_A[1])

# TASK 2
print(heights_A[1:4])

# TASK 3
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame([heights_A,weights_A],index=['Student_height','Student_weight']).T
height = df_A['Student_height']
print(type(height))

# TASK 4
df_s1s2 = df_A.loc[['s1','s2']]
print(df_s1s2)

# TASK 5
df_s2s5s1 = df_A.loc[['s2','s5','s1']]
print(df_s2s5s1)

# TASK 6
df_s1s4 = df_A.loc[['s1','s4']]
print(df_s1s4)