
col_indicadores = ['Recommend.Other', 'Recommend.All', 'Recommend.MA', 'RSI', 'RSI[1]', 'Stoch.K', 'Stoch.D', 'Stoch.K[1]', 'Stoch.D[1]', 'CCI20', 'CCI20[1]', 'ADX', 'ADX+DI', 'ADX-DI', 'ADX+DI[1]', 'ADX-DI[1]', 'AO', 'AO[1]', 'Mom', 'Mom[1]', 'MACD.macd', 'MACD.signal', 'Rec.Stoch.RSI', 'Stoch.RSI.K', 'Rec.WR', 'W.R', 'Rec.BBPower', 'BBPower', 'Rec.UO', 'UO', 'EMA5', 'SMA5', 'EMA10', 'SMA10', 'EMA20', 'SMA20', 'EMA30', 'SMA30', 'EMA50', 'SMA50', 'EMA100', 'SMA100', 'EMA200', 'SMA200', 'Rec.Ichimoku', 'Ichimoku.BLine', 'Rec.VWMA', 'VWMA', 'Rec.HullMA9', 'HullMA9', 'Pivot.M.Classic.S3', 'Pivot.M.Classic.S2', 'Pivot.M.Classic.S1', 'Pivot.M.Classic.Middle', 'Pivot.M.Classic.R1', 'Pivot.M.Classic.R2', 'Pivot.M.Classic.R3', 'Pivot.M.Fibonacci.S3', 'Pivot.M.Fibonacci.S2', 'Pivot.M.Fibonacci.S1', 'Pivot.M.Fibonacci.Middle', 'Pivot.M.Fibonacci.R1', 'Pivot.M.Fibonacci.R2', 'Pivot.M.Fibonacci.R3', 'Pivot.M.Camarilla.S3', 'Pivot.M.Camarilla.S2', 'Pivot.M.Camarilla.S1', 'Pivot.M.Camarilla.Middle', 'Pivot.M.Camarilla.R1', 'Pivot.M.Camarilla.R2', 'Pivot.M.Camarilla.R3', 'Pivot.M.Woodie.S3', 'Pivot.M.Woodie.S2', 'Pivot.M.Woodie.S1', 'Pivot.M.Woodie.Middle', 'Pivot.M.Woodie.R1', 'Pivot.M.Woodie.R2', 'Pivot.M.Woodie.R3', 'Pivot.M.Demark.S1', 'Pivot.M.Demark.Middle', 'Pivot.M.Demark.R1', 'P.SAR', 'BB.lower', 'BB.upper', 'AO[2]', 'volume', 'change', 'low', 'high', 'EXCHANGE', 'SYMBOL', 'INTERVAL', 'SCREEN', 'fecha']
col_indicadores_int = ['Rec.Stoch.RSI','Rec.WR','Rec.BBPower','Rec.UO','Rec.Ichimoku','Rec.VWMA','Rec.HullMA9']
col_sumario = ['RECOMMENDATION', 'BUY', 'SELL', 'NEUTRAL']#Ok sin nada agregado
col_medias = ['RECOMMENDATION.1', 'BUY.1', 'SELL.1', 'NEUTRAL.1']#, 'COMPUTE']#Agregar .1 // Dropear 'COMPUTE'//Todo entero, no se normaliza
col_medias_comp = ['EMA10', 'SMA10', 'EMA20', 'SMA20', 'EMA30', 'SMA30', 'EMA50', 'SMA50', 'EMA100', 'SMA100', 'EMA200', 'SMA200', 'Ichimoku', 'VWMA', 'HullMA']
col_medias_limpias = ['EMA10', 'SMA10', 'EMA20', 'SMA20', 'EMA30', 'SMA30', 'EMA50', 'SMA50', 'EMA100', 'SMA100', 'EMA200', 'SMA200', 'VWMA']
col_medias_int = ['Rec.Stoch.RSI','Rec.WR','Rec.BBPower','Rec.UO','Rec.Ichimoku','Rec.VWMA','Rec.HullMA9','Ichimoku','HullMA']
col_medias_float =list(filter(lambda x: x not in col_medias_int, col_medias_comp))# son las medias computadas sin enteros
col_medias_chicas=['EMA10', 'SMA10', 'EMA20', 'SMA20', 'EMA30', 'SMA30']
col_medias_grandes=['EMA50', 'SMA50', 'EMA100', 'SMA100', 'EMA200', 'SMA200']
col_oscila = ['RECOMMENDATION.2', 'BUY.2', 'SELL.2', 'NEUTRAL.2']#, 'COMPUTE.1']#Agregar .2//Dropear 'COMPUTE.1'//Todo entero; no se normaliza
col_oscila_comp = ['RSI.1', 'STOCH.K', 'CCI', 'ADX.1', 'AO.1', 'Mom.1', 'MACD', 'Stoch.RSI', 'W%R', 'BBP', 'UO.1']#Todos enteros
col_objects =  ['EXCHANGE', 'SYMBOL', 'INTERVAL', 'SCREEN', 'fecha'] # Estan ubicados en col_indicadores. El resto tiene todos datos enterios o float

col_indicadores_num = list(filter(lambda x: x not in col_objects, col_indicadores))# son los indicadores sin los objetos
reemplazos = {'RSI[1]':'RSI1', 'Stoch.K[1]':'Stoch.K1', 'Stoch.D[1]': 'Stoch.D1','CCI20[1]':'CCI201', 'ADX+DI[1]':'ADX+DI1', 'ADX-DI[1]':'ADX-DI1', 'AO[1]':'AO1', 'Mom[1]':'Mom1', 'AO[2]':'AO2'}
col_indicadores_num = [reemplazos.get(word,word) for word in col_indicadores_num]

col_indicadores_float = list(filter(lambda x: x not in col_indicadores_int, col_indicadores_num))# son los indicadores sin los objetos y enteros
reemplazos = {'RSI[1]':'RSI1', 'Stoch.K[1]':'Stoch.K1', 'Stoch.D[1]': 'Stoch.D1','CCI20[1]':'CCI201', 'ADX+DI[1]':'ADX+DI1', 'ADX-DI[1]':'ADX-DI1', 'AO[1]':'AO1', 'Mom[1]':'Mom1', 'AO[2]':'AO2'}
col_indicadores_float = [reemplazos.get(word,word) for word in col_indicadores_float]

col_nulas = ['COMPUTE','COMPUTE.1']
col_objetivos = ['open','close']
col_recomendaciones = ['RECOMMENDATION','RECOMMENDATION.1','RECOMMENDATION.2']
col_predicciones = col_medias_int + col_oscila_comp + col_recomendaciones