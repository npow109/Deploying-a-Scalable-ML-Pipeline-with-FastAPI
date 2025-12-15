import pytest
# TODO: add necessary import
from ml.model import compute_model_metrics, train_model, inference
from numpy import random
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_compute_metrics():
    """
    # Checks that the compute_metrics function correctly returns the 
    # precision, recall, and fbeta variables 
    """
    # Your code here
    y = [1,0,1,0,0,0,0,1,0,1,0]
    preds = [1,0,1,0,0,0,0,1,0,1,1]
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert(precision is not None)
    assert(recall is not None)
    assert(fbeta is not None)



# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    # Checks that the train_model function returns the correct model 
    # (RandomForestClassifier)
    """
    # Your code here
    X_train = random.randint(10, size=(3, 20))
    y_train = random.randint(1, size=(3))
    i = train_model(X_train, y_train)
    assert(isinstance(i, RandomForestClassifier))


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    # Checks that the inference function returns the preds variable
    """
    # Your code here
    X_train = random.randint(10, size=(3, 20))
    y_train = random.randint(1, size=(3))
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    assert(preds is not None)
