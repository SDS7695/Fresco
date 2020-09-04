# TASK 1
import pandas as pd
nameid = pd.Series(range(101, 111))
name = pd.Series(['person' + str(i) for i in range(1, 11)])
master = pd.DataFrame([nameid,name],index=['nameid','name']).T

transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})

mdf = pd.merge(master,transaction,on='nameid',how='inner')
print(mdf)