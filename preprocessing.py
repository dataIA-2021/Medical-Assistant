import pandas as pd

df=pd.read_csv("maladies_et_symptomes.csv", index_col=0, encoding="utf-8")

df.iloc[0:, 2:11] =df.iloc[0:, 2:11].applymap(lambda x: x.replace('[',''))
df.iloc[0:, 2:11] =df.iloc[0:, 2:11].applymap(lambda x: x.replace(']',''))

q='{"symptoms":"Skin dryness'
h="High blood pressure Also known as HBP"
l="Open wound of the head Open wound of the head is encountered rarely on Symcat. We will add mor..."
c="Open wound of the hip Open wound of the hip is encountered rarely on Symcat. We will add more ..."
v="Open wound of the chest Also known as Open Chest Wound Open wound of the chest is encountere..."
t="Open wound of the hip Open wound of the hip is..."
b='Open wound of the knee Open wound of the knee is encountered rarely on Symcat. We will add mor...'
m="Diabetes Diabetes mellitus"
o="Open wound due to trauma Open wound due to trauma is encountered rarely on Symcat. We will add..."
p="Chronic ulcer Also known as Chronic Skin Ulcer An ulcer is a discontinuity or break in a bod..."
to_clean=[]
to_clean.extend([q, b, h, t, l, v, c, m, o, p])

for i in range(4, 10):
    for s in to_clean:
        df = df[df[f"{i}"] != s]
for k in range(2, 10):
    df[f"{k}"]=[d['symptoms'] for d in [eval(i) for i in df[f"{k}"].tolist()] if 'symptoms' in d]

df.to_csv("symptoms_preprocess.csv")