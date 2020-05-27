data = [1, 22, 3, 54, 5, 0, 21, 43]
n = len(data)

for i in range(n-1):
     for j in range(n-i-1):
         if data[j] > data[j+1]:
             data[j], data[j+1] = data[j+1], data[j]
print(data)