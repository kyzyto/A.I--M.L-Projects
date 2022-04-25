# Networking and Graphical Models
### Main Languages
<p>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white"></p>

### Main Librarys and Modules
<p><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white">
<img src="https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white">
</p>

## GoT - Game of Thrones Network Analysis
Game of Thrones is a wildly popular television series by HBO, and I intend to analyze the co-occurrence network of the characters in the Game of Thrones books. It is important to note that if two characters are considered to co-occur if their names appear in the vicinity of 15 words from on another in the books.
-  Performed Descriptive analytics.
-  Ran Network Analysis Algorithms on individual books and combined.
-  Calculated the different centralities measures(i.e `degree`,`eigenvector`, and `betweenness`) and provide inference.
-  Created Network Graphs using Plotly to visualized each book.
-  Documented a summary of observations.
-  Ran `Louvain Community` Detection and found out different groups/communities in the data.
-  Discussed finding and results.
## caviar - Caviar Investigation Phases Case Study by the Royal Canadian Mounted Police
This project offered a rare opportunity to study a criminal network in upheaval by police forces.
-  Ran Network Analysis Algorithm
-  Generated and Visualized graphs.
-  Utilized and Visualized the centralities measures(i.e `degree`, `eigenvector`, `betweenness`, `closeness`).
-  Understand the variation of node importance across phases.
-  Documented comments and summary.
## enron - Enron Corp Network Analysis
Enron Corp was on of the biggest firms in USA and was delivering splendid performance  on the wall street. However, they declared bankruptcy and the Enron leadership was involved in one fo the biggest frauds and this particular fraud has been an area of interest for many **Research Scientists** and **Machine Learning Practioners**.
- Read data and understood the structure of the data.
- Put the data into a Graph.
- Identified the important nodes from the visualization
- Calculated the centrality measures and quantified the importance of;
    - `degree centrality`
    - `eigenvector centrality`
    - `closeness centrality`
    - `betweenness centrality`
- Discussed Observations and Discoveries.
## kalman - Tracking location and velocity of moving object in n-dimensional space
- **2-dimensional**<br>
  The only information available to us is the initial location (and velocity) and a series of noisy measurements of the velocity as the object moves in space. The key assumption of this problem is that the `true velocity of the object is known to be a constant`. However, the `constant velocity is not known to us`.
  -  Tracked the location (and velocity) of a moving object, e.g. a car, in a 2-dimensional space.
- **3-dimensional**<br>
  Factoring gravity to act on the ball and the intial position as well as the velocities are assumed to be known. Noisy location estimates would be used using a simulated sensor. 
  -  Tracked the location (and velocity) of a moving object, e.g. a ball, in a 3-dimensional space.
  -  Estimated the true location (and velocity) of the ball in 3D space.
## stocks - Network Stock Portfolio Optimization
The approach towards this project was based of the ***`Research Paper`*** on **Quantitative Finance** - [Dynamic portfolio strategy using clustering approach](https://arxiv.org/pdf/1608.03058.pdf).
-  Peformed data collection via web scraping and APIs.
-  Computed log returns
-  Computed correlation matrix for log returns
-  Find out the Top n central and peripheral stocks based on the following network topological parameters:
   - `Degree centrality`
   - `Betweenness centrality`
   - Distance on degree criterion
   - Distance on correlation criterion
   - Distance on distance criterion
-  Simulated the performance of central and peripheral portfolios against the performance of most resent period.
