#from config import col_indicadores_float
from imports import *
from config import col_indicadores_float


def categorizar_df(df):
  # Definir el diccionario de mapeo de valores para pasar valores Object a int: BUY: 1, SELL: -1, NEUTRAL: 0.
  mapping = {'BUY': 1, 'SELL': -1, 'NEUTRAL': 0,'STRONG_BUY': 2, 'STRONG_SELL': -2}
  # Reemplazar los valores en todo el DataFrame
  df_optimo = df.replace(mapping).copy()
  return df_optimo

def normalizar_floats(df):
  scaler = StandardScaler() # (x-M)/d
  df[col_indicadores_float] = scaler.fit_transform(df[col_indicadores_float]).copy()#.drop(df_optimizado[['close']],axis = 1))
  return df

def tratar_df(df):
    #Transformo las variables categoricas
    df_optimo = categorizar_df(df)

    #Renombro las columnas con conflictos
    df_optimo.rename(columns={'RSI[1]':'RSI1', 'Stoch.K[1]':'Stoch.K1', 'Stoch.D[1]': 'Stoch.D1','CCI20[1]':'CCI201', 
    'ADX+DI[1]':'ADX+DI1', 'ADX-DI[1]':'ADX-DI1', 'AO[1]':'AO1', 'Mom[1]':'Mom1', 'AO[2]':'AO2'},inplace = True)

    df_optimo['tomorrow'] = df_optimo["close"].shift(-1)
    df_optimo['target'] = (df_optimo['tomorrow'] > df_optimo["close"]).astype(int)

    return df_optimo


#Funcion que guarda el modelo ****NUEVO****
def guardar_modelo(modelo):
   file_path = '/modelos'

   # Llamar a la función de guardar después de entrenar el modelo
   ruta_modelo = os.path.join(file_path, 'lgbm_tuning_model.joblib')
   dump(modelo, ruta_modelo)
   print(f"Modelo guardado en: {ruta_modelo}")
