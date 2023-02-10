import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings(action='ignore')

cpath = os.path.dirname((os.path.abspath('__file__')))
df = pd.read_csv(cpath + '/산출물/교통사고패턴매칭.csv', encoding='cp949')
df = df[(df['party'].str.contains('Z') == False) & (df['crash'].str.contains('Z') == False) & (df['road'].str.contains('Z') == False) & (df['behavior'].str.contains("Z") == False)]

a = df.groupby('pattern')['발생일시'].count()
b = df.groupby('pattern')['사망자수'].sum()
df2 = pd.concat([a,b], axis=1)
df3 = df2.sort_values(by=['발생일시'], ascending=False)

df3.rename(columns={'발생일시':'사고건수'}, inplace=True)
list = [x[0:6] for x in df3.index]
df3['type'] = list
df3['prob'] = df3['사고건수']/sum(df3['사고건수'])
df3['cumsum'] = df3['prob'].cumsum()

df4 = df3[df3['cumsum']<=0.6]

types = df4['type'].unique()

os.mkdir(cpath+'/산출물/사고건수-사망자수 그래프')

plt.rc("font", family = "Malgun Gothic")
sns.set(font="Malgun Gothic", 
rc={"axes.unicode_minus":False}, style='white')


for x in types:
    temp = df4[df4['type']==x]
    if len(temp)>=10:
        q1 = temp['사망자수'].quantile(0.25)
        q3 = temp['사망자수'].quantile(0.75)
        iqr = q3 - q1

        boundary = 1.5 * iqr

        over = temp[(temp['사망자수']>q3+boundary+1) | (temp['사고건수'] == max(temp['사고건수'])) | (temp['사망자수'] == max(temp['사망자수']))]

        patterns = over.index.to_list()
        count = over['사고건수']
        dead = over['사망자수']

        fig = plt.subplots(figsize=(12,9))
        fig = sns.scatterplot(x=temp['사고건수'], y=temp['사망자수'], s=80, color='navy')
        fig.set_ylabel("사망자수", size=15)
        fig.set_xlabel("사고건수", size=15)

        for i in range(len(patterns)):
            plt.annotate(patterns[i], (count[i], dead[i]), xytext=(count[i]-(max(temp['사고건수']/20)), dead[i]+(max(temp['사망자수'])/15)), arrowprops=dict(arrowstyle="-", color='black'),size=10) 

        outputfilename = cpath + '/산출물/사고건수-사망자수 그래프/' + x + '.png'
        plt.savefig(outputfilename)

    elif len(temp)>5:
        q3 = temp['사망자수'].quantile(0.75)

        over = temp[(temp['사망자수']>q3-0.5) | (temp['사고건수'] == max(temp['사고건수'])) | (temp['사망자수'] == max(temp['사망자수']))]

        patterns = over.index.to_list()
        count = over['사고건수']
        dead = over['사망자수']

        fig = plt.subplots(figsize=(12,9))
        fig = sns.scatterplot(x=temp['사고건수'], y=temp['사망자수'], s=80, color='navy')
        fig.set_ylabel("사망자수", size=15)
        fig.set_xlabel("사고건수", size=15)

        for i in range(len(patterns)):
            plt.annotate(patterns[i], (count[i], dead[i]), xytext=(count[i]-(max(temp['사고건수']/20)), dead[i]+(max(temp['사망자수'])/15)), arrowprops=dict(arrowstyle="-", color='black'),size=10) 
        
        outputfilename = cpath + '/산출물/사고건수-사망자수 그래프/' + x + '.png'
        plt.savefig(outputfilename)

if len(os.listdir(cpath+'/산출물/사고건수-사망자수 그래프'))==0:
            os.rmdir(cpath+'/산출물/사고건수-사망자수 그래프')