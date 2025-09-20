import seaborn as sns
# pearson은 연속형
# spearman이 순서있는 범주형

sns.heatmap(data1.corr(numeric_only=True , method = 'pearson'),cmap = 'coolwarm', vmin= -1, vmax= 1, annot =True)
plt.show()