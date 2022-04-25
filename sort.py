import pandas

df = pandas.read_csv('crops.csv')
df.to_csv('crops.csv', index=None)
x= .1
y = 15

# converting csv to html
collist = ['CROP','WATERmm','TEMPC','WATER','TEMP']
croptable = pandas.read_csv('crops.csv', usecols=collist)
rank=[]
for index, row in croptable.iterrows():
    T = row['TEMPC']
    W = row['WATERmm']
    rank.append(abs(x-W)*.4/x+abs(y-T)*.6/y)

croptable['sim'] = rank
cropsort = croptable.sort_values(by=['sim'])
print(cropsort)
