import numpy as np
import pandas as pd
import scikitplot as skplt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_validate, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt


roguev_df = pd.read_csv('data.csv')
X = roguev_df[['hadamardDim1','hadamardDim2','hadamardDim3','hadamardDim4','hadamardDim5','hadamardDim6','hadamardDim7','hadamardDim8','hadamardDim9','hadamardDim10','hadamardDim11','hadamardDim12','hadamardDim13','hadamardDim14','hadamardDim15','hadamardDim16','hadamardDim17','hadamardDim18','hadamardDim19','hadamardDim20','hadamardDim21','hadamardDim22','hadamardDim23','hadamardDim24','hadamardDim25','hadamardDim26','hadamardDim27','hadamardDim28','hadamardDim29','hadamardDim30','hadamardDim31','hadamardDim32','hadamardDim33','hadamardDim34','hadamardDim35','hadamardDim36','hadamardDim37','hadamardDim38','hadamardDim39','hadamardDim40','hadamardDim41','hadamardDim42','hadamardDim43','hadamardDim44','hadamardDim45','hadamardDim46','hadamardDim47','hadamardDim48','hadamardDim49','hadamardDim50','hadamardDim51','hadamardDim52','hadamardDim53','hadamardDim54','hadamardDim55','hadamardDim56','hadamardDim57','hadamardDim58','hadamardDim59','hadamardDim60','hadamardDim61','hadamardDim62','hadamardDim63','hadamardDim64','hadamardDim65','hadamardDim66','hadamardDim67','hadamardDim68','hadamardDim69','hadamardDim70','hadamardDim71','hadamardDim72','hadamardDim73','hadamardDim74','hadamardDim75','hadamardDim76','hadamardDim77','hadamardDim78','hadamardDim79','hadamardDim80','hadamardDim81','hadamardDim82','hadamardDim83','hadamardDim84','hadamardDim85','hadamardDim86','hadamardDim87','hadamardDim88','hadamardDim89','hadamardDim90','hadamardDim91','hadamardDim92','hadamardDim93','hadamardDim94','hadamardDim95','hadamardDim96','hadamardDim97','hadamardDim98','hadamardDim99','hadamardDim100','hadamardDim101','hadamardDim102','hadamardDim103','hadamardDim104','hadamardDim105','hadamardDim106','hadamardDim107','hadamardDim108','hadamardDim109','hadamardDim110','hadamardDim111','hadamardDim112','hadamardDim113','hadamardDim114','hadamardDim115','hadamardDim116','hadamardDim117','hadamardDim118','hadamardDim119','hadamardDim120','hadamardDim121','hadamardDim122','hadamardDim123','hadamardDim124','hadamardDim125','hadamardDim126','hadamardDim127','hadamardDim128']]
y = np.ravel(roguev_df[['catagory']])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101, shuffle = True)
model= RandomForestClassifier(n_estimators=16)
model.fit(X_train, y_train)

predictions = (model.predict(X_test))

random_forest_score = (model.score(X_train,y_train))
random_forest_score_test = (model.score(X_test,y_test) )

print (random_forest_score)
print (random_forest_score_test)

#scores = cross_val_score(model, X, y, cv=5)
#print ("validated: ",  scores)

probs = model.predict_proba(X_test)

skplt.metrics.plot_roc(y_test, probs)
plt.savefig('testplot.png')

skplt.metrics.plot_precision_recall(y_test, probs)
plt.savefig('pr-curve.png')

#
#plt.scatter(y_test, predictions)
#plt.xlabel("True Values")
#plt.ylabel("Predictions")
#plt.savefig('testplot.png')
