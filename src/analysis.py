class SalesAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def top_products(self, n=5):
        return (
            self.df.groupby('product')['total_amount']
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
