# 정렬
data1.sort_values('거주연도',ascending = True).groupby(by = '계약자고유번호').tail(1)

