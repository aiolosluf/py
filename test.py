import random
import pandas as pd
import pandas_profiling

data = pd.read_csv('titanic.csv')
profile = data.profile_report(title='Titanic Dataset')
profile.to_file(output_file='titanic_report.html')

# for i in range(0,10):
#     print(i)