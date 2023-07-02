import numpy
import matplotlib.pyplot as plt

a = [5,7,8,7,2,17,2,9,4,11,12,9,6]
b = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(a, b)
plt.show()

c = numpy.random.normal(5.0, 1.0, 1000)
d = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(c, d)
plt.show()
