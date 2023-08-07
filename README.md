<h1 align="center"> House Prices : Advanced Regression Techniques </h1>

### Introduction
Predicting the sales price of a house is an essential topic in real estate. There are various factors that affect the price of a home. Some of the factors may cause an increment in the price, some of them may cause decrement, while others are dependent on one or more factors i.e. their combination with other factors decides whether they will increase or decrease the price. To help us find the relationship between these attributes and the sale prices, here we have data on 1460 houses (sold). The dataset includes nearly all the factors that affect the sales price of a house such as overall condition, neighborhood, presence of basement and garage, etc. along with the sale price. I created this project for the Kaggle competition, It has 2000+ viewers so far and it was featured on Kaggle. It includes exploratory data analysis and predictive modeling. If you find this useful please give it a star. Thank You!

### Important Links
[EDA & MLA](https://www.kaggle.com/code/prasadposture121/house-prices-prediction)
<br>[Web Application](https://house-price-prediction-pp.streamlit.app/)

### Workflow
1. Loading, Exploring, and Visualizing the Data using Pandas, NumPy, Matplotlib, Seaborn and Plotly.
2. Preparing the dataset for training, which includes,<br>
    a. Identifying input & target columns and numeric & categorical columns.<br>
    b. Imputing missing values in numeric columns.<br>
    c. Scaling numeric columns in the range of [0,1].<br>
    d. Encoding the categorical columns.<br>
    e. Splitting the dataset in training and validation datasets.
 3. K-Fold Cross Validation for checking the base accuracy of different models.
 4. Training, Evaluating and Tuning the best model(s) (one(s) with least RMSE).
 5. Taking a weighted average of the best-performing model to make predictions on the validation data so that it gives least RMSE.
 6. Making predictions on test data and submitting them for competition.
 7. Saving the model(s) and objects for future use.
 8. Concluding the project in the notebook with a summary and references.
 9. Creating a Streamlit web application that takes user inputs to predict the prices along with interactive visuals that help the user to understand the relationship between different attributes of a house and its sale price.
 10. Deploying the web application on `share.streamlit.io` for making it available for everyone.
