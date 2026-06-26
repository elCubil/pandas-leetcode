import pandas as pd

employee_data = {
    "id_emp": [1, 2, 3, 4, 5, 6,7,8,9],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max", "Janet","jp","lul","lui"],
    "salary": [85000, 90000, 80000, 60000, 90000, 69000,60000,40000,120000],
    "dep_id": [1, 1, 2, 2, 1, 1,1,1,1]
}

department_data = {
    "id_dep": [1, 2],
    "dep": ["IT", "Sales"]
}

emp = pd.DataFrame(employee_data)
dep = pd.DataFrame(department_data)
nivel=pd.Series(data=[1,2,3])

t=pd.merge(emp,dep,left_on='dep_id',right_on='id_dep',how='inner')[['name','salary','dep']]
t['ranking']=t.groupby('dep')['salary'].rank(ascending=False,method='dense')
t=t.sort_values(by=['dep','ranking'],ascending=[True,True])
t=t[t['ranking'].isin(nivel)]

print(t)