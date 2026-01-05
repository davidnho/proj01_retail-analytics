def show_all_data(df):
    return (
        df
          .reset_index()
    )
def show_top_10(df):
    return (
        df.head(10)
          .reset_index()
    )

def sales_summary_by_category(df):
    return (
        df.groupby('category')
          .agg(
              total_sales=('total_amount', 'sum'),
              total_orders=('order_id', 'count')
          )
          .reset_index()
    )

