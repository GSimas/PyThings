# -*- coding: utf-8 -*-
"""
Created on Sat May 27 22:26:15 2017

@author: Paulo Batista
ML Classification from Google Developers
"""

from sklearn import tree

features = [[140,1], [130,1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[130,0]]))
