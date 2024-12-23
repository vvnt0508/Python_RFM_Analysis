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

### II. Progress
### Recommended approach:
- Define and calculate the R, F, and M scores for each customer. Note: The reference date for calculating the R score is 31/12/2017.
- Develop a scoring system with ratings from 1 to 5. Use the quintile method from statistics.
- Based on the classification table, group the customers accordingly.
- Visualize the number of segments with various data dimensions.
- Analyze the current status of the company and provide recommendations to the Marketing team.
- Suggest to the Marketing and Sales teams which of the three R, F, M metrics the Superstore retail model should focus on the most.

### Data describe
https://private-user-images.githubusercontent.com/189510500/398052605-509b2ef2-4356-40f2-8bda-3a43b5140fb3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQ5Mjg5MTUsIm5iZiI6MTczNDkyODYxNSwicGF0aCI6Ii8xODk1MTA1MDAvMzk4MDUyNjA1LTUwOWIyZWYyLTQzNTYtNDBmMi04YmRhLTNhNDNiNTE0MGZiMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjIzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIyM1QwNDM2NTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kOTJiMTlhOThkMzI1ZDBjM2NkYTVjNGJiNWNmZjg0MjBlYTIxMjEzYzczYTY0MzNkNjlhY2Q1ZDFkOTUwYzU4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.tgXG5Bi4Dwfmnc6qBHRV5P2vK0T954syeQjpQ6U9C1E

