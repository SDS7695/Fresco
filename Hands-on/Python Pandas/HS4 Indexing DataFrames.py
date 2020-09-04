# TASK 1
import pandas as pd
dates = pd.date_range('2017-09-01','2017-09-15',freq='D')
print(dates[2])

# TASK 2
datelist = ['14-Sep-2017','9-Sep-2017']
dates_to_be_searched = pd.to_datetime(datelist)
print(dates_to_be_searched)

# TASK 3
print(dates_to_be_searched.isin(dates))

# TASK 4
arraylist = [['classA']*5 + ['classB']*5, ['s1', 's2', 's3','s4', 's5']*2]
ls = list(zip(*arraylist))
mi_index = pd.MultiIndex.from_tuples(ls)
print(mi_index)