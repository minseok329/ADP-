import matplotlib.pyplot as plt

num_col = df.select_dtypes(include='number').columns

# 히스토그램으로 분포 확인하기
fig, axes = plt.subplots(3,3, figsize=(20,10))
axes = axes.flatten()

for i, col in enumerate(num_col):
    axes[i].hist(df[col])
    axes[i].set_title(col)
plt.tight_layout()
plt.show()