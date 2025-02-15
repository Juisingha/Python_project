import matplotlib.pyplot as plt
import numpy as np

Unemployment_data=[]
fpr=open("Unemployment.csv","r")
head=fpr.readline()
line=fpr.readline()
while (len(line) > 0):
        arr = line.strip().split(',')
        Unemployment_data.append(float(arr[1]))
        line = fpr.readline()
fpr.close()
Unemployment_data_np=np.array(Unemployment_data)
mean_Unemployment_data=np.mean(Unemployment_data_np)
max_Unemployment_data=np.max(Unemployment_data_np)
min_Unemployment_data=np.min(Unemployment_data_np)

print(f"Mean Unemployment_data: {mean_Unemployment_data}")
print(f"Max Unemployment_data: {max_Unemployment_data}")
print(f"Min Unemployment_data: {min_Unemployment_data}")

plt.figure(figsize=(10,6))
plt.plot(Unemployment_data_np,label='Maryland unemployment_data',color='blue',marker='o')
plt.title('Unemployment_data in Dataset')
plt.xlabel('Index')
plt.ylabel('Unemployment_data')
plt.grid(True)
plt.legend()
plt.show()



