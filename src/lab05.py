"""Lab 5 starter code: regression models."""
import numpy as np

def add_bias(X):
    raise NotImplementedError('TODO: implement this')

def least_squares(X, y):
    """Return weights w (first element is the bias) minimising squared error."""
    raise NotImplementedError('TODO: implement this')

def gradient_descent(X, y, lr=0.05, epochs=2000):
    """Batch gradient descent on mean squared error. Return w (bias first)."""
    raise NotImplementedError('TODO: implement this')

def bayesian_linear_regression(X, y, alpha=1.0, beta=25.0):
    """Posterior mean and covariance with prior N(0, alpha^-1 I) and noise precision beta."""
    raise NotImplementedError('TODO: implement this')

def predict(w, X):
    raise NotImplementedError('TODO: implement this')
