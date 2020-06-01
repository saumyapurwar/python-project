import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fd = pd.read_csv('ann.csv')

fd.head()

max_avg = fd['max_avg']
legend = ['Maximum Average', 'Minimum Average']
age = fd['age']
#plt.hist([min_avg, max_avg], color=['orange', 'green'])
plt.plot(age, max_avg, 'o')
plt.xlabel("Age")
plt.ylabel("Maximum Average Speed")
plt.legend(legend)
plt.xlim(10, 25)
plt.ylim(0, 4)
plt.title('Speed Analysis With Respect To Age')
plt.show()
