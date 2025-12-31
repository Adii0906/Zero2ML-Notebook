import pandas as pd
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv("dataset/housing.csv")
df

df["income_cat"]=pd.cut(df["median_income"],
                          bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                          labels=[1, 2, 3, 4, 5])

split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

for train_index,test_index in split.split(df,df["income_cat"]):
    strat_train_set=df.loc[train_index]
    strat_test_set=df.loc[test_index]
df=strat_train_set.copy()

df_labbels=df["median_house_value"].copy()
df=df.drop("median_house_value",axis=1)

print(df,df_labbels)


# sepearte numerical and catogirical columns
num_attribs=df.drop("ocean_proximity",axis=1).columns.tolist()
cat_attribs=["ocean_proximity"]

# Pipleline  Numerical 
num_pipline=Pipeline([
    ('imputer',SimpleImputer(strategy="median")),
    ('std_scaler',StandardScaler()),
])
cat_piplene=Pipeline([
    ('imputer',SimpleImputer(strategy="most_frequent")),
    ('one_hot_encoder',OneHotEncoder(handle_unknown="ignore")),
])

# ColumnTransformer is used to apply different preprocessing steps to different subsets of features.such as num_attribs and Column cat_attribs
full_pipeline=ColumnTransformer([
    ("num",num_pipline,num_attribs),
    ("cat",cat_piplene,cat_attribs),
])

df_prepared=full_pipeline.fit_transform(df)
print(df_prepared.shape)

lin_reg = LinearRegression()
lin_reg.fit(df_prepared, df_labbels)
lin_reg_rmse=root_mean_squared_error(df_labbels,lin_reg.predict(df_prepared))
print("Linear Regression Model Trained and the root mean squared error is:",lin_reg_rmse)

tree=DecisionTreeRegressor()
tree_model=tree.fit(df_prepared,df_labbels)
tree_rmse=root_mean_squared_error(df_labbels,tree_model.predict(df_prepared))
print("Decision Tree Model Trained and the root mean squared error is:",tree_rmse)

random_forest=RandomForestRegressor()
forest_model=random_forest.fit(df_prepared,df_labbels)
random_forest_rmse=root_mean_squared_error(df_labbels,forest_model.predict(df_prepared))
print("Random Forest Model Trained and the root mean squared error is:",random_forest_rmse)

