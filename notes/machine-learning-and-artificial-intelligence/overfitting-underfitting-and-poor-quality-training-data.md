# Overfitting, Underfitting & Poor Quality Training Data

### Pitfalls of Machine Learning

Machine-learning methods models which perform well on training data but do not generalize well to unseen data are experiencing a phenomenon called **overfitting**.

Even complex deep neural networks can fall into a trap where, while they can detect intricate patterns in data when the data set is too noisy or small, they can start to recognize that noise as trends in the data. This results in the model being unable to generalize.

To mitigate overfitting in our models, we can:

1. Simplify the model, and select fewer input features.
2. Gather more training data.
3. Reduce noise in the training data.

Constraining a model to make it simple and reduce the risk of overfitting is called **regularisation**.

**Underfitting** occurs when the model is too simple to understand underlying patterns in the data. Underfit models will not perform well when generalized and on the training set.

To mitigate underfitting in our models, we can:

1. Select a more complex learning algorithm with more parameters.
2. Feed better features through **feature engineering**
3. Reduce constraints on the model

**Poor quality data** will likely produce poor performing models.
