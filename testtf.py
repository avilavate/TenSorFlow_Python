import tensorflow as tensorflow

sess= tensorflow.Session()

hello= tensorflow.constant("Hello World from tensorFlow")

print(sess.run(hello))

a= tensorflow.constant(10)
b= tensorflow.constant(20)

print("Addition of a and b {0}: ".format(sess.run(a+b)))
