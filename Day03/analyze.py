from transformers import pipeline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as  plt

df = pd.read_csv("2025-08-28_news.csv")
df = df.drop_duplicates()
classifier = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")
df["情感"],df["置信度"] = zip(*df["摘要"].map(lambda t:(classifier(t[:512])[0]["label"],classifier(t[:512])[0]["score"])))

df.to_csv("news_with_sentiment_828.csv",index=False,encoding='utf-8-sig')       
sns.countplot(x="情感",data=df)
plt.title("新闻情感分布")
plt.savefig("sentiment_distribution_828.png")
print("分析完成！结果已保存。")