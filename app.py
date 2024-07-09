#Mis funciones
import funciones
from imports import *
from config import col_indicadores_num, col_indicadores_int, col_indicadores_float

os.system('cls')

############# Carga de datos #################################
df = pd.read_csv('concat_1min.csv', index_col=0)
df5 = pd.read_csv('concat_5min.csv', index_col=0)

############    Tratamiento de los datos    ##################
df_optimo = funciones.tratar_df(df)

##Standar scaler para floats - Por ahora no lo hago


##################### Train y test del df original   ###################
# Defino X e y
X = df_optimo[col_indicadores_num]
y = df_optimo['target']

# Divido el conjunto de datos en conjuntos de entrenamiento y prueba del dataset sin haber hecho balanceo de clases
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.25, random_state=49150)#, stratify=y)

#####################   Balanceo de clases   ##############
# Crear el objeto de sobremuestreo
ros = RandomOverSampler(random_state=49150)
# Aplicar el sobremuestreo. Ahora tengo X e y balanceadas
X_resampled, y_resampled = ros.fit_resample(X, y)


###################   Entrenamiento   #########################
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.25, random_state=49150)

search_space1 = {
    'num_iterations': Integer(1500, 3000),
    'learning_rate': Real(0.1, 0.4),
    'max_depth': Integer(80, 150),
    #'objective': 'binary',
    'num_leaves': Integer(20, 50),
    'min_data_in_leaf': Integer(1, 15),
    'max_bin': Integer(20, 50),
    'bagging_fraction': Real(0.5 , 1),
    'feature_fraction':Real(0.5, 1),
    #'categorical_feature':
}

# Instanciar BayesSearchCV con el modelo y el espacio de búsqueda
lgbm = LGBMClassifier()
lgbm_bayes_search = BayesSearchCV(lgbm, search_space1, n_iter=70, scoring='f1', cv=5, random_state=49150, n_jobs=-1)

# Ajustar BayesSearchCV al conjunto de entrenamiento
lgbm_bayes_search.fit(X_train, y_train)

# Imprimir mejores parametros
print(f'Best Parameters: {lgbm_bayes_search.best_params_}')

################## Metricas #########################
#Predigo con los nuevos hiperparametros
y_pred_lgbm = lgbm_bayes_search.predict(X_test)

# Calcular métricas
accuracy_lgbm = accuracy_score(y_test, y_pred_lgbm)
cm_lgbm = confusion_matrix(y_test, y_pred_lgbm)
precision_lgbm = precision_score(y_test, y_pred_lgbm)#, average='weighted')
recall_lgbm = recall_score(y_test, y_pred_lgbm)#, average='weighted')
f1_lgbm = f1_score(y_test, y_pred_lgbm)#, average='weighted')

# Imprimir métricas
print('Accuracy: ', accuracy_lgbm)
print('Precision: ', precision_lgbm)
print('Recall: ', recall_lgbm)
print('F1 Score: ', f1_lgbm)
print('Matriz de confusion: ', cm_lgbm)


################### Guardo Modelo ##################### *****NUEVO******
funciones.guardar_modelo(lgbm)#Agregar el parametro "Nuevo Nombre"


# Configurar el URI de seguimiento de MLflow para usar Google Drive
mlflow.set_tracking_uri('/mlruns')
