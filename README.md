## Python_RFM_Analysis: Customer Segmentation
### *Applying Python and the RFM model to analyze customer data, supporting market expansion planning and strategic product selection.*

#### You can view my analysis and recommendations on Google Colab using the link below:
[RFM Analysis](https://colab.research.google.com/drive/1nj2g1ERs0GbQwXVqR42E_NyIbSgyOqF1)

### I. Introduction
#### 1. RFM Analysis
- RFM method is a marketing analysis tool used to segment customers based on their purchasing behavior. It helps businesses identify and understand their most valuable customers and tailor marketing strategies accordingly.
  + Recency: Measures how recently a customer has made a purchase.
  + Frequency: Measures how often a customer makes purchases within a specific time frame.
  + Monetary Value: Measures the total amount a customer has spent during their relationship with the business.
- RFM analysis helps businesses identify high-value and at-risk customers, enabling them to prioritize retention efforts, launch targeted win-back campaigns, and improve decision-making and personalization through data-driven insights.

#### 2. Business questions
- The Marketing department seeks to segment this year’s large customer base to run targeted campaigns but can no longer process the data manually as in previous years.
- They aim to thank loyal customers and identify potential ones who could become more engaged.
- The Marketing Director has proposed using the RFM model, and the Data Analytics team has been tasked with building an automated Python-based solution due to the dataset's scale.

### II. Progression
#### Data describe
![datadescribe](https://i.imgur.com/0Dw9LxD.png)

#### Data info
![datainfo](https://i.imgur.com/lXZislV.png)

#### Segmentation table
![segmentable](https://i.imgur.com/p8I8ohH.png)

- Since the focus is on analyzing customer segments, we need to remove data missing in the 'CustomerID' column. Additionally, to calculate available orders and using RFM method we will retain only positive values in the 'UnitPrice' and 'Quantity' columns.
- Applying the RFM method: calculate the R, F, and M scores for each customer and then develop a scoring framework based on a 1-to-5 scale. Using the statistical method of quintile analysis is recommended for this purpose.
- Combine the segmentation table with the customer data to assign each customer their status
  
#### RFM Score with Segmentation
![Screenshot 2025-01-01 085616](https://i.imgur.com/MQLFY0N.png)

### III. Visualization
- Histogram: Distribution of Recency, Frequency and Monetary
![Rececny](https://i.imgur.com/SylQWyu.png)
![Frequency](https://i.imgur.com/BmzhGqJ.png)
![Monetary](https://i.imgur.com/TyfvP0E.png)

- Treemap of Customer Segment
![Customer](https://i.imgur.com/tyTtDIU.png)

- Treemap of Total Sales
![totalsaletreemap](https://i.imgur.com/LhZtEv4.png)

- Bar plot of Total Profit by Segmentation
![totalprofitbarplot](https://i.imgur.com/hfwCq6b.png)

- Bar plot of Total Sales by Segmentation
![totalsalesbarplot](https://i.imgur.com/gXCbvZe.png)

### IV.Insights
1. Among three index R, F, M that the company needs to pay attention to, (R) should be the immediate focus because the company has a total of 32.39% of customers in the At Risk (9.87%), Hibernating (16%), and About to Sleep (6.52%) categories, low purchase frequency indicates these segments are at high risk of churn, significantly impacting revenue.
2. Loyal Customers (9.80%) are crucial but small, under 10% of the base. Potential Loyalists (9.50%) also make up a similar share but don't buy regularly. Promising (3.14%) and Need Attention (6.41%) groups have potential for higher frequency with the right strategies => index (F) should be the next focus, this needs improvement to ensure sustained growth.
3. Most customers spend very little (under 50,000 USD).
4. Champions (19.20%) drive 62.85% of total sales, while Loyal (11.40%) and Potential Loyalists (2.53%) contribute a valuable share of revenue. The focus should be on boosting spending from low-value, high-frequency segments through targeted promotions or premium bundles to increase overall revenue.

### V.Recommendations for Marketing and Sales Team




