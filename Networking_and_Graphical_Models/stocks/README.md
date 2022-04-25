
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

## stocks - Network Stock Portfolio Optimization
The approach towards this project was based of the ***Research Paper* on Quantitative Finance** - [Dynamic portfolio strategy using clustering approach](https://arxiv.org/pdf/1608.03058.pdf).

Active investing in the asset management industry aims to beat the stock market’s average returns and portfolio managers track a particular index and try to beat that index by creating their own portfolios.

Portfolio construction involves selection of stocks that have a higher probability of giving better returns in comparison to the tracking index, like S&P 500. In this project, we will use the concept of Network Analysis to select a basket of stocks and create two portfolios. We will then simulate portfolio value by investing a certain amount, keeping the portfolio for an entire year and we will then compare it against the S&P 500 index.

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
