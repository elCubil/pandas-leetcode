import pandas as pd

activity_data = {
    "machine_id": [0, 0, 0, 0, 1, 1, 1, 1],
    "process_id": [0, 0, 1, 1, 0, 0, 1, 1],
    "activity_type": [
        "start",
        "end",
        "start",
        "end",
        "start",
        "end",
        "start",
        "end"
    ],
    "timestamp": [
        0.712,
        1.520,
        3.140,
        4.120,
        0.550,
        1.550,
        0.430,
        1.420
    ]
}

t1=pd.DataFrame(activity_data)

m1=t1.copy()
m2=t1.copy()
m1=m1[m1['activity_type']=='start']
m2=m2[m2['activity_type']=='end']

tabla=pd.merge(m1,m2,on=['machine_id','process_id'],how='inner')\
    .rename(columns={'activity_type_x':'inicio','activity_type_y':'fin'})
tabla['delta']=tabla['timestamp_y']-tabla['timestamp_x']
tabla=tabla.groupby('machine_id').agg(promedio=('delta','mean')).reset_index()
print(tabla)