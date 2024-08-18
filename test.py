import tensorflow as tf

a = tf.constant(4)
b = tf.constant(6)
print(a)
print(b)
c = tf.add(a,b)
print(c)
d = a + b
print(d)
e = tf.subtract(a,b)
print(e)
f = tf.constant([[1,2,3],[4,5,6],[7,8,9]])
print(f)
g = tf.divide(a,b)
print(g)
h = tf.constant(4.0)
print(h)