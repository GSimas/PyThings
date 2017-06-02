#adapter from Siraj Raval

from sklearn import tree

#[altura, peso, tamanho sapato]
X = [   [181,80,42], [178, 75, 43], [190, 99, 41], [168,69,39],
        [201,105,38], [168,66,37], [175,78,39], [177, 77, 38],
        [181, 79,44], [166,79,36], [188,88,39], [166,69,39]
    ]

Y = [   'male', 'female', 'male', 'female',
        'male', 'female', 'female', 'female',
        'male', 'female', 'male', 'female'
    ]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[170,70,36]])
print(prediction)