import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="House Price Prediction" ,layout="wide", page_icon="🏡")
st.markdown('<h2 style = "background-color: #F0F2F6; color :white; text-shadow: 2px 2px 5px black;", align="center">House Price Prediction</h2>',unsafe_allow_html=True)
selected = option_menu(
    menu_title=None,
    options=["Data Visulization", "Home", "Prediction"],
    icons=["pie-chart", "house", "robot"],
    default_index=1,
    orientation="horizontal"
)
if selected=="Home":
    st.write("#### Introduction")
    st.write("""Predicting the sales price of the house is an important topic in real estate.
    There are various factors that affect the price of a house. Some of factors may cause increment 
    in the price, some of them may cause decrement, while others are dependent on one or more factors i.e. 
    their combination with other factors decides whether they will increas or decrease the price. 
    To help us finding the relationsip between these attribute and the sale prices, here we have data of 
    1460 houses (sold). The dataset includes nealry all the factors that affect the sales price of a house 
    such as over all condition, neighbourhood, presence of basement and/or garage, etc. 
    I had perform exploratory data analysis to find out which factors affect the most. For the predictive
    modeling, first i used mulitple machine learning algorithms, then chose the one with the highest base 
    accuracy. After that I trained, evaluated and tuned the model with appropriate parameter values to keep
    the Root Mean Square Error (RMSE) minimum. Now, in this web application I am using that trained & tuned 
    model and the visuals that I had created during the process of exploratory data analysis. I tried to make
        this web application as user-friendly as possible, but if you have any suggestions please feel free to
        contact.""")
    st.write("___")
    st.write("#### Description")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Location Specifics", "Lot/Land Specifics", "Timeline", "Quality/Condition",
                                                        "House Specifics (Internal)","House Speicifics (External)", "Thermoregulation"])
    with tab1:
        st.write("##### MSZoning : Identifies the general zoning classification of the sale.")
        st.write("A : Agriculture, C : Commercial, FV : Floating Village Residential, I : Industrial, RH : Residential High Density, RL : Residential Low Density, RP : Residential Low Density Park, RM : Residential Medium Density")
        st.write("##### Street : Type of road access to property")
        st.write("Grvl : Gravel, Pave : Paved")
        st.write("##### Alley : Tyep of alley access to the property")
        st.write("Grvl : Gravel, Pave : Paved, NA : No Alley Access")
        st.write("##### Neighborhood : Physical locations within Ames city limits")      
        st.write("Blmngtn : Bloomington Heights, Blueste : Bluestem, BrDale : Briardale, BrkSide : Brookside, ClearCr : Clear Creek, CollgCr : College Creek, Crawfor : Crawford, Edwards : Edwards, Gilbert : Gilbert, IDOTRR : Iowa DOT and Rail Road, MeadowV : Meadow Village, Mitchel : Mitchell , Names : North Ames, NoRidge : Northridge, NPkVill : Northpark Villa, NridgHt : Northridge Heights, NWAmes : Northwest Ames, OldTown : Old Town, SWISU : South & West of Iowa State University, Sawyer : Sawyer, SawyerW : Sawyer West, Somerst : Somerset, StoneBr : Stone Brook, Timber : Timberland, Veenker : Veenker")
        st.write("##### MSSubClass : Identifies the type of dwelling involved in the sale.")
        st.write("""20 : 1-STORY 1946 & NEWER ALL STYLES,
            30 : 1-STORY 1945 & OLDER,
            40 : 1-STORY W/FINISHED ATTIC ALL AGES,
            45 : 1-1/2 STORY - UNFINISHED ALL AGES,
            50 : 1-1/2 STORY FINISHED ALL AGES,
            60 : 2-STORY 1946 & NEWER,
            70 : 2-STORY 1945 & OLDER,
            75 : 2-1/2 STORY ALL AGES,
            80 : SPLIT OR MULTI-LEVEL,
            85 : SPLIT FOYER,
            90 : DUPLEX - ALL STYLES AND AGES,
        120 : 1-STORY PUD (Planned Unit Development) - 1946 & NEWER,
        150 : 1-1/2 STORY PUD - ALL AGES,
        160 : 2-STORY PUD - 1946 & NEWER,
        180 : PUD - MULTILEVEL - INCL SPLIT LEV/FOYER,
        190 : 2 FAMILY CONVERSION - ALL STYLES AND AGES""")
    with tab2:
        st.write("##### LotShape : General shape of property")
        st.write("""
        Reg : Regular, 
        IR1 : Slightly irregular, 
        IR2 : Moderately Irregular, 
        IR3 : Irregular""")
        st.write("##### LandContour : Flatness of the property")
        st.write("""
        Lvl : Near Flat/Level, 
        Bnk : Banked - Quick and significant rise from street grade to building,
        HLS : Hillside - Significant slope from side to side,
        Low : Depression""")
        st.write("##### LotConfig : Lot configuration")
        st.write("""
        Inside : Inside lot,
        Corner : Corner lot,
        CulDSac : Cul-de-sac,
        FR2 : Frontage on 2 sides of property,
        FR3 : Frontage on 3 sides of property""")
        st.write("##### LandSlope : Slope of property")
        st.write("""
        Gtl : Gentle slope
        Mod : Moderate Slope	
        Sev : Severe Slope""")
        st.write("##### LotFrontage : Linear feet of street connected to property")
        st.write("##### LotArea : Lot size in square feet")
    with tab3:
        st.write("##### YearBuilt : Original construction date")
        st.write("##### YearRemodAdd : Remodel date (same as construction date if no remodeling or additions")
        st.write("##### MoSold : Month Sold (MM)")
        st.write("##### YrSold : Year Sold (YYYY)")
    with tab4:
        st.write("##### OverallQual: Rates the overall material and finish of the house")
        st.write("""
        10 : Very Excellent,
        9 : Excellent,
        8 : Very Good,
        7 : Good,
        6 : Above Average,
        5 : Average,
        4 : Below Average,
        3 : Fair,
        2 : Poor,
        1 : Very Poor""")
        st.write("##### OverallCond : Rates the overall condition of the house")
        st.write("""
        10 : Very Excellent
        9 : Excellent
        8 : Very Good
        7 : Good
        6 : Above Average	
        5 : Average
        4 : Below Average	
        3 : Fair
        2 : Poor
        1 : Very Poor""")
        st.write("##### Condition1 : Proximity to various conditions")
        st.write("""
        Artery : Adjacent to arterial street
        Feedr : Adjacent to feeder street	
        Norm : Normal	
        RRNn : Within 200' of North-South Railroad
        RRAn : Adjacent to North-South Railroad
        PosN : Near positive off-site feature--park, greenbelt, etc.
        PosA : Adjacent to postive off-site feature
        RRNe : Within 200' of East-West Railroad
        RRAe : Adjacent to East-West Railroad""")
        st.write("##### Condition2: Proximity to various conditions (if more than one is present)")
        st.write("""
        Artery : Adjacent to arterial street
        Feedr : Adjacent to feeder street	
        Norm : Normal	
        RRNn : Within 200' of North-South Railroad
        RRAn : Adjacent to North-South Railroad
        PosN : Near positive off-site feature--park, greenbelt, etc.
        PosA : Adjacent to postive off-site feature
        RRNe : Within 200' of East-West Railroad
        RRAe : Adjacent to East-West Railroad""")
        st.write("##### SaleCondition : Condition of sale")
        st.write("""
        Normal : Normal Sale
        Abnorml : Abnormal Sale -  trade, foreclosure, short sale
        AdjLand : Adjoining Land Purchase
        Alloca : Allocation - two linked properties with separate deeds, typically condo with a garage unit	
        Family : Sale between family members
        Partial : Home was not completed when last assessed (associated with New Homes)""")
    with tab5:
        st.write("##### FullBath : Full bathrooms above grade")
        st.write("##### HalfBath : Half baths above grade")
        st.write("##### BedroomAbcGr : Bedrooms above grade (does NOT include basement bedrooms)")
        st.write("##### Kitchen : Kitchens above grade")
        st.write("##### TotRmsAbvGrd : Total rooms above grade (does not include bathrooms)")
        st.write("##### KitchenQual : Kitchen quality")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Typical/Average
        Fa : Fair
        Po : Poor""")
    with tab6:
        st.write("##### BldgType: Type of dwelling")
        st.write("""
        1Fam : Single-family Detached	
        2FmCon : Two-family Conversion; originally built as one-family dwelling
        Duplx : Duplex
        TwnhsE : Townhouse End Unit
        TwnhsI : Townhouse Inside Unit""")
        st.write("##### HouseStyle : Style of dwelling")
        st.write("""
        1Story : One story,
        1.5Fin : One and one-half story: 2nd level finished
        1.5Unf : One and one-half story: 2nd level unfinished
        2Story : Two story
        2.5Fin : Two and one-half story: 2nd level finished
        2.5Unf : Two and one-half story: 2nd level unfinished
        SFoyer : Split Foyer
        SLvl : Split Level""")
        st.write("##### RoofStyle: Type of roof")
        st.write("""
        Flat : Flat
        Gable : Gable
        Gambrel : Gabrel (Barn)
        Hip : Hip
        Mansard : Mansard
        Shed : Shed""")
            
        st.write("##### RoofMatl : Roof material")
        st.write("""
        ClyTile : Clay or Tile
        CompShg : Standard (Composite) Shingle
        Membran : Membrane
        Metal : Metal
        Roll : Roll
        Tar&Grv : Gravel & Tar
        WdShake : Wood Shakes
        WdShngl : Wood Shingles""")
        
        st.write("##### Foundation : Type of foundation")
        st.write("""
        BrkTil : Brick & Tile
        CBlock : Cinder Block
        PConc : Poured Contrete	
        Slab : Slab
        Stone : Stone
        Wood :Wood""")
    with tab7:
        st.write("##### CentralAir: Central air conditioning")
        st.write("""
        N : No
        Y : Yes""")
        st.write("##### Heating: Type of heating")
        st.write("""
        Floor : Floor Furnace
        GasA : Gas forced warm air furnace
        GasW : Gas hot water or steam heat
        Grav : Gravity furnace	
        OthW : Hot water or steam heat other than gas
        Wall : Wall furnace""")
        st.write("##### HeatingQC: Heating quality and condition")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Average/Typical
        Fa :Fair
        Po : Poor""")
        st.write("##### Fireplaces: Number of fireplaces")
        st.write("##### FireplaceQu: Fireplace quality")
        st.write("""
        Ex : Excellent - Exceptional Masonry Fireplace
        Gd : Good - Masonry Fireplace in main level
        TA : Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
        Fa : Fair - Prefabricated Fireplace in basement
        Po : Poor - Ben Franklin Stove
        NA : No Fireplace""")
        
    tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17 = st.tabs(["Exterior", "Basement", "Garage", "Porch", "Pool", "Internal Area",
                                                                    "Surroundings","Masnory","Miscellaneous", "Others"])
    with tab8:
        st.write("##### ExterQual: Evaluates the quality of the material on the exterior")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Average/Typical
        Fa : Fair
        Po : Poor""")
        
        st.write("##### ExterCond: Evaluates the present condition of the material on the exterior")
        st.write("""	
        Ex : Excellent
        Gd : Good
        TA : Average/Typical
        Fa : Fair
        Po : Poor""")
        st.write("##### Exterior1st: Exterior covering on house")
        st.write("""
        AsbShng : Asbestos Shingles
        AsphShn : Asphalt Shingles
        BrkComm : Brick Common
        BrkFace : Brick Face
        CBlock : Cinder Block
        CemntBd : Cement Board
        HdBoard : Hard Board
        ImStucc : Imitation Stucco
        MetalSd : Metal Siding
        Other : Other
        Plywood : Plywood
        PreCast : PreCast	
        Stone : Stone
        Stucco : Stucco
        VinylSd : Vinyl Siding
        Wd Sdng : Wood Siding
        WdShing : Wood Shingles""")
        
        st.write("##### Exterior2nd: Exterior covering on house (if more than one material")
        st.write("""
        AsbShng : Asbestos Shingles
        AsphShn : Asphalt Shingles
        BrkComm : Brick Common
        BrkFace : Brick Face
        CBlock : Cinder Block
        CemntBd : Cement Board
        HdBoard : Hard Board
        ImStucc : Imitation Stucco
        MetalSd : Metal Siding
        Other : Other
        Plywood : nlywood
        PreCast : PreCast
        Stone : Stone
        Stucco : Stucco
        VinylSd : Vinyl Siding
        Wd Sdng : Wood Siding
        WdShing : Wood Shingles""")
    with tab9:
        st.write("##### BsmtQual: Evaluates the height of the basement")
        st.write("""
        Ex : Excellent (100+ inches)	
        Gd : Good (90-99 inches)
        TA : Typical (80-89 inches)
        Fa : Fair (70-79 inches)
        Po : Poor (<70 inches
        NA : No Basement""")
        st.write("##### BsmtCond: Evaluates the general condition of the basement")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Typical - slight dampness allowed
        Fa : Fair - dampness or some cracking or settling
        Po : Poor - Severe cracking, settling, or wetness
        NA : No Basement""")
        
        st.write("##### BsmtExposure: Refers to walkout or garden level walls")
        st.write("""
        Gd : Good Exposure
        Av : Average Exposure (split levels or foyers typically score average or above)	
        Mn : Mimimum Exposure
        No : No Exposure
        NA : No Basement""")
        
        st.write("##### BsmtFinType1: Rating of basement finished area")
        st.write("""
        GLQ : Good Living Quarters
        ALQ : Average Living Quarters
        BLQ : Below Average Living Quarters	
        Rec : Average Rec Room
        LwQ : Low Quality
        Unf : Unfinshed
        NA : No Basement""")
        
            
        st.write("##### BsmtFinSF1: Type 1 finished square feet")
        st.write("###### BsmtFinType2: Rating of basement finished area (if multiple types)")
        st.write("""
        GLQ : Good Living Quarters
        ALQ : Average Living Quarters
        BLQ : Below Average Living Quarters	
        Rec : Average Rec Room
        LwQ : Low Quality
        Unf : Unfinshed
        NA : No Basement""")
        st.write("##### BsmtFinSF2: Type 2 finished square feet")
        st.write("##### BsmtUnfSF: Unfinished square feet of basement area")
        st.write("##### TotalBsmtSF: Total square feet of basement area")
        st.write("##### BsmtFullBath : Basement full bathrooms")
        st.write("##### BsmtHalfBath : Basement half bathrooms")

    with tab10:
        st.write("##### GarageType : Garage location")
        st.write("""
        2Types : More than one type of garage
        Attchd : Attached to home
        Basment : Basement Garage
        BuiltIn : Built-In (Garage part of house - typically has room above garage)
        CarPort : Car Port
        Detchd : Detached from home
        NA : No Garage""")
        st.write("##### GarageYrBlt: Year garage was built")
        st.write("##### GarageFinish: Interior finish of the garage")
        st.write("""
        Fin : Finished
        RFn : Rough Finished	
        Unf : Unfinished
        NA : No Garage""")
        st.write("##### GarageCars: Size of garage in car capacity")
        st.write("##### GarageArea: Size of garage in square feet")
        st.write("##### GarageQual: Garage quality")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Typical/Average
        Fa : Fair
        Po : Poor
        NA : No Garage""")
        st.write("##### GarageCond: Garage condition")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Typical/Average
        Fa : Fair
        Po : Poor
        NA : No Garage""")
    with tab11:
        st.write("##### OpenPorchSF: Open porch area in square feet")
        st.write("##### EnclosedPorch: Enclosed porch area in square feet")
        st.write("##### 3SsnPorch: Three season porch area in square feet")
        st.write("##### ScreenPorch: Screen porch area in square feet")
    with tab12:
        st.write("##### PoolArea: Pool area in square feet")
        st.write("##### nPoolQC: Pool quality")
        st.write("""
        Ex : Excellent
        Gd : Good
        TA : Average/Typical
        Fa : Fair
        NA : No Pool""")
    with tab13:
        st.write("##### 1stFlrSF: First Floor square feet")
        st.write("##### 2ndFlrSF: Second floor square feet")
        st.write("##### LowQualFinSF: Low quality finished square feet (all floors)")
        st.write("##### GrLivArea: Above grade (ground) living area square feet")
    with tab14:
        st.write("##### PavedDrive: Paved driveway")
        st.write("""
        Y : Paved 
        P : Partial Pavement
        N : Dirt/Gravel""")
        st.write("##### WoodDeckSF: Wood deck area in square feet")
        st.write("##### Fence: Fence quality")
        st.write("""
        GdPrv : Good Privacy
        MnPrv : Minimum Privacy
        GdWo : Good Wood
        MnWw : Minimum Wood/Wire
        NA : No Fence""")
    with tab15:
        st.write("##### MasVnrType: Masonry veneer type")
        st.write("""
        BrkCmn : Brick Common
        BrkFace : Brick Face
        CBlock : Cinder Block
        None : None
        Stone : Stone""")
        st.write("##### MasVnrArea: Masonry veneer area in square feet")

    with tab16:
        st.write("##### MiscFeature: Miscellaneous feature not covered in other categories")
        st.write("""
    Elev : Elevator
        Gar2 : 2nd Garage (if not described in garage section)
        Othr : Other
        Shed : Shed (over 100 SF)
        TenC : Tennis Court
        NA : None""")
        st.write("##### MiscVal: $Value of miscellaneous feature")

    with tab17:
        st.write("##### Utilities: Type of utilities available")
        st.write("""
        AllPub : All public Utilities (E,G,W,& S)	
        NoSewr : Electricity, Gas, and Water (Septic Tank)
        NoSeWa : Electricity and Gas Only
        ELO : Electricity only""")
        st.write("##### Electrical: Electrical system")
        st.write("""
        SBrkr : Standard Circuit Breakers & Romex
        FuseA : Fuse Box over 60 AMP and all Romex wiring (Average)	
        FuseF : 60 AMP Fuse Box and mostly Romex wiring (Fair)
        FuseP : 60 AMP Fuse Box and mostly knob & tube wiring (poor)
        Mix : Mixed""")
        st.write("##### Functional: Home functionality (Assume typical unless deductions are warranted)")
        st.write("""
        Typ : Typical Functionality
        Min1 : Minor Deductions 1
        Min2 : Minor Deductions 2
        Mod : Moderate Deductions
        Maj1 : Major Deductions 1
        Maj2 : Major Deductions 2
        Sev : Severely Damaged
        Sal : Salvage only""")
        st.write("##### SaleType: Type of sale")
        st.write("""
        WD  : Warranty Deed - Conventional
        CWD : Warranty Deed - Cash
        VWD : Warranty Deed - VA Loan
        New : Home just constructed and sold
        COD : Court Officer Deed/Estate
        Con : Contract 15% Down payment regular terms
        ConLw : Contract Low Down payment and low interest
        ConLI : Contract Low Interest
        ConLD : Contract Low Down
        Oth : Other""")
    st.write("___")

if selected=="Data Visulization":

    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px

    df=pd.read_csv('train.csv')
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
    st.write("___")
if selected=="Prediction":
    import joblib as jb
    import streamlit as st
    from pandas import read_csv
    import numpy as np

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
    st.write("___")
    st.write("#### 🏡 The Predicted Sale Price of The House is ${}".format(np.round(samp, decimals=2)))
    st.markdown('<br>', unsafe_allow_html=True)
    st.write("___")

a,b,c = st.columns(3)
with a:
    st.markdown("<a href='https://www.linkedin.com/in/prasad-posture-6a3a77215/' target='blank'><img align='center' src='https://img.shields.io/badge/-Prasad Posture-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/prasad-posture-6a3a77215/' alt='Prasad Posture' height='20' width='100' /></a>", unsafe_allow_html=True)
with b:    
    st.markdown("<a href='https://github.com/prasadposture' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/prasadposture' alt='prasadposture' height='20' width='100' /></a>", unsafe_allow_html=True)
with c:
    st.markdown("<a href='https://www.kaggle.com/prasadposture121' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture121-blue?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/prasadposture121' alt='prasadposture121' height='20' width='100' /></a>", unsafe_allow_html=True)