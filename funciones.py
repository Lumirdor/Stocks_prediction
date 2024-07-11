#from config import col_indicadores_float
from imports import *
from config import col_indicadores_float


def categorizar_df(df):
  # Definir el diccionario de mapeo de valores para pasar valores Object a int: BUY: 1, SELL: -1, NEUTRAL: 0.
  mapping = {'BUY': 1, 'SELL': -1, 'NEUTRAL': 0,'STRONG_BUY': 2, 'STRONG_SELL': -2}
  # Reemplazar los valores en todo el DataFrame
  df_optimo = df.replace(mapping).copy()
  return df_optimo

#Funcion que normaliza los valores del tipo float mediante un standard scaler
def normalizar_floats(df):
  scaler = StandardScaler() # (x-M)/d
  df[col_indicadores_float] = scaler.fit_transform(df[col_indicadores_float]).copy()#.drop(df_optimizado[['close']],axis = 1))
  return df

#Funcion
def tratar_df(df):
    #Transformo las variables categoricas
    df_optimo = categorizar_df(df)

    #Renombro las columnas con conflictos
    df_optimo.rename(columns={'RSI[1]':'RSI1', 'Stoch.K[1]':'Stoch.K1', 'Stoch.D[1]': 'Stoch.D1','CCI20[1]':'CCI201', 
    'ADX+DI[1]':'ADX+DI1', 'ADX-DI[1]':'ADX-DI1', 'AO[1]':'AO1', 'Mom[1]':'Mom1', 'AO[2]':'AO2'},inplace = True)

    return df_optimo


#Funcion que guarda el modelo ****NUEVO****
def guardar_modelo(modelo, nuevo_nombre = "No_name"):
  file_path = 'modelos'

  # Llamar a la función de guardar después de entrenar el modelo
  ruta_modelo = os.path.join(file_path, nuevo_nombre)
  dump(modelo, ruta_modelo)
  print(f"Modelo guardado en: {ruta_modelo}")


### Funcion que encuentra los mejores hiperparametros para un modelo LGBM
def buscar_hiper_LGBM (X,y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=49150)

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
  lgbm_bayes_search = BayesSearchCV(lgbm, search_space1, n_iter=1, scoring='f1', cv=5, random_state=49150, n_jobs=-1)

  # Ajustar BayesSearchCV al conjunto de entrenamiento
  lgbm_bayes_search.fit(X_train, y_train)

  # Imprimir mejores parametros
  print(f'Best Parameters: {lgbm_bayes_search.best_params_}')

  return lgbm_bayes_search, lgbm_bayes_search.best_params_



### Funcion que calcula las metricas
def calcular_metricas(X, y, mejor_modelo):
  #Predigo con los nuevos hiperparametros
  y_pred_lgbm = mejor_modelo.predict(X)

  # Calcular métricas
  accuracy_lgbm = accuracy_score(y, y_pred_lgbm)
  cm_lgbm = confusion_matrix(y, y_pred_lgbm)
  precision_lgbm = precision_score(y, y_pred_lgbm)#, average='weighted')
  recall_lgbm = recall_score(y, y_pred_lgbm)#, average='weighted')
  f1_lgbm = f1_score(y, y_pred_lgbm)#, average='weighted') 

  return accuracy_lgbm, cm_lgbm, precision_lgbm, recall_lgbm, f1_lgbm



### Funcion: Si el precio toca el objetivo POSITIVO en el periodo elegido (proyeccion) devuelve 1. Si toca el stop o no toca el target devuelve 0
def toca_long(referencia, porciento_varia, columna, proyeccion):

  variacion_positiva = 1 + (porciento_varia/100)
  variacion_negativa = 1 - (porciento_varia/100)
  resultado = 0

  # Recorremos la columna 'close' y aplicamos las condiciones
  for precio in columna.head(proyeccion):
    if precio >= variacion_positiva * referencia:
      resultado = 1
    elif precio <= variacion_negativa * referencia:
      resultado = 0
  return resultado

### Funcion que crea una columna  con 1 si se toco el target positivo y 0 si no se toco o se fue por el stop
def crea_target_long(df, nombre_target = "LONG_target_20p_05", porciento_varia = 0.5, proyeccion = 20):
  for indice, fila in df.iterrows():
    indice_inicio = df.index.get_loc(indice)#Obtiene el indice en el cual se esta iterando
    df.loc[indice,nombre_target]=toca_long(referencia = df.loc[indice,'close'], porciento_varia = porciento_varia, columna = df['close'].iloc[indice_inicio:],proyeccion=proyeccion)

  df['tomorrow'] = df["close"].shift(-1)
  df['target'] = (df['tomorrow'] > df["close"]).astype(int)

  return df