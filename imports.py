#Graficos
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Preprocesado y modelado
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline # NUEVO
from sklearn.compose import ColumnTransformer # NUEVO

#Correlacion
from scipy.stats import pointbiserialr, spearmanr, pearsonr

# Detección de outliers
from sklearn.ensemble import IsolationForest

#Modelos de clasificacion
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree

#Modelos de regresion
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor

#Tratamiento de datos
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

# Desbalanceo de Clases
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from imblearn.ensemble import BalancedRandomForestClassifier
from imblearn.ensemble import RUSBoostClassifier

# Feature Engineering
from sklearn.inspection import PartialDependenceDisplay
from sklearn.preprocessing import PolynomialFeatures
#import eli5
#from eli5.sklearn import PermutationImportance
from sklearn.inspection import permutation_importance

#Metricas
#from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score

# Selección de Modelos
from sklearn.model_selection import GridSearchCV, cross_val_score
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer

import scipy.stats as stats
from sklearn import datasets

from types import resolve_bases


#Monitorea
import mlflow
from joblib import dump, load
import psutil  # Para métricas del sistema
import pynvml # Para métricas de GPU

