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
print(df_target["target"])

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


################### Separo en entrenamiento y testing  ###############################
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.25, random_state=49150)

###################   Encontrar los mejores parametros   ######################### deberia ser una funcion
#mejor_modelo, mejores_hiperparametros = funciones.buscar_hiper_LGBM(X_resampled, y_resampled)

################## Metricas #########################
#accuracy, precision, recall, f1, cm = funciones.calcular_metricas(X_test, y_test, mejor_modelo)

# Imprimir métricas
'''print('Accuracy: ', accuracy)
print('Precision: ', precision)
print('Recall: ', recall)
print('F1 Score: ', f1)
print('Matriz de confusion: ',cm)'''

################### Guardo Modelo ##################### *****NUEVO******
#funciones.guardar_modelo(mejor_modelo)#Agregar el parametro "Nuevo Nombre"

# Configurar el URI de seguimiento de MLflow para usar Google Drive
#mlflow.set_tracking_uri('/mlruns')
