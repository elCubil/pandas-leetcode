import pandas as pd

logins_data = {
    "user_id": [6, 6, 6, 8, 8, 2, 2, 14, 14],
    "time": [
        "2020-06-30 15:06:07",
        "2021-04-21 14:06:06",
        "2019-03-07 00:18:15",
        "2020-02-01 05:10:53",
        "2020-12-30 00:46:50",
        "2020-01-16 02:49:50",
        "2019-08-25 07:59:08",
        "2019-07-14 09:00:00",
        "2021-01-06 11:59:59"
    ]
}

log = pd.DataFrame(logins_data)

log['time']=pd.to_datetime(log['time'])

log=log[log['time'].dt.year==2020]
log=log.groupby('user_id',as_index=False).agg(ultima_conexcion=('time','max'))

print(log)