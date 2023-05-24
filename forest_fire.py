#Import Libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

#Load Data
data = pd.read_csv("Forest_fire.csv")
data = np.array(data)

#Transform Data
X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('float')
X = X.astype('float')

#Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Train Model
model = LogisticRegression()


model.fit(X_train, y_train)

# inputt=[int(x) for x in "45 32 60".split(' ')]
# final=[np.array(inputt)]

b = model.predict_proba(X_test)


pickle.dump(model,open('model.pkl','wb'))


