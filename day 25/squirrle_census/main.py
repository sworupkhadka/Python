import pandas as pd

data=pd.pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrles_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrles_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrles_count=len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirrles_count)
print(cinnamon_squirrles_count)
print(black_squirrles_count)


data_dict={
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[grey_squirrles_count,cinnamon_squirrles_count,black_squirrles_count]
}

df=pd.pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrle_count.csv")





