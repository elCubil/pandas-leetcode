import pandas as pd
import numpy as np

seat = pd.DataFrame({
    "id": [1,2,3,4,5],
    "student": [
        "Abbot",
        "Doris",
        "Emerson",
        "Green",
        "Jeames"
    ]
})


seat['student2']=np.where(seat['id']%2==0,seat['student'].shift(1),seat['student'].shift(-1))
seat['studentt']=np.where(seat['student2'].isna(),seat['student'],seat['student2'])
seat=seat[['id','studentt']].rename(columns={'studentt':'student'})
print(seat)