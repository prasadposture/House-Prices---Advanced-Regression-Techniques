import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import joblib as jb

st.set_page_config(page_title="House Price Prediction", layout="wide",page_icon="📊")
df=pd.read_csv('train.csv')
st.markdown('<h3 style = "background-color: #00BFFF; color :white; text-shadow: 2px 2px 5px black;", align="center">Data Visualization</h3>',unsafe_allow_html=True)
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
    
    try:
        xdf=df.groupby(option7, as_index=False, dropna=False)['Id'].count()
        xdf.fillna('NA', inplace=True)
        xdf.rename(columns={'Id':'Number of Houses'}, inplace=True)
        fig5 = px.sunburst(xdf,path=option7, values='Number of Houses', color='Number of Houses')
        st.plotly_chart(fig5, use_container_width=True)
    except Exception as e:
        pass
with d:
    option8 = st.multiselect('Correlation of (Columns)',['SalePrice', 'MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual',
                                               'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1',
                                               'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
                                               'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
                                               'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea',
                                               'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch','3SsnPorch', 'ScreenPorch', 'PoolArea',
                                               'MiscVal','MoSold','YrSold'], default=['SalePrice','OverallQual','OverallCond', 'YearBuilt'],max_selections=10)
    option9 = st.multiselect('Correlation with (Rows)',['SalePrice', 'MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual',
                                               'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1',
                                               'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
                                               'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
                                               'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea',
                                               'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch','3SsnPorch', 'ScreenPorch', 'PoolArea',
                                               'MiscVal','MoSold','YrSold'], default=['SalePrice','OverallQual','OverallCond', 'YearBuilt'],max_selections=10)
    fig6 = plt.figure()
    sns.heatmap(df.corr()[option8].loc[option9], annot=True)
    st.pyplot(fig6)