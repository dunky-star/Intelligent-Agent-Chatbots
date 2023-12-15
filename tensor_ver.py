import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
TF_ENABLE_ONEDNN_OPTS=0

print(tf.__version__)


print(tf.reduce_sum(tf.random.normal([1000, 1000])))
