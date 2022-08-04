# Wine Price Prediction Using Machine Learning

*Problem Statement* - To predict the price of wines on the basis of the given features.

#### The Data :-

![](https://i.imgur.com/Mw7titw.png)

The above data is raw data. It needed to be cleaned i.e. all the _NULL_ and _'N.V.'_ needed to be removed. This was done with the help of `numpy` and `pandas` libraries. This clean data was then exported to a separate file __clean_wine.csv__. This is what the cleaned data now looked like:-

![](https://i.imgur.com/kZAofy3.png)

and ofcourse, it was fully cleaned data with no null values.

![](https://i.imgur.com/Enrk8p4.png)

#### Data Visualization :-

The below heatmap shows the correlation of each of the rows with each other. 

![](https://i.imgur.com/L1W2g6t.png)

The above diagram can be simplified by the `df.corr()['price']` function which essentially gives the correlation of all the features with the target variable.

![](https://i.imgur.com/HKX73ki.png)



#### Feature Engineering

Now, from the above correlation values, only those features were chosen who had a __positive__ correlation with the target variable i.e. _price_.

These variables were:-

* winery

* wine

* rating

* region

* body

But, the major problem was that some of the chosen features had textual data. Hence, they were ran through `sklearn.preprocessing.LabelEncoder` which converted all the textual values to numbers. <sub><sup>Note - We found out later that `sklearn.preprocessing.OrdinalEncoder` is better suited for encoding the textual data to numeric data since the `LabelEncoder` is more suitable for the target variable (as per sklearn documentation)</sup></sub>

The `sklearn.preprocessing.LabelEncoder` was used like this:-

![](https://i.imgur.com/bFrETVt.png)

After encoding, the final data to be used for the model looked something like this:-

![](https://i.imgur.com/ldrV7sr.png)



#### Making The Model

For this regression problem, `sklearn.ensemble.RandomForestRegressor` was used. 

First, the data was divided in training and testing data using `sklearn.model_selection.train_test_split`

Then the model was fitted with the training data and tested on the testing data.

![](https://i.imgur.com/zQFbZ5n.png)





#### Evaluating The Model

For the evaluation of this model, the below metrics were used:-

* R^2 Score

* MAE - Mean Absolute Error

* RMSE - Root Mean Squared Error

The below image denotes the performance of the model:-

![](https://i.imgur.com/1SIObkh.png)

The above figures indicate that:-

1. Since the R^2 score for testing data is higher than training data, the model is overfitted.

2. High values of MAE and RMSE indicate that there are many outliers in the data.



#### Visualizing The Model And Predictions

The below diagrams were made using `YellowBrick` and `Seaborn` libraries.

![](https://i.imgur.com/9TBeGYG.png)

![](https://i.imgur.com/TErJl7g.png)

![](https://i.imgur.com/jXJ97gV.png)





#### Deploying The Model

These were the steps taking to deploy the model and the final csv file and the deployment files can be found in the above uploaded files.

1. The `sklearn.preprocessing.OrdinalEncoder` was exported as a pickle file.

2. The `skelarn.ensemble.RandomForestRegressor` was also exported as a pickle file.

3. A __POST__ endpoint was made with the use of `FastAPI` which accepted the winery, wine, rating, region and body via the `request body`.

4. The text inputs were converted to their corressponding numeric data by the use of the pickle file of `OrdinalEncoder`.

5. The final numeric data was used as an input for the `RandomForestRegressor` model so that it can predict the corresponding price.

6. This numeric value of price was returned as the `HttpResponse`.

7. The whole thing was dockerized and put in a container. The `Dockerfile` and `docker-compose.yml` can also be found in this repo.



The final response from the API looks something like this:-

![](https://i.imgur.com/NZ7Be9X.png)


