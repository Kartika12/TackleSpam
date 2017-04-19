from sklearn.naive_bayes import GaussianNB
import numpy as np
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
x = np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
model = GaussianNB()

model.fit(x,y)

predicted = model.predict([[1,2],[3,4]])
print (predicted)