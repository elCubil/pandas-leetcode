import pandas as pd

scores_data = {
    "id": [1, 2, 3, 4, 5, 6],
    "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

scores = pd.DataFrame(scores_data)

scores['ranking']=scores['score'].rank(method='dense',ascending=False)
scores=scores.sort_values(by='ranking',ascending=True).reset_index(drop=True)
print(scores)