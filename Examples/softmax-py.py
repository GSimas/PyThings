''' This is an example python code with tensorflow
    MNIST library tutorial, OCR
    
    Dependencies
    Python 3.5.x (64bit)
    tensorflow, numpy, os
    Developer: Gustavo S.
    Date: June-2017
    References: https://www.tensorflow.org/get_started/mnist/beginners
'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #supress level2- warnings

#import dependencies
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#read mnist dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

#initial definitions
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

#y labels softmax function
y = tf.nn.softmax(tf.matmul(x,W) + b)

#cross-entropy calc
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

#Grad Descent
train_step = tf.train.GradientDescentOptimizer(0.8).minimize(cross_entropy)

#create tf session
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

#train model
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(500)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    print("Training percentage:{} %".format(_/10))

#model evaluation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#print result
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))