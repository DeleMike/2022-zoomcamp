# Session 2

## Notes on Introduction to Linear Regression

Linear Regression can be broken into a simple function

                  g(x) = Wo + W(xi)

Where ```Wo``` = the prediction we make without knowing anything about a data point(a single entity in the dataset). Like a default value for the car used in this module. This is the bias term.

And ```W(xi)``` = weight of each feature of the car

One of the important things in ML is determining the weights of a model. And under the hood, the **Normal Equation** is one of the ways used to generate the weights for each feature.

In ML, it is important to build a baseline model with few features. It will help give a platform to judge if the future iteration of your models are good or not. One way to measure the performance of a Linear Regression model is to use the **RMSE** metric.

**Regularization** is a technique used to reduce our model weights. It helps ensure that if we had a chance of getting a *"Singular Matrix" Error* during training, it would prevent that by adding a little value to the diagonal of our `Feature Matrix` to ensure that it is impossible for us to have duplicate coulmns. Hence this will reduce large weights.

A sign that we need to use regularization is when we are having ***large weights*** while training our model. It is maybe caused by having duplicate features in our feature matrix hence leading the model to create large weights during training.

Knowing what **"little value"** to use is up to the engineer of the model as it will require tuning until you get your desired set of weight/results.

Finally, a basic framework once again to building an ML model:

- get and load dataset
- prepare dataset: clean all the noise and ensure it is good for the model to consume
- perform some exploratory data analysis: get to know your data, continue cleaning and preparing the dataset
- set up the validation framework(train, test, split)
- train a baseline model
- evaluate the model's performance by using the correct metric for measuring performance/quality for the model. (e.g. RMSE for linear regression)
- validate the model by testing using the validation data set and evaluate again
- add more features and build model again
- evaluate the model. We can use baseline model score to judge if it is better or worse.
- perform feature engineering if need be to better the model. Your categorical variables can help you here to decide what to use.
- use regularization if need be to reduce those large weights
- evaluate the final model
- USE the model.
