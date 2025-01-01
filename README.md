## Python_RFM_Analysis: Customer Segmentation
### *Applying Python and the RFM model to analyze customer data, supporting market expansion planning and strategic product selection.*

#### You can view my analysis and recommendations on Google Colab using the link below:
[Open the notebook on Google Colab](https://colab.research.google.com/drive/1nj2g1ERs0GbQwXVqR42E_NyIbSgyOqF1)

### I. Introduction
### 1. RFM Analysis
- RFM method is a marketing analysis tool used to segment customers based on their purchasing behavior. It helps businesses identify and understand their most valuable customers and tailor marketing strategies accordingly.
  + Recency: Measures how recently a customer has made a purchase.
  + Frequency: Measures how often a customer makes purchases within a specific time frame.
  + Monetary Value: Measures the total amount a customer has spent during their relationship with the business.
- RFM analysis helps businesses identify high-value and at-risk customers, enabling them to prioritize retention efforts, launch targeted win-back campaigns, and improve decision-making and personalization through data-driven insights.

### 2. Business questions
- The Marketing department seeks to segment this year’s large customer base to run targeted campaigns but can no longer process the data manually as in previous years.
- They aim to thank loyal customers and identify potential ones who could become more engaged.
- The Marketing Director has proposed using the RFM model, and the Data Analytics team has been tasked with building an automated Python-based solution due to the dataset's scale.

### II. Progression
#### Data describe
![Screenshot 2024-12-23 112840](https://i.imgur.com/0Dw9LxD.png)

#### Data info
![Screenshot 2025-01-01 082521](https://i.imgur.com/lXZislV.png)

#### Segmentation table
![Screenshot 2025-01-01 085027](https://i.imgur.com/p8I8ohH.png)

- Since the focus is on analyzing customer segments, we need to remove data missing in the 'CustomerID' column. Additionally, to calculate available orders and using RFM method we will retain only positive values in the 'UnitPrice' and 'Quantity' columns.
- Applying the RFM method: calculate the R, F, and M scores for each customer and then develop a scoring framework based on a 1-to-5 scale. Using the statistical method of quintile analysis is recommended for this purpose.
- Combined with the segmentation table to distribute each customer with their status
  
#### RFM Score with Segmentation
![Screenshot 2025-01-01 085616](https://i.imgur.com/MQLFY0N.png)

### III. Visualization
#### Histogram: Distribution of Recency, Frequency and Moneytary
![Rececny](https://i.imgur.com/SylQWyu.png)
![Frequency](https://i.imgur.com/BmzhGqJ.png)
![Moneytary](https://i.imgur.com/TyfvP0E.png)
#### Treemap of Customer segment
#### Treemap of Total Sales
#### Bar plot of Total Profit by Segmentation
#### Bar plot of Total Sales by Segmentation



