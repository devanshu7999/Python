import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start=1,stop=50)
y = np.multiply(x,3)

plt.subplot(2,2,1)
plt.plot(x,y)

languages = ['Java','python','PHP','JavaScript','C#','C++']

popularity = [22.2,17.6,8.8,8,7.7,6.7]

plt.xlabel('Languages')
plt.ylabel('Popularity')

plt.subplot(2,2,2)
plt.bar(languages,popularity)

plt.subplot(2,2,3)
plt.pie(popularity,colors=["#1f77b4", "#ff7f0e","#2ca02c", "#d62728", "#9467bd","#8c564b"],labels=languages)

x = np.random.randint(1,201,size=200)
y = np.random.randint(1,201,size=200)

plt.subplot(2,2,4)
plt.scatter(x,y)

plt.show()