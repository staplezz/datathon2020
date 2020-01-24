# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:17:25 2020

@author: ilian
"""
import pandas as pd
df=pd.read_csv('authorships.csv')
df=df.groupby("author").count()
df=df[df["id_article"]>=3]
df=df.drop(["id_article"],axis=1)
df.to_csv("nodes_catalogue.csv",encoding='utf-8')



