### Text classifcation project - We'll be able to tell wheter a movie review is positive
### or negative based off the texts.

import numpy as np 
import pandas as pd 

df = pd.read_csv('moviereviews.tsv', sep='\t')
#check the first few rows
print(df.head())
#check for missing values
print(df.isnull().sum())
#We find we're missing 35 reviews so I'll just drop them.
df.dropna(inplace=True)
print(df.isnull().sum())
#label     0
#review    0

#now lets check for whitespace in the review column


blanks = []
#(index, label, review text)
for i, lb, rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)
print(blanks)
#Result:
#[57, 71, 147, 151, 283, 307, 313, 323, 343, 351, 427, 501, 633, 675, 815, 851, 977, 1079, 1299, 1455, 1493, 1525, 1531, 1763, 1851, 1905, 1993]
#The above are indexes positions for fields with whitespace in them. We can drop them as well.

df.drop(blanks, inplace=True)
print(len(df))

#Now that the data is clean, we can split the data into a training and test set

from sklearn.model_selection import train_test_split

X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=42)

#Build the pipeline
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

text_clf=Pipeline([('tfidf', TfidfVectorizer()), ('clf',LinearSVC())])

text_clf.fit(X_train, y_train)
print(text_clf.fit(X_train, y_train))

predictions = text_clf.predict(X_test)

#analyze results

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

from sklearn import metrics

acc=metrics.accuracy_score(y_test, predictions)
print(acc)

test_predict=text_clf.predict(["Bad movie!"])

print(test_predict)