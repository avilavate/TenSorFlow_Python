import tensorflow as tensorflow
import math
import numpy as num
import matplotlib.pyplot as plt 

num_house =160

num.random.seed(42)

house_size=num.random.randint(1000,3500,size=num_house)

num.random.seed(42)

house_price= house_size*1000+ num.random.randint(20000,70000,size=num_house)

plt.plot(house_size,house_price, 'bx')
plt.xlabel("Size")
plt.ylabel("Price")
plt.show()