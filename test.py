import random
import pandas as pd
import pandas_profiling
import sys

# data = pd.read_csv('titanic.csv')
# profile = data.profile_report(title='Titanic Dataset')
# profile.to_file(output_file='titanic_report.html')

# for i in range(0,10):
#     print(i)

import datetime
import time


today = time.strftime("%A")
condition = ''

if today == 'Saturday':
    print('Party!')
elif today == 'Sunday':
    if condition == 'Headache':
        print('Recover, then rest.')
    else:
        print('Rest.')
else:
    print('today is: '+today)