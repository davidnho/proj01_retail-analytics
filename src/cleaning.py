import pandas as pd

def clean_sales_data(data):
    df = pd.DataFrame(data)

    df.drop_duplicates(inplace=True)
    df['order_date'] = pd.to_datetime(df['order_date'])

    df['total_amount'] = df['price'] * df['quantity']

    return df