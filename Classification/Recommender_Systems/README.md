# Recommendation Systems
It uses user/customer data (what user watches, what user buyes what music user listens to, what user uses, etc.) and finds patterns in that data and on the basis of these patterns provide personalized suggestions to improve user/customer experience.

![](https://www.mdpi.com/applsci/applsci-10-05510/article_deploy/html/images/applsci-10-05510-g001-550.jpg)
* Case-based filtering
* Adaptive filtering
* Rule-based filtering
* Content-based filtering
* Collaborative filtering (i.e clustering-based recommendation systems) - It includes user-based(user-user collaborative filtering) and item-based(item-item collaborative filtering)
  * user-based
    * Determing a list of users similar to a user **U**
    * Then calculate the rating **R** that **U** would give to a certain item **I**, which hasn't been rated.
    * Predict whether a user's rating **R** for an item **I** will be close to the average of the ratings given to **I** by the top 5 or top 10 users most  
      similar to **U**
  * item-based
    * Determing a list of items similar to a user **U**
    * Then calculate the rating **R** that **I** would recieve from certain user **U** who hasn't rated it.
    * Predict whether a item's rating **R** by a user **U** will be close to the average of the ratings recieved by **U** for the top 5 or top 10 items most 
      similar to **I**
