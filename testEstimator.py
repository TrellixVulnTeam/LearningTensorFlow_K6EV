import numpy as np
import tensorflow as tf

# list of features
feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]

# linear regression estimator
estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

# training and evaluation datasets
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7, 0.])