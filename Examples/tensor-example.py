''' This is an example code for python and tensorflow
    Create tensors and a simple machine learning model
    Gradient Descent - Least Square Errors
    
    Dependencies
    Python 3.5.x (64bit)
    tensorflow, numpy, pandas, matplotlib, os
    Developer: Gustavo S.
    Date: June-2017
    References: tensorflow.org
'''
#Importing modules
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #supress level2- warnings

import tensorflow as tf
import matplotlib.pyplot as plt

#create nodes 
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
print(node1, node2)

#create session
sess = tf.Session()
print(sess.run([node1,node2]))

#addition node
node3 = tf.add(node1, node2)
print("node3:", node3)
print("Session run node3:", sess.run(node3))

#tensors placeholders
a = tf.placeholder(tf.float32) 
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, {a: 3, b:4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2,4]}))

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

#Linear Model
W = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b

#init session
init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, {x:[1,2,3,4]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

#gradient descent function
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)

numW = [W.eval(sess)] #store W value
numb = [b.eval(sess)] #store b value

#training loop
for i in range(1000):
    sess.run(train, {x: [1,2,3,4], y:[0,-1,-2,-3]})
    sess.run([W,b])
    numW.append(W.eval(sess))
    numb.append(b.eval(sess))

plt.plot(numW) #plot values of W
plt.plot(numb) #plot values of b
plt.ylabel("W and b values")
plt.show()
