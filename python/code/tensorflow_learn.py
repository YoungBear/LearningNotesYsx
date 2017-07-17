#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Import the library
import tensorflow as tf

# Define the graph

hello_op = tf.constant('Hello, TensorFlow!')
a = tf.constant(10)
b = tf.constant(32)
compute_op = tf.add(a, b)

# Define the session to run graph
with tf.Session() as sess:
	print(sess.run(hello_op))
	print(sess.run(compute_op))
