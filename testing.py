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


# recipes=pd.read_csv("recipe.csv")
# newRecipes=recipes.set_index("year")
# print(newRecipes.loc[2020:2023,["index","Small"]])

# recipes=pd.read_csv("recipe.csv")
# print(recipes.year==2025)

# recipes=pd.read_csv("recipe.csv")
# #recipes=recipes.set_index("year")
# print(recipes.loc[(recipes.year<=2015) | (recipes.year>=2020)])
#print(recipes.year==2020)    #So Panda library itself will go through and check. You don't have to loop and check when year == 2020

# recipes=pd.read_csv("recipe.csv")
# print(recipes.loc[recipes.year.isin([2015])])

# recipes=pd.read_csv("recipe.csv")
# print(recipes.year.isnull())
# print(recipes.year.notnull())

# recipes=pd.read_csv("recipe.csv")
# recipes["topping"]="peperonni"
# print(recipes)

# recipes=pd.read_csv("recipe.csv")
# recipes["index_backwards"]=range(len(recipes.year),0,-1)
# print(recipes)

#recipe=pd.read_csv("recipe.csv")
# print(recipe.year.describe())
# print(recipe.year.mean())
# # print(recipe.Small.unique())
# # print(recipe.Large.value_counts())
# recipe_mean=recipe.year.mean()
# # print(recipe.year.map(lambda age:age-recipe_mean))
# # print(recipe)
# # print(recipe.year.apply(lambda age:age-recipe_mean,axis="columns"))
# print(recipe.Small+" & "+recipe.Large)

# def deviationYears(row):
#     row.year=row.year-recipe_mean
#     return row

# print(recipe.apply(deviationYears,axis="columns"))
#print(recipe.Small.describe())

recipe=pd.read_csv("recipe.csv")
# print(recipe.groupby("Small").mean())
# print(recipe.apply(lambda x: x.mode().iloc[0], axis=0))
# print(recipe.apply(lambda row:max(len(str(ind)) for ind in row), axis=1))
