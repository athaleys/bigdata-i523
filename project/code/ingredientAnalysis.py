# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:01:58 2017

@author: susha
"""
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#read the ingredient data
dfTrain = pd.read_json('./data/train.json')


#check/decribe data
print(dfTrain.head())
print(dfTrain.describe())

#plot recipe distribution across cuisine
plt.style.use(u'ggplot')
figCuisineDist = dfTrain.cuisine.value_counts().plot(kind="bar", title="Recipies By Cuisine")
figCuisineDist = figCuisineDist.get_figure()
figCuisineDist.tight_layout()
figCuisineDist.savefig('./images/Number_of_recipes_by_cuisine.png')
plt.clf()

#plot ingredient distribution across recipes
#print(dfTrain.ingredients)
#count recipe ingredients recipe by recipe
recipe_ingredient = [Counter(recipe) for recipe in dfTrain.ingredients]
#print(recipe_ingredient)

#sum all ingredients after the counting
ingredient_distribution = sum(recipe_ingredient, Counter())
#print(ingredient_distribution)

#load ingredients into dataframe
dfIngredient = pd.DataFrame(ingredient_distribution, index=[0])
#print(dfIngredient.head())
#print(dfIngredient.columns)

#plot graph for top 20 ingredients
ingredient_fig = dfIngredient.transpose()[0].sort_values(ascending=False, inplace=False)[:20].plot(kind='barh')
ingredient_fig.invert_yaxis()
ingredient_fig = ingredient_fig.get_figure()
ingredient_fig.tight_layout()
ingredient_fig.savefig("./images/Ingredient_Distribution.png")
plt.clf()

#plot 10 most used ingredient by cuisine
#group data by cuisine
dfCuisineGrouped = dfTrain.groupby(['cuisine'])

for cuisine in dfCuisineGrouped.groups.keys():
    print('{0:15} -> {1:10}'.format(cuisine,len(dfCuisineGrouped.groups[cuisine])))

all_ingredients = set()
dfTrain.ingredients.map(lambda x: [all_ingredients.add(i) for i in list(x)])

# fill the dataset with a column per ingredient
for ingredient in all_ingredients:
    dfTrain[ingredient] = dfTrain.ingredients.apply(lambda x: ingredient in x)

# take a serie with the number of times each ingredient was used
for cuisine in dfCuisineGrouped.groups.keys():
    df_cuisine = dfCuisineGrouped.get_group(cuisine);
    s = df_cuisine[list(all_ingredients)].apply(pd.value_counts).fillna(0).transpose()[True]
    # Finally, plot the 10 most used ingredients
    fig = s.sort_values(inplace=False, ascending=False)[:10].plot(kind='bar', title = cuisine)
    fig = fig.get_figure()
    fig.tight_layout()
    fig.savefig("./images/" + cuisine + "_10_most_used_ingredients.png")
    plt.clf()

