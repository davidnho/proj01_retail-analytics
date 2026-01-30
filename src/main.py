from ingestion import load_sales_data
from cleaning import clean_sales_data
from transformation import sales_summary_by_category,show_top_10,show_all_data
from database import save_to_db

data = load_sales_data("data/raw/sales.json")
df = clean_sales_data(data)

summary = sales_summary_by_category(df)
save_to_db(df)

top10 = show_top_10(df)
save_to_db(df)

all_data = show_all_data(df)
save_to_db(df)

print(all_data)
print(top10)
print("Summary")
print(summary)
