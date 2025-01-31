import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.arange(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data, cmap=plt.cm.jet)
plt.xlabel('entry a')
plt.ylabel('entry b')

data['a']
data['b']
data['c']
data['d']
plt.show()
