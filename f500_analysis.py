import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('f500.csv', index_col=0)
df.index.name = None
df.info()
print(df["profits"].mean())
previously_ranked = df[df["previous_rank"].notnull()]
revenue_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
df["rank_change"] = revenue_change
df.info()
# visualizing the dataset
plt.figure(figsize=(10, 6))
plt.hist(df["revenues"], bins=20, color='skyblue', edgecolor='black') 
plt.title('Distribution of Company Revenues (F500 Dataset)')
plt.xlabel('Revenue (in millions/billions - scale depends on dataset)')
plt.ylabel('Number of Companies')
plt.grid(axis='y', alpha=0.5)
plt.show()