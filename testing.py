import pandas as pd

#df=pd.DataFrame({"Cool":["yes"],"Not cool":["NO"]},index=['bruh','notbruh'])
#print(df)

# calc=pd.Series([1,2,3,4,5,6,"bruh"],index=[2015,2016,2017,2018,2019,2020,4434],name="Value of years")
# print(calc)

# recipes=pd.read_csv("recipe.csv")
# print(recipes)

# recipes=pd.read_csv("recipe.csv")
# print(recipes["Small"])


# print(pd.Series({"Apple":12,"Banana":23,"Orange":34,"Strawberry":45}))
# print(pd.Series(["12","23",34,45],index=["Apple","Banana","Orange","Strawberry"]))


# recipes=pd.read_csv("recipe.csv")
# print(recipes["Large"][10])

# recipes=pd.read_csv("recipe.csv")
# recipes.index=[543543,54323542,5432542,5432542,7,67865,765432,545,4345,45,654,5654,5]    BTW doesn't work
# print(recipes.iloc[-1,:])

#Interesting side effect
# recipes=pd.read_csv("recipe.csv", index_col=1)
# recipes=recipes.set_index("year")
# print(recipes)


recipes=pd.read_csv("recipe.csv")
newRecipes=recipes.set_index("year")
print(newRecipes.loc[2020,["index","Small"]])