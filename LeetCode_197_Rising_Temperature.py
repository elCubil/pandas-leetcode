import pandas as pd
data = {
    "id": [1, 2, 3, 4,5,6,7],
    "date": [
        "2015-01-01",
        "2015-01-02",
        "2015-01-03",
        "2015-01-04",
        '2015-01-20',
        '2015-01-28',
        '2015-01-21'
    ],
    "tem": [10, 25, 20, 30,70,40,80]
}



def temperatura(df:pd.DataFrame)->pd.DataFrame:
    df['date']=pd.to_datetime(df['date'])
    tabla1=df.copy()
    tabla2=df.copy()
    tabla2["fecha_anterior"]=tabla2['date']+pd.Timedelta(days=1)
    output=pd.merge(tabla1,tabla2,left_on='date',right_on='fecha_anterior',how='inner')
    output=output[output['tem_x']>output['tem_y']][['id_x']]
    return output