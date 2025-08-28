import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/301141SZ_raw.csv")
print(df.info())
df = df.dropna()
df = df.drop_duplicates()
df['trade_date'] = pd.to_datetime(df['trade_date'],format='%Y%m%d')
# 重命名列
df = df.rename(columns={
    "trade_date":"日期",
    "open":"开盘价",
    "close":"收盘价",
    "vol":"成交量"
})
# ==============================
# 4. 计算年度统计指标
# ==============================
df['月份'] = df['日期'].dt.month
annual_stats = df.groupby('月份')['收盘价'].agg(['mean','max','min']).reset_index()
annual_stats = annual_stats.rename(columns={
    'mean':'平均收盘价',
    'max':'最高收盘价',
    'min':'最低收盘价'
})
print("\n月度统计：\n",annual_stats)
annual_csv_path = "data/annual_month_stats.csv"
annual_stats.to_csv(annual_csv_path,index=False,encoding="utf-8-sig")
print(f"月度统计结果已保存到：{annual_csv_path}")

# ==============================
# 5. 绘制收盘价折线图
# ==============================
plt.figure(figsize=(10,5))
plt.plot(annual_stats['月份'],annual_stats['平均收盘价'],marker='o',label='月平均收盘价')
plt.title("中科磁业2024年月平均收盘价趋势")
plt.xlabel("日期")
plt.ylabel("价格")
plt.grid(True)
plt.legend()

img_path="data/closing_price_month_trend_301141.png"
plt.savefig(img_path,dpi=300)
plt.show()
print(f"收盘价折线图已保存到: {img_path}")