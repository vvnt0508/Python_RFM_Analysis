## Python: RFM Analysis: Customer Segmentation
#### You can also view my analysis and recommendations on Google Colab using the link below:
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

- Bar plot of Total Sales by Segmentation
![totalsalesbarplot](https://i.imgur.com/gXCbvZe.png)

### IV. Insights
- Among the three indexes R, F, and M, Recency (R) should be the immediate focus, as 32.39% of customers fall into At Risk (9.87%), Hibernating (16%), and About to Sleep (6.52%) categories. These groups pose a high risk of churn, which could significantly impact revenue.
- Frequency (F) insights show that Loyal (9.80%, $1,015,513.33), Potential Loyalists (9.50%, $225,247.60), Promising (3.14%, $121,031.35), and Need Attention (6.41%, $461,077.53) collectively hold significant growth potential. Increasing purchase frequency within these groups is critical to driving sustained revenue growth.
- Monetary (M) analysis highlights that Champions (19.20%) generate 62.85% of total sales ($5,600,439.80), while Loyal (11.40%, $1,015,513.33) and Potential Loyalists (2.53%, $225,247.60) also contribute meaningfully.
- In contrast, Hibernating customers, making up 16% of the base, account for only 3.20% of total sales ($285,314.97), indicating low engagement.
- Smaller but impactful segments like Cannot Lose Them (2.30%, $205,324.72) and At Risk (8.55%, $761,560.87) contribute disproportionately high sales, emphasizing the importance of retention strategies for these groups.

### V. Recommendations
- Launch re-engagement campaigns for At Risk and Hibernating customers with discounts, loyalty rewards, or free shipping.
- Increase purchase frequency in Promising and Need Attention segments by offering personalized product bundles and subscription plans.
- Reward high-value segments (Champions, Loyal) with exclusive benefits like early access to sales, VIP programs, or recognition gifts.
- Improve retention strategies for Cannot Lose Them customers by addressing potential churn factors with tailored outreach.
- Strengthen the company’s data infrastructure to enable real-time tracking of RFM metrics for better decision-making.
- Align efforts across departments to deliver consistent and engaging customer experiences, reducing churn and driving revenue growth.





