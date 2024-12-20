import pandas as pd

df1 = pd.read_excel(r'D:\Budventure\Wendor-wise Product Data.xlsx')
df2 = pd.read_excel(r'D:\Budventure\Product Data.xlsx')

print("Columns in df1:", df1.columns)
print("Columns in df2:", df2.columns)

merged_df = pd.merge(df1, df2, on=['Product name', 'Manufacturere'], how='outer', indicator=True)

mismatched_rows = merged_df[merged_df['_merge'] != 'both']

print(mismatched_rows[['Product name', 'Manufacturere']])
topic_df = pd.DataFrame(mismatched_rows)
print(topic_df)

topic_df.to_csv('topic_df',index=0)