# Session 1

## Notes on Introduction to ML, Numpy and Pandas

- ML can be divided largerly into Supervised and Unsupervised Machine Learning.

- Not all problems must be solved with ML. Ask yourself, do research on how it can be solved and then you will know if you need to use ML.

- ML has **6 flows** using the CRISP DM:
  - Business Understanding: What does your business what to achieve? Do we need ML?

  - Data Understanding: is data available? How do we get data for the project? is it good data? is it large enough?

  - Data Preparation: Extracting features from the data that will be useful for building the model

  - Modeling: This is where we train the model. We can build different models and evaluate them before we decide which one is the best.

  - Evaluation: This is asking ourselves if the model we have built is good enough. In this phase, we can go back to the Business Understanding to confirm if our project is still worthwhile.

  - Deployment: Your model has to be deployed so that it can be used. This is one of the essence of ML - to be shared and used so as to enable/improve lives. This phase comes together with Evaluation. "Real Evaluation" is done when it is deployed.

  - Iterate: We don't stop at deployment. We see that deployement can be used to evaluate our model which will take us back to the Business Understanding Phase which will cause the other steps to follow. This step can ask questions like if we need to improve our model? Do we need more data and so on.

- When builidng ML models, start with a simple model before you move on to building other types of models.

- Data spliting is a good step to creating / selecting a good model.

There are many libraries really helpful when building ML models but numpy and pandas are really helpful when trying to understand your data and prepare too

```python
   import numpy as np
   import pandas as pd
   print(np.__version_)
   # Output: '1.21.2'

   # read a csv file
   df = pd.read_csv('cars_data.csv')
   print(df.shape)
   # Output: (11914, 16)
```

[#mlzoomcamp](https://twitter.com/search?q=%23mlzoomcamp&src=typeahead_click) with [Alexey Grigorev](@https://twitter.com/Al_Grigor)
