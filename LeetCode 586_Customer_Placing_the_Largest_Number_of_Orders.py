import pandas as pd

orders_data = {
    "order_number": [1, 2, 3, 4],
    "customer_number": [1, 2, 3, 3]
}

orders = pd.DataFrame(orders_data)
orders=orders.groupby('customer_number',as_index=True).agg(cuenta=('order_number','count')).reset_index()
orders=orders[orders['cuenta']==orders['cuenta'].max()][['customer_number']]
print(orders)