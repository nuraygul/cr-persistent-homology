
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from generate_dataset import generate_dataset
from persistence_features import compute_diagrams, betti_curve, persistence_image

def prepare_data():
    data, labels = generate_dataset()
    X, y = [], []
    for fX, gX in data:
        diag_f = compute_diagrams(fX)
        diag_g = compute_diagrams(gX)
        # Use difference of persistence images as features
        pi_diff = persistence_image(diag_f) - persistence_image(diag_g)
        bc_diff = betti_curve(diag_f) - betti_curve(diag_g)
        features = np.concatenate([pi_diff, bc_diff])
        X.append(features)
        y.append(labels.pop(0))
    return np.array(X), np.array(y)

def train_classifier():
    X, y = prepare_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    clf = SVC(kernel='rbf')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_classifier()
