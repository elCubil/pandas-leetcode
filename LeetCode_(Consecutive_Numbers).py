import pandas as pd
logs = pd.DataFrame({
    "id": [0,2,3,4,5,6,7,9,10,11,12,13],
    "num": [1,1,1,2,1,1,7,7,7,7,4,4]
})


logs['valor_anterior_1']=logs['num'].shift(1).fillna(0)
logs['valor_anterior_2']=logs['num'].shift(2).fillna(0)
logs['id_anterior_1']=logs['id'].shift(1).fillna(0)+1
logs['id_anterior_2']=logs['id'].shift(2).fillna(0)+2
logs['filtro']=(logs['num']==logs['valor_anterior_1'])&(logs['num']==logs['valor_anterior_2'])&(logs['id']==logs['id_anterior_1'])\
    &(logs['id']==logs['id_anterior_2'])
logs=logs[logs['filtro']==True][['num']].rename(columns={'num':'valor'}).reset_index(drop=True)