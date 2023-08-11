# Regularisation & Hyperparameters

**Regularisation** is a technique used to prevent **overfitting** in machine learning models. Overfitting occurs when a model learns to fit the training data too closely, resulting in poor generalization to new, unseen data. Regularisation mitigates overfitting by adding a penalty term to the loss function, discouraging the model from assigning too much importance to any particular feature or creating complex and overly flexible models.

The **two** commonly used regularization techniques are:

1. **L1 Regularization (Lasso)**: This technique adds the sum of the absolute values of the model's coefficients as a penalty term. It encourages sparse solutions, where some coefficients become exactly zero, effectively performing feature selection.&#x20;
2. **L2 Regularization (Ridge)**: L2 regularization adds the sum of the squared values of the model's coefficients as a penalty term. It encourages small and distributed weights across all the features, avoiding excessive emphasis on specific elements

**Hyperparameters** are parameters not learned from the data but set before training the model to impose constraints on its behaviour. They control the behaviour and performance of a machine learning algorithm. Unlike the model's parameters, which are learned from the data during training (e.g., weights in neural networks), hyperparameters are determined by the practitioner or through hyperparameter tuning.
