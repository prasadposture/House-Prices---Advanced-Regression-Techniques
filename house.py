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
        #fig4 = plt.figure()
        #sns.kdeplot(df[option6])
        #st.pyplot(fig4)
        fig4 = px.histogram(df, x=option6 )
        st.plotly_chart(fig4, use_container_width=True)

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

    
    

with st.container():
    left, middle, right = st.columns(3)
    with left:
        st.markdown("<a href='https://www.linkedin.com/in/prasad-posture-6a3a77215/' target='blank'><img align='center' src='https://img.shields.io/badge/-Prasad Posture-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/prasad-posture-6a3a77215/' alt='Prasad Posture' height='20' width='100' /></a>", unsafe_allow_html=True)
    with middle:
        st.markdown("<a href='https://github.com/prasadposture' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/prasadposture' alt='prasadposture' height='20' width='100' /></a>", unsafe_allow_html=True)
    with right:
        st.markdown("<a href='https://www.kaggle.com/prasadposture121' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture121-blue?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/prasadposture121' alt='prasadposture121' height='20' width='100' /></a>", unsafe_allow_html=True)