import subprocess as sp
import sys
import os.path as p

import numpy as np

import h2o
from h2o import frame
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
# determine whether the values of this column are of type - numeric
print df['A'].isnumeric()

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

# 6.4 perform descriptive statistics - get the mean value of each column in df4
# na_rm == NA removal
print df4.mean(na_rm=True)
# df3 has NA elements, after removal we get the mean value for column 1
print df3.mean(na_rm=True)
# here we fail to compute the mean value for column 1 since we have not cleaned NAs
print df3.mean()
print df3['A'].mean(na_rm=True)

# 6.5 applying a lambda fuction to each column
# returns an H2O Frame with 1 row which holds the results of the lambda function
print df3.apply(lambda x: x.mean(na_rm=True))

# 6.6 sum the elements of each column
print df.apply(lambda row: row.sum())

# 6.7 sum the elements of each row
row_sums =  df.apply(lambda row: row.sum(), axis=1)
print row_sums.shape
# for viewing purposes, only the 10 lines of the result are prined
print row_sums

# 7. plotting and discretizing data - HISTOGRAMS
arr = [[x] for x in np.random.randint(0, 7, size=100)]
df6 = h2o.H2OFrame(arr) # a 2D array
# df7 is a matrix with 100 columns and 1 row with values in [0,7]
print df6

#print df6[0].hist()
## print df6.hist(plot=True)

# 8. find string repetitions
df7 = h2o.H2OFrame.from_python(['Hello', 'World', 'Welcome', 'To', 'H2O', 'World'])
# count how many times 'W' occurs in the frame
print df7.countmatches('l')
print df7.countmatches('W')

# 8.1 replace the first occurrence of "W" with "x" in each entry
print df7.sub('W', 'x')
print df7.sub('l', '00')

# 8.2 replace all occurrences of "l" with "x" in ach entry
print df7.gsub("l", "x")

# 9 MERGING - merge df8 and df9, adds the df9 rows to the bottom of all df8 rows
df8 = h2o.H2OFrame.from_python(np.random.randn(100,4).tolist(),column_names=list('ABCD')) # (100,4)
df9 = h2o.H2OFrame.from_python(np.random.randn(100,4).tolist(),column_names=list('WXYZ')) # (100,4)
df8.rbind(df9) # row bind, e.g. add after the last row
print df8.shape

# we have failed to merge the two H2OFrames. For successful matching the column names
# and column types must match
df9 = h2o.H2OFrame.from_python(np.random.randn(100,4).tolist(),column_names=list('ABCD')) # (100,4)
df8.rbind(df9)
print df8.shape

# 9.1 match two frames together by matching column names
# merge df10 with df11
## ?? a nan entry is inserted in 'n' followed by the first entry of 'A'
df10 = h2o.H2OFrame.from_python( {'A': ['Hello', 'World', 'Welcome', 'To', 'H2O', 'World'],
                                 'n': [0,1,2,3,4,5]})
df11 = h2o.H2OFrame.from_python([[1],[2],[5],[4],[3],[0]], column_names=['n'])
print df10.merge(df11)

# 10 GROUPING
df12 = h2o.H2OFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                     'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                     'C' : np.random.randn(8).tolist(),
                     'D' : np.random.randn(8).tolist()})
print df12
# 10.1 group by column and apply function
# collapse 'A' to its unique elements, and sum the elements according to that in the other columns
# if a column has no numerical value, it just prints the number of times each entry in column 'A' occurs
# in the original array
## NEEDS A PIC TO EXPLAIN
print df12.group_by('A').sum().frame

# 10.2 group by different columns and apply fuction
df13 = df12.group_by(['A', 'B']).sum().frame
print df13

# join the results in the original 2D array
print df12.merge(df13)

# 11 using DATE and time data
df14 = h2o.H2OFrame.from_python({'D': ['18OCT2015:11:00:00','19OCT2015:12:00:00','20OCT2015:13:00:00'],
                                 'A': ['1AUG2016:11:00:00','2AUG2016:12:00:00','3AUG2016:13:00:00']},
                                column_types=['time', 'time'])
print df14.types

# 11.1 display the day of the month
print df14['A'].day()

# 11.2 display the day of the week
print df14['A'].dayOfWeek()

# 12 Categoricals
print df12.types

# 12.1 determine whether a categorical column exits
print df12.anyfactor()

# 12.2 view categorical levels in a single column
print df12['B'].levels() # prints [one, two, three]

# 12.3 create categorical interactions between columns
print df12.interaction(['A','B'], pairwise=False, max_factors=2,min_occurrence=1)

# 12.4 create an interaction of a categorical column wiht itself
bb_df12 = df12.interaction(['B','B'], pairwise=False, max_factors=2,min_occurrence=1)
print bb_df12

# 12.5 then add this new B_B column to the original 2D array
df15 = df12.cbind(bb_df12) # column bind, e.g. add after the last column

# 13 loading and saving data - from disk, NFS, HDFS, HTTP address
# supported files - CSV, ORC, SVMLite, ARFF, XLS, XLST

# 13.1 from the same machine running H2O
##h2o.upload_file("/pathToFile/fileName")

# 13.2 from a the machine that runs Python to the machine that runs H2O
##h2o.import_file("/pathToFile/filename")

# 13.3 save an H2OFrame to the machine running H2O
##h2o.export_file(df, "/pathToFile/filename")

# 13.4 save an H2OFrame from the machine running H2O to the machine running Python
##h2o.download_csv(df, "/pathToFile/filename")