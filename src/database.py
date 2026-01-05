import sqlite3

sales_db = "data/sales.db"

def save_to_db(df):
    conn = sqlite3.connect(sales_db)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()
