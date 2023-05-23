import joblib as jb
import streamlit as st
from pandas import read_csv
import numpy as np

st.set_page_config(page_title="House Price Prediction", layout="wide", page_icon="🧐")
st.markdown('<h3 style = "background-color: #00BFFF; color :white; text-shadow: 2px 2px 5px black;", align="center">Predictions</h3>',unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
hpp = jb.load('house_price_predictor.joblib')
model1=hpp['model1'] #Ridge
model2=hpp['model2'] #Gradient Boosting
imputer=hpp['imputer']
scaler=hpp['scaler']
encoder=hpp['encoder']
input_cols=hpp['input_cols']
target_col=hpp['target_col']
numeric_cols = hpp['numeric_cols']
categorical_cols=hpp['categorical_cols']
encoded_cols=hpp['encoded_cols']
log_numeric_cols=hpp['log_numeric_cols']

#If button : Mention these groups in the about sectino
#so that we can use a button to to show these inputs and the app wont be crowdy
#cooooooolllllllll

# Locations Specifications
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Location Specifics", "Lot/Land Specifics", "Timeline", "Quality/Condition",
                                                    "House Specifics (Internal)","House Speicifics (External)", "Thermoregulation"])
with tab1:
    a,b,c = st.columns(3)
    with a:
        MSZoning = st.selectbox('MSZoning', ('RH', 'RL', 'RM', 'FV', 'C (all)',np.nan))
        Street = st.selectbox('Street', ('Pave', 'Grvl'))
    with b:    
        Alley = st.selectbox('Alley',(np.nan, 'Pave', 'Grvl'))
        Neighborhood = st.selectbox('Neighborhood', ('NAmes','Gilbert','StoneBr','BrDale','NPkVill','NridgHt','Blmngtn','NoRidge','Somerst','SawyerW','Sawyer','NWAmes','OldTown','BrkSide','ClearCr','SWISU','Edwards','CollgCr','Crawfor','Blueste','IDOTRR','Mitchel','Timber','MeadowV','Veenker'))
    with c:
        MSSubClass = st.slider('MSSubClass', min_value=20, max_value=190, value=50, step=10)
with tab2:
    a,b,c = st.columns(3)
    with a:    
        LotShape = st.selectbox('LotShape', ('Reg', 'IR1', 'IR2', 'IR3'))
        LandContour = st.selectbox('LandContour', ('Lvl', 'HLS', 'Bnk', 'Low'))
    with b:
        LotConfig = st.selectbox('LotConfig', ('Inside', 'Corner', 'FR2', 'CulDSac', 'FR3'))
        LandSlope = st.selectbox('LandSlope', ('Gtl', 'Mod', 'Sev'))
    with c:
        LotFrontage = st.slider('LotFrontage', min_value=21, max_value=313, value=69, step=1)
        LotArea = st.slider('LotArea', min_value=1300, max_value=215245, value=9478, step=1)
with tab3:
    a,b,c,d = st.columns(4)
    with a:
        YearBuilt = st.slider('YearBuilt', min_value=1872, max_value=2010, value=1973, step=1) 
    with b:
        YearRemodAdd = st.slider('YearRemodAdd', min_value=1950, max_value=2010, value=1994, step=1)
    with c:
        MoSold = st.slider( 'MoSold' ,min_value= 1 , max_value= 12 , value= 6 , step=1)
    with d:
        YrSold = st.slider( 'YrSold' ,min_value= 2006 , max_value= 2010 , value= 2008 , step=1)
with tab4:
    a,b,c = st.columns(3)
    with a:
        OverallQual = st.slider('OverallQual', min_value=1, max_value=10, value=6, step=1)
        OverallCond = st.slider('OverallCond', min_value=1, max_value=10, value=5, step=1)
    with b:
        Condition1 = st.selectbox('Condition1',('Feedr','Norm','PosN','RRNe','Artery','RRNn','PosA','RRAn','RRAe'))
        Condition2 = st.selectbox('Condition2', ('Norm', 'Feedr', 'PosA', 'PosN', 'Artery'))
    with c:
        SaleCondition = st.selectbox('SaleCondition', ('Normal','Partial','Abnorml','Family','Alloca','AdjLand'))
with tab5:
    a,b,c = st.columns(3)
    with a:
        FullBath = st.slider( 'FullBath' ,min_value= 0 , max_value= 3 , value= 2 , step=1)
        HalfBath = st.slider( 'HalfBath' ,min_value= 0 , max_value= 2 , value= 0 , step=1)
    with b:
        BedroomAbvGr = st.slider( 'BedroomAbvGr' ,min_value= 0 , max_value= 8 , value= 3 , step=1)
        KitchenAbvGr = st.slider( 'KitchenAbvGr' ,min_value= 0 , max_value= 3 , value= 1 , step=1)
    with c:
        TotRmsAbvGrd = st.slider( 'TotRmsAbvGrd' ,min_value= 2 , max_value= 14 , value= 6 , step=1) 
        KitchenQual = st.selectbox('KitchenQual', ('TA', 'Gd', 'Ex', 'Fa', np.nan))
with tab6:
    a,b,c = st.columns(3)
    with a:
        BldgType = st.selectbox('BldgType', ('1Fam', 'TwnhsE', 'Twnhs', 'Duplex', '2fmCon'))
        HouseStyle = st.selectbox('HouseStyle',('1Story','2Story','SLvl','1.5Fin','SFoyer','2.5Unf','1.5Unf'))
    with b:
        RoofStyle = st.selectbox('RoofStyle',('Gable', 'Hip', 'Gambrel', 'Flat', 'Mansard', 'Shed'))
        RoofMatl = st.selectbox('RoofMatl',('CompShg', 'Tar&Grv', 'WdShake', 'WdShngl'))
    with c:
        Foundation = st.selectbox('Foundation',('CBlock', 'PConc', 'BrkTil', 'Stone', 'Slab', 'Wood'))
with tab7:
    a,b,c = st.columns(3)
    with a:
        CentralAir = st.selectbox('CentralAir',('Y', 'N')) 
        Heating = st.selectbox('Heating', ('GasA', 'GasW', 'Grav', 'Wall'))
    with b:
        FireplaceQu =  st.selectbox('FireplaceQu',(np.nan, 'TA', 'Gd', 'Po', 'Fa', 'Ex'))
        HeatingQC = st.selectbox('HeatingQC', ('TA', 'Gd', 'Ex', 'Fa', 'Po'))
    with c:
        Fireplaces = st.slider( 'Fireplaces' ,min_value= 0 , max_value= 3 , value= 1 , step=1)


tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17 = st.tabs(["Exterior", "Basement", "Garage", "Porch", "Pool", "Internal Area",
                                                                  "Surroundings","Masnory","Miscellaneous", "Others"])

with tab9:
    a,b,c = st.columns(3)
    with a:
        BsmtQual = st.selectbox('BsmtQual',('TA', 'Gd', 'Ex', 'Fa', np.nan))
        BsmtCond =  st.selectbox('BsmtCond',('TA', 'Po', 'Fa', 'Gd', np.nan))
        BsmtExposure = st.selectbox('BsmtExposure',('No', 'Gd', 'Mn', 'Av', np.nan))
        BsmtFinType1 = st.selectbox('BsmtFinType1',('Rec', 'ALQ', 'GLQ', 'Unf', 'BLQ', 'LwQ', np.nan))
    with b:
        BsmtFinSF1 = st.slider('BsmtFinSF1', min_value=0, max_value=5644, value=383, step=1)
        BsmtFinSF2 = st.slider('BsmtFinSF2', min_value=0, max_value=1474, value=0, step=1)
        BsmtUnfSF = st.slider('BsmtUnfSF', min_value=0, max_value=2336, value=477, step=1)
        BsmtFinType2 = st.selectbox('BsmtFinType2',('LwQ', 'Unf', 'Rec', 'BLQ', 'GLQ', 'ALQ', np.nan))
    with c:
        TotalBsmtSF = st.slider('TotalBsmtSF', min_value=0, max_value=6110, value=991, step=1)
        BsmtFullBath = st.slider( 'BsmtFullBath' ,min_value= 0 , max_value= 3 , value= 0 , step=1)   
        BsmtHalfBath = st.slider( 'BsmtHalfBath' ,min_value= 0 , max_value= 2 , value= 0 , step=1)
with tab10:
    a,b,c = st.columns(3)
    with a:
        GarageType = st.selectbox('GarageType', ('Attchd','Detchd','BuiltIn',np.nan,'Basment','2Types','CarPort'))
        GarageFinish = st.selectbox('GarageFinish', ('Unf', 'Fin', 'RFn', np.nan))
        GarageQual = st.selectbox('GarageQual', ('TA', np.nan, 'Fa', 'Gd', 'Po'))
    with b:
        GarageCond = st.selectbox('GarageCond', ('TA', np.nan, 'Fa', 'Gd', 'Po', 'Ex'))
        GarageYrBlt = st.slider( 'GarageYrBlt' ,min_value= 1900 , max_value= 2010 , value= 1980 , step=1)
    with c:
        GarageCars = st.slider( 'GarageCars' ,min_value= 0 , max_value= 4 , value= 2 , step=1)
        GarageArea = st.slider( 'GarageArea' ,min_value= 0 , max_value= 1418 , value= 480 , step=1)
with tab8:
    a,b,c,d = st.columns(4)
    with a:
        ExterQual = st.selectbox('ExterQual', ('TA', 'Gd', 'Ex', 'Fa'))
    with b:
        ExterCond = st.selectbox('ExterCond',('TA', 'Gd', 'Fa', 'Po', 'Ex'))
    with c:
        Exterior1st = st.selectbox('Exterior1st',('VinylSd','Wd Sdng','HdBoard','Plywood','MetalSd','CemntBd','WdShing','BrkFace','AsbShng','BrkComm','Stucco','AsphShn','CBlock',np.nan))
    with d:
        Exterior2nd = st.selectbox('Exterior2nd',('VinylSd','Wd Sdng','HdBoard','Plywood','MetalSd','Brk Cmn','CmentBd','ImStucc','Wd Shng', 'AsbShng','Stucco','CBlock','BrkFace','AsphShn','Stone', np.nan))
 

with tab11:
    a,b,c,d = st.columns(4)
    with a:
        OpenPorchSF = st.slider( 'OpenPorchSF' ,min_value= 0 , max_value= 547 , value= 25 , step=1)
    with b:
        EnclosedPorch = st.slider( 'EnclosedPorch' ,min_value= 0 , max_value= 552 , value= 0 , step=1)  
    with c:
        SsnPorch = st.slider( '3SsnPorch' ,min_value= 0 , max_value= 508 , value= 0 , step=1)
    with d:
        ScreenPorch = st.slider( 'ScreenPorch' ,min_value= 0 , max_value= 480 , value=0 , step=1)


with tab12:
    a,b = st.columns(2)
    with a:
        PoolQC = st.selectbox('PoolQC', (np.nan, 'Ex', 'Gd'))
    with b:
        PoolArea = st.slider('PoolArea' ,min_value= 0 , max_value= 738 , value=0 , step=1)

with tab13:
    a,b,c,d = st.columns(4)
    with a:
        stFlrSF = st.slider('1stFlrSF', min_value=334, max_value=4692, value=1087, step=1)
    with b:
        ndFlrSF = st.slider('2ndFlrSF', min_value=0, max_value=2065, value=0, step=1)
    with c:
        LowQualFinSF = st.slider('LowQualFinSF', min_value=0, max_value=572, value=0, step=1)
    with d:
        GrLivArea = st.slider('GrLivArea', min_value=334, max_value=5642, value=1464, step=1)

with tab14:
    a,b,c = st.columns(3)
    with a:
        PavedDrive = st.selectbox('PavedDrive', ('Y', 'N', 'P'))
    with b:
        Fence = st.selectbox('Fence', ('MnPrv', np.nan, 'GdPrv', 'GdWo', 'MnWw'))
    with c:
        WoodDeckSF = st.slider( 'WoodDeckSF' ,min_value= 0 , max_value= 857 , value= 0 , step=1)

with tab15:
    a,b = st.columns(2)
    with a:
        MasVnrType = st.selectbox('MasVnrType',('None', 'BrkFace', 'Stone', 'BrkCmn', np.nan))
    with b:
        MasVnrArea = st.slider('MasVnrArea', min_value=0, max_value=1600, value=0, step=1)

with tab16:
    a,b = st.columns(2)
    with a:
        MiscFeature = st.selectbox('MiscFeature', (np.nan, 'Gar2', 'Shed', 'Othr'))
    with b:
        MiscVal = st.slider( 'MiscVal' ,min_value= 0 , max_value= 15500 , value=0 , step=1)

with tab17:
    a,b,c,d = st.columns(4)
    with a:
        Utilities = st.selectbox('Utilities', ('AllPub', np.nan))
    with b:
        Electrical = st.selectbox('Electrical',('SBrkr', 'FuseA', 'FuseF', 'FuseP'))
    with c:
        Functional = st.selectbox('Functional', ('Typ', 'Min2', 'Min1', 'Mod', 'Maj1', 'Sev', 'Maj2', np.nan))    
    with d:
        SaleType = st.selectbox('SaleType', ('WD','COD','New','ConLD','Oth','Con','ConLw','ConLI','CWD',np.nan))

sample_input = { 'MSSubClass':MSSubClass, 'MSZoning': MSZoning, 'LotFrontage':LotFrontage, 'LotArea': LotArea,
 'Street': Street, 'Alley': Alley, 'LotShape': LotShape, 'LandContour': LandContour, 'Utilities': Utilities,
 'LotConfig': LotConfig, 'LandSlope': LandSlope, 'Neighborhood': Neighborhood, 'Condition1': Condition1, 'Condition2': Condition2,
 'BldgType': BldgType, 'HouseStyle': HouseStyle, 'OverallQual': OverallQual, 'OverallCond': OverallCond, 'YearBuilt': YearBuilt,
 'YearRemodAdd': YearRemodAdd, 'RoofStyle': RoofStyle, 'RoofMatl': RoofMatl, 'Exterior1st': Exterior1st,
 'Exterior2nd': Exterior2nd, 'MasVnrType': MasVnrType,'MasVnrArea': MasVnrArea,'ExterQual': ExterQual,'ExterCond': ExterCond,
 'Foundation': Foundation,'BsmtQual': BsmtQual,'BsmtCond': BsmtCond,'BsmtExposure': BsmtExposure,'BsmtFinType1': BsmtFinType1,
 'BsmtFinSF1': BsmtFinSF1,'BsmtFinType2': BsmtFinType2,'BsmtFinSF2': BsmtFinSF2,'BsmtUnfSF': BsmtUnfSF,
 'TotalBsmtSF': TotalBsmtSF,'Heating': Heating,'HeatingQC': HeatingQC,'CentralAir': CentralAir,'Electrical': Electrical, '1stFlrSF': stFlrSF,
 '2ndFlrSF': ndFlrSF, 'LowQualFinSF': LowQualFinSF, 'GrLivArea': GrLivArea, 'BsmtFullBath': BsmtFullBath, 'BsmtHalfBath': BsmtHalfBath, 'FullBath': FullBath,
 'HalfBath': HalfBath, 'BedroomAbvGr': BedroomAbvGr, 'KitchenAbvGr': KitchenAbvGr,'KitchenQual': KitchenQual,'TotRmsAbvGrd': TotRmsAbvGrd,'Functional': Functional,
 'Fireplaces': Fireplaces,'FireplaceQu': FireplaceQu,'GarageType': GarageType,'GarageYrBlt': GarageYrBlt,'GarageFinish': GarageFinish,'GarageCars': GarageCars,
 'GarageArea': GarageArea,'GarageQual': GarageQual,'GarageCond': GarageCond,'PavedDrive': PavedDrive, 'WoodDeckSF': WoodDeckSF, 'OpenPorchSF': OpenPorchSF,
 'EnclosedPorch': 0,'3SsnPorch': 0, 'ScreenPorch': 0, 'PoolArea': 0, 'PoolQC': np.nan, 'Fence': np.nan, 'MiscFeature': MiscFeature,
 'MiscVal': MiscVal, 'MoSold': MoSold, 'YrSold': YrSold, 'SaleType': SaleType, 'SaleCondition': SaleCondition}

from pandas import DataFrame
input_df = DataFrame([sample_input])
if st.button("Show Inputs"):
    st.write(input_df)
else:
    pass
#this function does all the needful and makes the predictions on the inputs
def predict_input(input_df):
    input_df[log_numeric_cols]=np.log(input_df[log_numeric_cols]+1)
    input_df[numeric_cols] = imputer.transform(input_df[numeric_cols])
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])
    input_df[encoded_cols] = encoder.transform(input_df[categorical_cols].values)
    X_input = input_df[numeric_cols + encoded_cols]
    prediction = 0.45*model1.predict(X_input) + 0.55*model2.predict(X_input)
    return np.exp(prediction)

samp=predict_input(input_df)[0]
st.write("#### 🏡 The Predicted Sale Price of The House is ${}".format(np.round(samp, decimals=2)))
st.markdown('<br>', unsafe_allow_html=True)    