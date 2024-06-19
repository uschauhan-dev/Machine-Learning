import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
monthly_sales = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
plt.plot(monthly_sales, color = 'b',marker = "o", ms=20)
plt.xlabel('Months')
plt.ylabel('Monthly Sales ')
plt.title('company sales data')
plt.grid()
plt.savefig("sales_data.jpg")
plt.show()