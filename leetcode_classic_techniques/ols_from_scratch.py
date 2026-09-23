#ols from scratch

import numpy as np

def fit_ols(X, y):
    X = np.column_stack([np.ones(len(X)), X])      # intercept column
    beta = np.linalg.solve(X.T @ X, X.T @ y)        # normal equations: (XᵀX)β = Xᵀy
    return beta

def predict(X, beta):
    X = np.column_stack([np.ones(len(X)), X])
    return X @ beta

def r_squared(y, y_hat):
    ss_res = np.sum((y - y_hat) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    return 1 - ss_res / ss_tot




