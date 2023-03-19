import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import joblib as jb

st.set_page_config(page_title="House Prices Prediction", layout="wide")
df=pd.read_csv('train.csv')
st.markdown('<h1 style = "background-color: #00BFFF; color :white; text-shadow: 2px 2px 5px black;", align="center">House Prices Prediction</h1>',unsafe_allow_html=True)
a,b = st.columns(2)

with a:
    tab1, tab2 = st.tabs(["Box Plot","Bar Plot"])
    with tab1:
        option1=st.selectbox('Select Categorical / Discrete Feature',('OverallQual','OverallCond','Neighborhood','MSSubClass','BsmtFullBath',
                                                                      'BsmtHalfBath', 'FullSBath', 'HalfBath','BedroomAbvGr', 'KitchenAbvGr',
                                                                      'TotRmsAbvGrd', 'Fireplaces','GarageCars', 'MoSold','YrSold',
                                                                      'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
                                                                      'LotConfig', 'LandSlope', 'Condition1', 'Condition2','HouseStyle', 'RoofStyle',
                                                                      'RoofMatl', 'Exterior1st', 'Exterior2nd','BldgType','MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
                                                                      'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical',
                                                                      'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive',
                                                                      'PoolQC', 'Fence', 'MiscFeature', 'SaleType', 'SaleCondition'))
    
        option2=st.selectbox('Select Numeric Feature',('SalePrice','LotFrontage','LotArea','YearBuilt',
                                                       'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
                                                       'LowQualFinSF', 'GrLivArea',   'GarageYrBlt', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch','3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal'))
        fig=px.box(df, x=option1, y=option2, color=option1)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        option3=st.selectbox('Select Feature',('Neighborhood','MSSubClass','BsmtFullBath', 'OverallCond','OverallQual',
                                               'BsmtHalfBath', 'FullBath', 'HalfBath','BedroomAbvGr', 'KitchenAbvGr',
                                                'TotRmsAbvGrd', 'Fireplaces','GarageCars', 'MoSold','YrSold',
                                                'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
                                                'LotConfig', 'LandSlope', 'Condition1', 'Condition2','HouseStyle', 'RoofStyle',
                                                'RoofMatl', 'Exterior1st', 'Exterior2nd','BldgType','MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
                                                'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical',
                                                'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive',
                                                'PoolQC', 'Fence', 'MiscFeature', 'SaleType', 'SaleCondition'))
        
        fig2 = px.histogram(df,x=option3, color=option3)
        st.plotly_chart(fig2, use_container_width=True)

with b:
    tab3, tab4 = st.tabs(["Scatter Plot", "Distribution Plot"])
    with tab3:
        option4 = st.selectbox('Select Numeric Feature 1',
                               ('LotFrontage','LotArea','YearBuilt',
                                'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
                                'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF','SalePrice',
                                'LowQualFinSF', 'GrLivArea',  'GarageYrBlt', 'GarageArea',
                                'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch','3SsnPorch',
                                'ScreenPorch', 'PoolArea', 'MiscVal','MSSubClass','BsmtFullBath', 'BsmtHalfBath', 'FullBath',
                                'HalfBath','BedroomAbvGr', 'KitchenAbvGr','TotRmsAbvGrd', 'Fireplaces','GarageCars', 'MoSold','YrSold'))
        
        option5 = st.selectbox('Select Numeric Feature 2',
                               ('SalePrice','LotFrontage','LotArea','YearBuilt',
                                'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
                                'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
                                'LowQualFinSF', 'GrLivArea',  'GarageYrBlt', 'GarageArea',
                                'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch','3SsnPorch',
                                'ScreenPorch', 'PoolArea', 'MiscVal','MSSubClass','BsmtFullBath', 'BsmtHalfBath', 'FullBath',
                                'HalfBath','BedroomAbvGr', 'KitchenAbvGr','TotRmsAbvGrd', 'Fireplaces','GarageCars', 'MoSold','YrSold'))
        fig3 = px.scatter(df, x=option4, y=option5, color=option5 )
        st.plotly_chart(fig3, use_container_width=True)

    with tab4:
        option6 = st.selectbox('Select Feature for Distribution',('SalePrice','LotFrontage','LotArea','YearBuilt',
                                                                  'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1',
                                                                  'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
                                                                  '1stFlrSF', '2ndFlrSF','LowQualFinSF', 'GrLivArea',
                                                                  'GarageYrBlt', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
                                                                  'EnclosedPorch','3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal'))
        fig4 = plt.figure()
        sns.kdeplot(df[option6])
        st.pyplot(fig4)

st.write("___")
c,d = st.columns(2)

with c:
    option7=st.multiselect('Number of Houses Grouped With',['Neighborhood','MSSubClass','BsmtFullBath', 'OverallCond','OverallQual',
                                 'BsmtHalfBath', 'FullBath', 'HalfBath','BedroomAbvGr', 'KitchenAbvGr',
                                 'TotRmsAbvGrd', 'Fireplaces','GarageCars', 'MoSold','YrSold',
                                 'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
                                 'LotConfig', 'LandSlope', 'Condition1', 'Condition2','HouseStyle', 'RoofStyle',
                                 'RoofMatl', 'Exterior1st', 'Exterior2nd','BldgType','MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
                                 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical',
                                 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive',
                                 'PoolQC', 'Fence', 'MiscFeature', 'SaleType', 'SaleCondition'], default=['Street','Alley','MSZoning','Neighborhood'],max_selections=5)
    xdf=df.groupby(option7, as_index=False, dropna=False)['Id'].count()
    xdf.fillna('NA', inplace=True)
    xdf.rename(columns={'Id':'Number of Houses'}, inplace=True)
    fig5 = px.sunburst(xdf,path=option7, values='Number of Houses', color='Number of Houses')
    st.plotly_chart(fig5, use_container_width=True)

HPP=jb.load('house_price_predictor.joblib')
model1 = HPP['model1']
model2 = HPP['model2']
imputer = HPP['imputer']
scaler = HPP['scaler']
encoder = HPP['encoder']
input_cols = HPP['input_cols']
target_col = HPP['target_col']
numeric_cols = HPP['numeric_cols']
categorical_cols = HPP['categorical_cols']
encoded_cols = HPP['encoded_cols']
log_numeric_cols = HPP['log_numeric_cols']

with d:
    st.write("Predicions")
    tab5, tab6 = st.tabs(["Categorical Input","Numerical Input"])
    with tab5:
        categorical_input = { 'MSZoning': 'RL', 'Street': 'Pave', 'Alley': None, 'LotShape': 'IR1', 'LandContour': 'Lvl', 'Utilities': 'AllPub',
                             'LotConfig': 'Inside', 'LandSlope': 'Gtl', 'Neighborhood': 'NAmes', 'Condition1': 'Norm', 'Condition2': 'Norm',
                             'BldgType': '1Fam', 'HouseStyle': '1Story', 'RoofStyle': 'Gable', 'RoofMatl': 'CompShg', 'Exterior1st': 'Plywood',
                             'Exterior2nd': 'Plywood', 'MasVnrType': 'None','ExterQual': 'TA','ExterCond': 'TA',
                             'Foundation': 'CBlock','BsmtQual': 'TA','BsmtCond': 'TA','BsmtExposure': 'No','BsmtFinType1': 'ALQ',
                             'Heating': 'GasA','HeatingQC': 'Fa','CentralAir': 'Y','Electrical': 'SBrkr', 'KitchenQual': 'TA','Functional': 'Typ',
                             'FireplaceQu': np.nan,'GarageType': np.nan,'GarageYrBlt': np.nan,'GarageFinish': np.nan,
                             'GarageQual': np.nan,'GarageCond': np.nan,'PavedDrive': 'Y',  'PoolQC': np.nan, 'Fence': np.nan, 'MiscFeature': 'Shed',
                             'SaleType': 'WD', 'SaleCondition': 'Normal'}
        categorical_input_df = pd.DataFrame([categorical_input])
        st.write(categorical_input_df)

    with tab6:
        numerical_input={ 'MSSubClass': 20,'LotFrontage': 77.0, 'LotArea': 9320,
                          'OverallQual': 4, 'OverallCond': 5, 'YearBuilt': 1959,
                          'YearRemodAdd': 1959,'MasVnrArea': 0.0,'MiscVal': 400, 'MoSold': 1, 'YrSold': 2010,
                          'BsmtFinSF1': 569,'BsmtFinType2': 'Unf','BsmtFinSF2': 0,'BsmtUnfSF': 381,
                          'TotalBsmtSF': 950,'1stFlrSF': 1225, '2ndFlrSF': 0, 'LowQualFinSF': 0, 'GrLivArea': 1225,
                          'BsmtFullBath': 1, 'BsmtHalfBath': 0, 'FullBath': 1, 'HalfBath': 1, 'BedroomAbvGr': 3, 'KitchenAbvGr': 1,
                          'Fireplaces': 0,'TotRmsAbvGrd': 6,'GarageCars': 0,'GarageArea': 0,'WoodDeckSF': 352, 'OpenPorchSF': 0,
                          'EnclosedPorch': 0,'3SsnPorch': 0, 'ScreenPorch': 0, 'PoolArea': 0,
                          }
        numerical_input_df=pd.DataFrame([numerical_input])
        st.write(numerical_input_df)
    
    new_df = pd.concat([categorical_input_df, numerical_input_df], axis=1)
    st.image('OIP.jfif')

    
    
    st.write("#### Predicted Sale Price : $ 120774")

with st.container():
    left, middle, right = st.columns(3)
    with left:
        st.markdown("<a href='https://www.linkedin.com/in/prasad-posture-6a3a77215/' target='blank'><img align='center' src='https://img.shields.io/badge/-Prasad Posture-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/prasad-posture-6a3a77215/' alt='Prasad Posture' height='20' width='100' /></a>", unsafe_allow_html=True)
    with middle:
        st.markdown("<a href='https://github.com/prasadposture' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/prasadposture' alt='prasadposture' height='20' width='100' /></a>", unsafe_allow_html=True)
    with right:
        st.markdown("<a href='https://www.kaggle.com/prasadposture121' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture121-blue?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/prasadposture121' alt='prasadposture121' height='20' width='100' /></a>", unsafe_allow_html=True)