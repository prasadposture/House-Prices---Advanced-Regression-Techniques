import streamlit as st
st.set_page_config(page_title="House Price Prediction", layout="wide", page_icon="🏡")
#st.sidebar.success("Select a page")
st.sidebar.markdown("<a href='https://www.linkedin.com/in/prasad-posture-6a3a77215/' target='blank'><img align='center' src='https://img.shields.io/badge/-Prasad Posture-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/prasad-posture-6a3a77215/' alt='Prasad Posture' height='20' width='100' /></a><br><a href='https://github.com/prasadposture' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/prasadposture' alt='prasadposture' height='20' width='100' /></a><br><a href='https://www.kaggle.com/prasadposture121' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture121-blue?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/prasadposture121' alt='prasadposture121' height='20' width='100' /></a>", unsafe_allow_html=True)


st.markdown('<h3 style = "background-color: #00BFFF; color :white; text-shadow: 2px 2px 5px black;", align="center">House Price Prediction</h3>',unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.write("#### Introduction")
st.write("""Predicting the sales price of the house is an important topic in real estate.
There are various factors that affect the price of a house. Some of factors may cause increment 
in the price, some of them may cause decrement, while others are dependent on one or more factors i.e. 
their combination with other factors decides whether they will increas or decrease the price. 
To help us finding the relationsip between these attribute and the sale prices, here we have data of 
1460 houses (sold). The dataset includes nealry all the factors that affect the sales price of a house 
such as over all condition, neighbourhood, presence of basement and/or garage, etc. 
I had performed exploratory data analysis to find out which factors affect the most. For the predictive
 modeling, first I used mulitple machine learning algorithms, then chose the one with the highest base 
 accuracy. After that I trained, evaluated and tuned the model with appropriate parameter values to keep
   the Root Mean Square Error (RMSE) minimum. Now, in this web application, I am using that same trained & tuned 
   model and the visuals that I had created during the process of exploratory data analysis in a jupyter notebook. I tried to make
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
st.markdown('<p class="footer-company-name">All Rights Reserved. &copy; 2023 <a href="#">Prasad Posture</a></p>', unsafe_allow_html=True)
