## RFM_Customer_Segmentation
### *Applies the RFM model to segment SuperStore's customer data, enabling targeted marketing strategies by classifying customers based on their purchasing behavior and engagement.*

#### You can view my Python code, my analysis and recommendations on Google Colab using the link below:
[Open the notebook on Google Colab](https://colab.research.google.com/drive/1nj2g1ERs0GbQwXVqR42E_NyIbSgyOqF1)

### Overview:
- SuperStore is a global retail company with a large customer base.
- To celebrate Christmas and the New Year, the Marketing department wants to run marketing campaigns to thank customers for their continuous support and to identify potential customers who could become loyal ones.
- However, the Marketing department has not yet segmented this year’s customers due to the large dataset, which cannot be processed manually as in previous years. Therefore, they have asked the Data Analytics department to assist in developing a customer segmentation solution to implement targeted marketing campaigns for each customer group.
- The Marketing Director has proposed using the RFM (Recency, Frequency, Monetary) model. However, in the past, when the company was smaller, the team could handle this task using Excel. Given the current scale, with the vast amount of data, they now wish the Data department to build an automated Python-based segmentation process.

### Recommended approach:
- Prepare a dataset suitable for the RFM model.
- Define and calculate the R, F, and M scores for each customer. Note: The reference date for calculating the R score is 31/12/2017.
- Develop a scoring system with ratings from 1 to 5.
Suggestion: Use the quintile method from statistics.
- Based on the classification table, group the customers accordingly.
- Visualize the number of segments with various data dimensions.
- Analyze the current status of the company and provide recommendations to the Marketing team.
- Suggest to the Marketing and Sales teams which of the three R, F, M metrics the Superstore retail model should focus on the most.
