import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/2019 Winter Data Science Intern Challenge Data Set.csv')
data.head()

plt.scatter(data.created_at, data.order_amount)
plt.show()
