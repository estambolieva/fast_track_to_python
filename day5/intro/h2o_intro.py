import subprocess as sp
import sys
import os.path as p

import numpy as np

import h2o
# 1. initialize h2o
# 1.1 find path of h2o jar
h2o_path = p.join(sys.prefix, "h2o_jar", "h2o.jar")
# 1.2 subprocess to launch h2o
# the command can be further modified to include virtual machine parameters
sp.Popen("java -jar " + h2o_path)
# 1.3 h2o.init() call to verify that h2o launch is successfull
h2o.init()

# 2. create an H2OFrame object
# 2.1 from a tuple
df = h2o.H2OFrame(zip(*((1, 2, 3),
                        ('a', 'b', 'c'),
                        (0.1, 0.2, 0.3))))
print df
# 2.2 from a list
df = h2o.H2OFrame(zip(*[[11, 22, 33],
                        ['aa', 'bb', 'cc'],
                        [1.1, 1.2, 1.3]]))
print df
# 2.3 from an ordered dictionary
# NOTE: note how the order of the columns is the following: A, C and B, D
df = h2o.H2OFrame({'A': [1, 2, 3],
                   'B': ['a', 'b', 'c'],
                   'C': [0.1, 0.2, 0.3],
                   'D' : ['oh', ',', 'really']})
print df
# 2.3.1 from an ordered dictionary and specify column types
df1 = h2o.H2OFrame.from_python({'A': [1, 2, 3],
                               'B': ['a', 'b', 'c'],
                               'C': [0.1, 0.2, 0.3],
                               'D' : ['oh', ',', 'really']},
                                column_types = ['numeric','string','numeric','string'])
print df

# 3. display
# 3.1 all column types
print df.types
# 3.2 all column names
print df.columns

# 4. VIEWING DATA - create a 100x4 matrix
## numpy.random.randn - returns a sample from the standard normal distribution
df = h2o.H2OFrame.from_python(np.random.randn(100,4).tolist(),
                              column_names=['A', 'B', 'C', 'D'])
# 4.1 view the first 10 rows of each column
print df.head()
# 4.2 view the last 5 rows of each column
print df.tail(5)
# 4.3 view compression imformation, distribution, and summary stats
print df.describe()

# 5. SELECTION - select and display a single column
# by its name
print df['A']
# by index
print df[2]
# select multiple columns by name
cols = ['A', 'D']
print df[cols]
# select multiple columns by index - slicing
print df[0:2]
# select muptiple rows resulting in an H2OFrame - 5x4
print df[2:7, :]
# select a row based on a criterion
# here we use the previous example as the df random number 2D array is generated every run
print df1[df1['D'] == 'really', :]
print df1[df1['C'] == 0.2, :]

# 6 MISSING DATA
df3 = h2o.H2OFrame.from_python({'A': [1, 2, 3,None,''],
                                'B': ['a', 'a', 'b', 'NA', 'NA'],
                                'C': ['hello', 'all', 'world', None, None],
                                'D': ['12MAR2015:11:00:00',None, '13MAR2015:12:00:00',
                                      None, '14MAR2015:13:00:00']},
                               column_types=['numeric', 'enum', 'string', 'time'])
print df3
# 6.1 find missing data rows in column 'A'
# a missing etry is found if on its index there is 1, if the entry exits - there is a 0
print df3["A"].isna()

# 6.2 determine all missing value locations in the 2D array
print df3.isna()

# if we want to insert some missing values in our dataset while testing
## warning: this operation modifies the original array, invoke on a copy of the original array
df4 = h2o.H2OFrame.from_python(np.random.randn(3, 5).tolist(),
                              column_names=['A', 'B', 'C', 'D', 'E'])
print df4
# 6.3 make 20% of the values missing values
df4.insert_missing_values(0.2)
print df4



