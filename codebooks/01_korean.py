import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 깨짐 방지 (Windows 전용)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Malgun Gothic'

# 안될경우
path = "c:/Windows/Fonts/malgun.ttf"   # 맑은 고딕
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)
