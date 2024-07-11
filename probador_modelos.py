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

############   Agrego columnas target   #################
df_target = funciones.crea_target_long(df=df_optimo, nombre_target="LONG_target_20p_05",porciento_varia = 0.5, proyeccion = 20)
#print(df_target["target"])

##################### Train y test del df original   ###################
# Defino X e y
X = df_target[col_indicadores_num]
y = df_target["LONG_target_20p_05"]


################### Levanto el modelo a utilizar ######################
modelo = load('modelos\lgbm_tuning_model.joblib')

# Uso del modelo cargado para hacer predicciones
y_pred = modelo.predict(X) # El X_test NO QUEDA GUARDADO EN EL .joblib
accuracy = accuracy_score(y, y_pred)
print("Exactitud del modelo cargado:", accuracy)
