#Feature Extraction with text
import numpy as np 
import pandas as pd 

df = pd.read_csv('smsspamcollection.tsv', sep='\t')

from sklearn.model_selection import train_test_split

X=df['message']
y=df['label']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33,random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

#FIT VECTORIZER TO THE DATA (build a vocab, count the number of words...)
#TRANSFORM THE ORIGINAL TEXT MESSAGE --> VECTOR

X_train_counts=count_vect.fit_transform(X_train)

xtraincounts = X_train_counts.shape
print(xtraincounts)
#Result: (3733, 7082)

#from sklearn.feature_extraction.text import TfidfTransformer
#tfidf_transformer = TfidfTransformer()

#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#print(X_train_tfidf.shape)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)

from sklearn.svm import LinearSVC
clf = LinearSVC()
clf.fit(X_train_tfidf,y_train)
print(clf.fit(X_train_tfidf,y_train))

from sklearn.pipeline import Pipeline

text_clf=Pipeline([('tfidf',TfidfVectorizer()),('clf',LinearSVC())])

text_clf.fit(X_train, y_train)

predictions= text_clf.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

from sklearn import metrics

acc=metrics.accuracy_score(y_test, predictions)
print(acc)
#Result = .989668297988037

#test_predict=text_clf.predict(["Congratuations!  You've been selected as a winner.  TEXT WON to 44255"])
test_predict=text_clf.predict(["I'm running late.  I'll call when I'm on my way home."])

print(test_predict)