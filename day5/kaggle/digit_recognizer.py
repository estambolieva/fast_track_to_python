import h2o
from h2o.estimators.deeplearning import H2ODeepLearningEstimator

import os
# initialize an h2o cluster
import subprocess as sp
import sys
import os.path as p
import h2o

# path of h2o jar file
h2o_path = p.join(sys.prefix, "h2o_jar", "h2o.jar")
# subprocess to launch h2o
# the command can be further modified to include virtual machine parameters
sp.Popen("java -jar " + h2o_path)
# h2o.init() call to verify that h2o launch is successfull
h2o.init()

# then load your training and testing data into the 'train' and 'test' variables
# using H2O's data frames
curr_directory = os.path.dirname(os.path.realpath(__file__))
train_file = 'train.csv'
test_file = 'test.csv'
train = h2o.import_file(os.path.join(curr_directory, "data", train_file))
test = h2o.import_file(os.path.join(curr_directory, "data", test_file))

# Take a look at the dimensions of your data frames
# notice that test is one column less than train, that's because
# test doesn't contain the response column, listed as 'label', in the train data set
print train.shape
print test.shape

print "describe"
print train.describe()

# If you want to see all the column names you can use train.columns or train.names
# uncomment the below to see examples
print "First column of the data is  " + str(train.names) # looks at the first column name in your data frame
print train.columns
print test.columns   # gives you all of the column names in your data frame

# Split your train data set from train.csv into a train and test set (where both sets have a response column)
# you can split the data as you want, the example below splits the data 80/20
# First use .runif to assign a random number to each row, from a uniform set of random numbers between 0 and 1
r = train.runif()

# all values of r under .8 are assigned to 'train_split' (80 percent)
train_split = train[r  < 0.8]
# all values of r equal or above .8 are assigned 'valid_split' (20 percent)
valid_split = train[r >= 0.8]

print "training set size is " + str(train_split.shape)
print "validation set size is " + str(valid_split.shape)

# Encode the response column as categorical ('label' in the train.csv data set lists the actual handwritten digit)
train_split["label"] = train_split["label"].asfactor()
valid_split["label"] = valid_split["label"].asfactor()

# set the parameters of your Deep Learning model
model = H2ODeepLearningEstimator(
        distribution="multinomial",
        activation="RectifierWithDropout",
        hidden=[100,200,100],
        input_dropout_ratio=0.2,
        sparse=True,
        l1=1e-5,
        epochs=100)

# train your model on your train_split data set, and then validate it on the valid_split set
# x is the list of column names excluding the response column (all of your features)
# y is the name of the response column ('label')
model.train(
        x= train.names[1:785],
        y=train.names[0],
        training_frame=train_split,
        validation_frame=valid_split)