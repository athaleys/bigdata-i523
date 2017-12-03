# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:26:16 2017

@author: susha
"""

import json
import itertools
import xlsxwriter

#load data
dataFilePath="./data/train.json"
with open(dataFilePath) as data_file:    
    data = json.load(data_file)

ingredients = []
edgeList = []

#cretate ingredient relationship - all ingredients in same recipe are related
#relate all ingredient in same recipe with each other    
for i in range(len(data)):
    cuisineName = data[i]['cuisine']
    ingredientsPerRecipie = data[i]['ingredients']
    #print ("ingredientsPerRecipie--",type(ingredientsPerRecipie))
    #print("cuisineName--", cuisineName)
    #print("ingredientsPerRecipie--", ingredientsPerRecipie)
    #clean data
    try:
        ingredientsPerRecipie.remove("salt")
        ingredientsPerRecipie.remove("water")
    except Exception:
        "do nothing"
        
    edgeList.extend((list(itertools.combinations(ingredientsPerRecipie, 2))))
    #print("edgeList--", edgeList)
    ingredients.extend(ingredientsPerRecipie)


#get distinct ingredients    
ingredients = list(set(ingredients))
#ingredients are nodes - in nodes spreadsheet import first elemnt should be Id
ingredients.insert(0,"Id")
#edge spreadsheet should have first column as source and traget 
edgeList.insert(0, list(["Source","Target"]))

#function to write excel file from list
def writeFileFromList(x, output_filepath):
    workbook = xlsxwriter.Workbook(output_filepath)
    worksheet = workbook.add_worksheet()
    for i,e in enumerate(x):
        worksheet.write(i,0,e)

    workbook.close()

#function to write edge relationship 
def writeEdgeFileFromList(x, output_filepath):
    workbook = xlsxwriter.Workbook(output_filepath)
    worksheet = workbook.add_worksheet()
    for i,e in enumerate(x):
        worksheet.write(i,0,e[0])
        worksheet.write(i,1,e[1])
        
    workbook.close()
    
        
#write node file
nodeFile = "./data/nodes.xlsx"        
writeFileFromList(ingredients,nodeFile)

#write edge file
edgeFile = "./data/edges.xlsx"        
writeEdgeFileFromList(edgeList,edgeFile)

