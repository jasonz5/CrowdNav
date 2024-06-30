import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
my_font = FontProperties(family='SimHei')

# 读取数据
df = pd.read_excel("experiment.xlsx", sheet_name="num_plot")

# 设置图像大小
fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(15,5))

# 将结果数据乘以100
df.iloc[1:,:] *= 100

# 循环绘制每个子图
for i, method in enumerate(["ORCA", "SARL", "RGL_OneStep", "Gattn", "Gattn_linear"]):
    # 获取当前方法的数据
    method_df = df.iloc[1:, i*4+1:(i+1)*4+1].T
    # 绘制堆叠柱状图
    method_df.plot(kind="bar", stacked=True, ax=axs[i], legend=None)
    # 设置子图标题、x轴标题、y轴标题
    axs[i].set_title(method)
    axs[i].set_xlabel("人数", fontproperties=my_font)
    axs[i].set_ylabel("结果(%)", fontproperties=my_font)
    # 设置x轴刻度
    axs[i].set_xticklabels(['5', '10', '15', '20'], rotation=0)
    # 在每个柱状图上添加标签
    text_offset = [0,2,0]
    for j in range(len(method_df)):
        for k in range(len(method_df.columns)):
            axs[i].text(j, method_df.iloc[j,:k].sum()+method_df.iloc[j,k]/2 + text_offset[k], 
                        f"{method_df.iloc[j,k]:.0f}", ha="center", va="center")
    # 只在第一个子图上标识图例
    if i == 0:
        axs[i].legend([ "碰撞率", "超时率", "成功率"], prop=my_font)

# 调整子图之间的距离和边距
plt.subplots_adjust(wspace=0.3, left=0.05, right=0.95)

# 显示图像
plt.show()
