import pandas as pd

employee = pd.DataFrame({
    "id": [
        1,2,3,
        4,5,6,7,
        8,9,10,11,12,
        13,14
    ],
    "company": [
        "A","A","A",
        "B","B","B","B",
        "C","C","C","C","C",
        "D","D"
    ],
    "salary": [
        100,200,300,
        100,200,300,400,
        100,200,300,400,500,
        500,800
    ]
})
employee['total_company']=employee.groupby('company')['id'].transform('count')
employee['ranking']=employee.groupby('company')['salary'].rank(method='first',ascending=True)
employee['mediana1']=(employee['total_company']+2)//2
employee['mediana2']=(employee['total_company']+1)//2
employee=employee[(employee['ranking']==employee['mediana1']) | (employee['ranking']==employee['mediana2'])]
employee=employee[['id','company','salary']]


print(employee)