# -*- coding: utf-8 -*-
"""RFM_Customer_Segmentation.ipynb


# Import libraries & data
"""

import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

!pip install squarify
import squarify

from google.colab import drive
drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/Trâm_Python_Final_Project/ecommerce retail.xlsx'

ecommerce_retail = pd.read_excel(file_path, sheet_name='ecommerce retail')
segmentation = pd.read_excel(file_path, sheet_name='Segmentation')

ecommerce_retail

segmentation

"""#EDA
###There are 135,080 missing data in the `CustomerID` and 1,454 in the `Description`=> action: Remove rows with missing data in the `CustomerID` as it is the primary key for customer groups, and keep the data in the `Description` unchanged.
###Data type is normal.
###There are 5,225 duplicate rows => action: no action needed.
###Keep only positive values in the `UnitPrice` and `Quantity` columns.
"""

ecommerce_retail.info()

ecommerce_retail.describe()

#Missing data
print(ecommerce_retail.isnull().sum())

#Remove missing data in the CustomerID column
ecommerce_retail = ecommerce_retail.dropna(subset=['CustomerID'])

#Duplicates data
ecommerce_retail.duplicated().sum()

#Keep only positive values in the UnitPrice and Quantity columns
ecommerce_retail = ecommerce_retail[(ecommerce_retail['Quantity'] > 0) & (ecommerce_retail['UnitPrice'] > 0)]

"""#RFM Score"""

reference_date = pd.to_datetime('2011-12-31')

#Calculate the RFM score for each customer
RFM_Score = ecommerce_retail.groupby('CustomerID').agg(
    Recency=('InvoiceDate', lambda x: (reference_date - x.max()).days),
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('Quantity', lambda x: (x * ecommerce_retail.loc[x.index, 'UnitPrice']).sum())
).reset_index()

RFM_Score.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

RFM_Score['CustomerID'] = RFM_Score['CustomerID'].astype(int)
RFM_Score

#Create RFM_Score on scale from 1 to 5
RFM_Score['recency_rank'] = RFM_Score['Recency'].rank(method='first')
RFM_Score['frequency_rank'] = RFM_Score['Frequency'].rank(method='first')
RFM_Score['monetary_rank'] = RFM_Score['Monetary'].rank(method='first')


RFM_Score['R_Score'] = pd.qcut(RFM_Score['recency_rank'], 5, labels=[5, 4, 3, 2, 1])
RFM_Score['F_Score'] = pd.qcut(RFM_Score['frequency_rank'], 5, labels=[1, 2, 3, 4, 5])
RFM_Score['M_Score'] = pd.qcut(RFM_Score['monetary_rank'], 5, labels=[1, 2, 3, 4, 5])

RFM_Score['RFM_Score'] = RFM_Score['R_Score'].astype(str) + RFM_Score['F_Score'].astype(str) + RFM_Score['M_Score'].astype(str)

RFM_Score = RFM_Score[['CustomerID', 'Recency', 'Frequency', 'Monetary', 'R_Score', 'F_Score', 'M_Score', 'RFM_Score']]

RFM_Score

"""#RFM Score with Segmentation"""

#Transform, split the Segmentation table
segmentation.columns = segmentation.columns.str.replace(' ', '_')
segmentation['RFM_Score'] = segmentation['RFM_Score'].str.split(',')
segmentation = segmentation.explode('RFM_Score').reset_index(drop=True)

#Combining RFM_Score with customer segmentation
segmentation['RFM_Score'] = segmentation['RFM_Score'].astype(int)
RFM_Score['RFM_Score'] = RFM_Score['RFM_Score'].astype(int)

RFM_Segmentation = RFM_Score.merge(segmentation, on='RFM_Score', how='left')

RFM_Segmentation

"""#Visualization

##Histogram
"""

colnames = ['Recency', 'Frequency', 'Monetary']

for col in colnames:
    fig, ax = plt.subplots(figsize=(12, 3))
    sns.histplot(RFM_Score[col], kde=True, ax=ax)
    ax.set_title('Distribution of %s' % col)
    plt.show()

"""##Treemap"""

#Segment by Customers

grp = RFM_Segmentation.groupby('Segment').agg({'CustomerID': 'count'}).reset_index()

colors = ['#FF0000', '#00FFFF', '#FFFF00', '#A52A2A', '#800080', '#800000', '#00FF00', '#808000', '#FFC0CB', '#FFA500', '#FF00FF']

fig, ax = plt.subplots(1, figsize=(15, 8))

squarify.plot(sizes=grp['CustomerID'],
              label=grp['Segment'],
              value=[f'{x*100/len(RFM_Segmentation):.2f}%' for x in grp['CustomerID']],
              alpha=.8,
              color=colors,
              bar_kwargs=dict(linewidth=1.5, edgecolor="white"))

plt.title('RFM Segments of Customer Count', fontsize=16)
plt.axis('off')
plt.show()

#Segment by Total sales

grp_sales = RFM_Segmentation.groupby('Segment').agg({'Monetary': 'sum'}).reset_index()

colors = ['#FF0000', '#00FFFF', '#FFFF00', '#A52A2A', '#800080', '#800000', '#00FF00', '#808000', '#FFC0CB', '#FFA500', '#FF00FF']

fig, ax = plt.subplots(1, figsize=(15, 8))

squarify.plot(sizes=grp_sales['Monetary'],
              label=grp_sales['Segment'],
              value=[f'{x*100/grp_sales["Monetary"].sum():.2f}%' for x in grp_sales['Monetary']],
              alpha=.8,
              color=colors,
              bar_kwargs=dict(linewidth=1.5, edgecolor="white"))

plt.title('RFM Segments by Total Sales', fontsize=16)
plt.axis('off')
plt.show()

"""##Bar plot"""

#Total Sales by Segmentation

sales_seg = RFM_Segmentation.groupby("Segment").agg(total_sales=("Monetary", "sum")).reset_index()
plt.figure(figsize=(12, 6))
plt.bar(sales_seg["Segment"], sales_seg["total_sales"], color='skyblue', edgecolor='black')

for i, v in enumerate(round(sales_seg["total_sales"], 2)):
    plt.text(i, v + 0.05 * max(sales_seg["total_sales"]), str(v), color='darkorange', fontweight='bold', ha='center', va='bottom')

plt.title('Total Sales by Segmentation', fontsize=16)
plt.xlabel('Segmentation', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()