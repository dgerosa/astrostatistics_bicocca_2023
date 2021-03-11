# G. Richards 2016, based on linear_regression.py by Jake Vanderplas

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

a = 0.5
b = 1.0

# x from 0 to 10
x = 30 * np.random.random(20)

# y = a*x + b with noise
y = a * x + b + np.random.normal(size=x.shape)

# create a linear regression classifier
clf = LinearRegression()
clf.fit(x[:, None], y)

#GTR: Note that these all do the same thing
#print x[:, None]
#print x[:, np.newaxis]
#print x.reshape(-1,1)
#But only the first one actually is readable

# predict y from the data
x_new = np.linspace(0, 30, 100)
y_new = clf.predict(x_new[:, None])

# plot the results
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')
plt.show()
