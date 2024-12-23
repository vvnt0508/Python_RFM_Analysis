## Python_RFM_Analysis: Customer Segmentation
### *Applying Python and the RFM model to analyze customer data, supporting market expansion planning and strategic product selection.*

#### You can view my analysis and recommendations on Google Colab using the link below:
[Open the notebook on Google Colab](https://colab.research.google.com/drive/1nj2g1ERs0GbQwXVqR42E_NyIbSgyOqF1)

### I. Introduction
### 1. RFM Analysis
- RFM method is a marketing analysis tool used to segment customers based on their purchasing behavior. It helps businesses identify and understand their most valuable customers and tailor marketing strategies accordingly.
  + Recency: Measures how recently a customer has made a purchase. Customers who bought recently are more likely to purchase again compared to those who haven’t bought in a while.
  + Frequency: Measures how often a customer makes purchases within a specific time frame. Customers who buy frequently are considered more loyal.
  + Monetary Value: Measures the total amount a customer has spent during their relationship with the business. High monetary values indicate high-value customers.
- RFM analysis helps businesses identify high-value and at-risk customers, enabling them to prioritize retention efforts, launch targeted win-back campaigns, and improve decision-making and personalization through data-driven insights.

### 2. Business questions
- The Marketing department seeks to segment this year’s large customer base to run targeted campaigns but can no longer process the data manually as in previous years.
- They aim to thank loyal customers and identify potential ones who could become more engaged.
- The Marketing Director has proposed using the RFM model, and the Data Analytics team has been tasked with building an automated Python-based solution due to the dataset's scale.

### Recommended approach:
- Prepare a dataset suitable for the RFM model.
- Define and calculate the R, F, and M scores for each customer. Note: The reference date for calculating the R score is 31/12/2017.
- Develop a scoring system with ratings from 1 to 5.
Suggestion: Use the quintile method from statistics.
- Based on the classification table, group the customers accordingly.
- Visualize the number of segments with various data dimensions.
- Analyze the current status of the company and provide recommendations to the Marketing team.
- Suggest to the Marketing and Sales teams which of the three R, F, M metrics the Superstore retail model should focus on the most.
