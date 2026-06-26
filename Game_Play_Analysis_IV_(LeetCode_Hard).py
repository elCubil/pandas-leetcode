import pandas as pd

activity = pd.DataFrame({
    "player_id": [1, 1, 2, 3, 3,4,4,5,5,5],
    "event_date": [
        "2016-03-01",
        "2016-03-02",
        "2017-06-25",
        "2016-03-01",
        "2016-03-02",
        "2015-02-01",
        "2015-02-02",
        "2020-03-01",
        "2020-03-02",
        "2020-03-10"

    ],
    "games_played": [5, 6, 1, 0, 0,4,5,1,0,10]
})

activity['event_date']=pd.to_datetime(activity['event_date'])
activity['ranking']=activity.groupby('player_id')['event_date'].rank(method='dense',ascending=True)
fecha_coneccion_1=activity[activity['ranking']==1][['player_id','event_date']].rename(columns={'player_id':'id','event_date':'fecha'})
fecha_coneccion_1['fecha_2']=fecha_coneccion_1['fecha']+pd.Timedelta(days=1)
lista_players_2da_coneccion=pd.merge(activity,fecha_coneccion_1,left_on=['player_id','event_date'],right_on=['id','fecha_2'],how='inner')
respuesta=pd.DataFrame({
    'fraccion':[lista_players_2da_coneccion['id'].nunique()/activity['player_id'].nunique()]

})
print(respuesta)