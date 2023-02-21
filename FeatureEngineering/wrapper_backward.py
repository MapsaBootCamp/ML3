import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.datasets import load_wine
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score, classification_report


def decision_tree_backward(X: np.ndarray, y: np.ndarray, n_selected_features: int):
    """
    This function implements the backward feature selection algorithm based on decision tree
    Input
    -----
    X: {numpy array}, shape (n_samples, n_features)
        input data
    y: {numpy array}, shape (n_samples,)
        input class labels
    n_selected_features : {int}
        number of selected features
    Output
    ------
    F: {numpy array}, shape (n_features, )
        index of selected features
    """

    n_samples, n_features = X.shape
    # using 10 fold cross validation
    cv = KFold(n_splits=10, shuffle=True, random_state=42)
    # choose decision tree as the classifier
    clf = SVC()

    # selected feature set, initialized to contain all features
    F = list(range(n_features))
    count = n_features

    while count > n_selected_features:
        max_acc = 0
        for i in range(n_features):
            if i in F:
                F.remove(i)
                X_tmp = X[:, F]
                acc = 0
                for train, test in cv.split(X):
                    clf.fit(X_tmp[train], y[train])
                    y_predict = clf.predict(X_tmp[test])
                    acc_tmp = accuracy_score(y[test], y_predict)
                    acc += acc_tmp
                acc = float(acc)/10
                F.append(i)
                # record the feature which results in the largest accuracy
                if acc > max_acc:
                    max_acc = acc
                    idx = i
        # delete the feature which results in the largest accuracy
        print("remove feature: ", data.feature_names[idx])
        F.remove(idx)
        count -= 1
    return np.array(F)


if __name__ == "__main__":
    data = load_wine()
    X = data.data
    y = data.target

    selected_features = decision_tree_backward(X, y, 10)
    for indx in selected_features:
        print(data.feature_names[indx])

    X_train, X_test, y_train, y_test = train_test_split(
        X[:, selected_features], y, test_size=0.2, random_state=42)

    clf = SVC()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print(classification_report(y_predict, y_test))
    # a = [1, 2, 3, 4]

    # for elm in range(1, 4):
    #     a.remove(elm)
    #     print("before: ", a)
    #     a.append(elm)
    #     print("after: ", a)
