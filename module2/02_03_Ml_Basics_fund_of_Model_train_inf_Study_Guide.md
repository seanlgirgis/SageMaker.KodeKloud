Study Guide: Machine Learning Basics and Model Training

Quiz

Answer the following questions in 2-3 sentences each, based on the provided material.

1. What is the purpose of training data in machine learning, and what critical component must it contain?
2. In the context of linear regression, what is a "residual" and why are these values squared during the training process?
3. Describe the primary role of an algorithm, such as XGBoost, during model training.
4. What is the output of a training process called, and what step is necessary before it can be used for inference?
5. Explain the concept of an "inference request" and how the data it contains differs from the training data.
6. In the linear equation f(x) = wx + b, what do the terms 'w' and 'b' represent in machine learning terminology?
7. What is Gradient Descent and what is its function in optimizing a model?
8. Why is it important for a machine learning model to "generalize" from the data?
9. According to the material, what are three common use cases for machine learning in organizations?
10. What are "stopping criteria" and why are they useful in the model training process?


--------------------------------------------------------------------------------


Answer Key

1. Training data is historical data used to teach a machine learning model. It must contain both the input features (e.g., number of bedrooms, square footage) and the target value (e.g., the actual price a house sold for), which is the value the model will ultimately learn to predict.
2. A residual is the measured distance between a known data point in the training set and the model's line of best fit. These values are squared to convert all residuals into positive numbers, preventing negative and positive values from canceling each other out and ensuring the total calculated error (loss) accurately reflects the magnitude of the inaccuracies.
3. An algorithm's role is to ingest the training data and iteratively identify the underlying patterns, correlations, and relationships within it. It uses this process to build a generalized mathematical formula (the model) that can make accurate predictions on new, unseen data.
4. The output of a training process is a file called a model artifact (e.g., model.gz). Before it can be used for inference, this artifact must be hosted on a compute platform, such as a virtual machine or a service like SageMaker, which provides the necessary environment to handle prediction requests.
5. An inference request is the act of providing new data to a trained model to generate a prediction. This data contains the same input features as the training data but crucially excludes the target value, as predicting this value is the model's objective.
6. In the formula f(x) = wx + b, 'w' represents the weight, which is the coefficient that determines the slope of the line. 'b' represents the bias, which is the value where the line intercepts the Y-axis.
7. Gradient Descent is a common optimization method used by algorithms during training. It works by systematically adjusting the model's weights and biases in the direction that most effectively reduces the loss function (e.g., the sum of squared residuals), thereby improving the model's accuracy with each iteration.
8. A model must generalize to be useful because its purpose is to make accurate predictions on brand new data it has never seen before. If it simply memorized the exact values in the training data, it would be unable to derive a reasonable prediction when presented with a new combination of features.
9. The three common use cases mentioned are classifying objects (e.g., fraud detection), forecasting trends (e.g., future sales figures), and identifying relationships in data that may not be obvious to humans.
10. Stopping criteria are rules that determine when the iterative training process should end. They are useful because they can stop the training once the model's accuracy is no longer improving significantly, which saves computational resources and time by preventing unnecessary iterations.


--------------------------------------------------------------------------------


Essay Questions

Construct detailed responses to the following prompts, synthesizing concepts from across the lesson.

1. Describe the complete machine learning workflow as outlined in the source material, starting from the initial data and ending with a final prediction. Detail each major stage (Training Data, Algorithm, Training Process, Trained Model, Prediction Platform) and its specific function.
2. Explain the mathematical foundation of linear regression. Discuss the "line of best fit," its corresponding algebraic formula (f(x) = wx + b), and the process of quantifying and minimizing error using the "sum of squared residuals."
3. Discuss the iterative nature of the model training process. How do the concepts of Gradient Descent, Learning Rate, and Stopping Criteria work together to optimize a model and find the most accurate "line of best fit"?
4. Using the provided examples of used car sales (single input feature) and London house prices (multiple input features), compare and contrast the complexity of training a model in these two scenarios. How does the concept of a "line of best fit" extend into a multi-dimensional space?
5. Elaborate on the statement that a trained model is ultimately a "long and complex formula." Explain how input features, weights, and biases are combined within this formula during an inference request to derive a final prediction value.


--------------------------------------------------------------------------------


Glossary

Term	Definition
Algorithm	A pre-developed mathematical procedure (e.g., XGBoost, Linear Learner) selected by a data scientist that ingests training data to identify patterns and build a model.
Bias (b)	In the linear equation f(x) = wx + b, this is the value representing the y-intercept; the point at which the line intersects the vertical axis.
Gradient Descent	An optimization technique used during training to iteratively adjust the model's parameters (weights and biases) to minimize the loss function and improve accuracy.
Inference	The process of using a trained model to generate a prediction on new, unseen data.
Inference Request	The submission of input data (without a target value) to a hosted model to receive a prediction.
Input Features	The independent variables in a dataset used to make a prediction (e.g., number of bedrooms, square footage, age of a car).
Learning Rate	A parameter that controls the size of the adjustment steps taken by the algorithm (like Gradient Descent) when updating the model's weights and biases during each iteration of training.
Linear Regression	A type of machine learning used to predict a continuous target value by calculating a "line of best fit" that describes the relationship between input features and the target.
Logistic Regression	A type of machine learning mentioned as a common use case for tabular data, distinct from linear regression.
Loss	A quantifiable measure of a model's error or how inaccurate its predictions are compared to the actual values. In linear regression, this is often calculated as the sum of squared residuals.
Model Artifact	The file (e.g., model.gz) that is the output of the training process. This file contains the learned mathematical formula and must be hosted to perform inference.
Prediction	The output generated by a model when it is given an inference request; the model's calculated estimate for the target value.
Residuals	The difference between the actual value of a data point and the value predicted by the model's line of best fit. It is a measure of error for a single data point.
Stopping Criteria	Pre-defined conditions that tell the training process when to stop, such as when accuracy is sufficient or a maximum number of iterations has been reached.
Sum of Squared Residuals	A method for calculating the total loss of a linear regression model. It involves squaring each residual (to make all values positive) and then adding them all together; the goal of training is to minimize this sum.
Target Value	The dependent variable in a dataset that the model is being trained to predict (e.g., the sale price of a house).
Training Data	The initial dataset used to train a model, which must include both the input features and the known historical target values.
Training Process	The iterative process where an algorithm analyzes the training data to learn patterns and relationships, adjusting its internal parameters to minimize loss and create an accurate model.
Weight (w)	In the linear equation f(x) = wx + b, this is the coefficient for an input feature that determines the slope of the line and represents the feature's influence on the prediction.
