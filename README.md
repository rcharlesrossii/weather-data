My wife and I currently live in Port Washington, WI, and plan on moving to Charlotte, NC, in late 2025.
I have been collecting weather data from both of these places as a way to continue the excitement about the move and monitor the better weather in Charlotte.
First, I needed to find a free weather API that had a considerable rate limit as a feasible way of running my script daily.
After looking around at different weather APIs, I settled on Weatherbit (www.weatherbit.io).
I needed to create an account, which allowed me to have an API key to make requests to.
After playing around with the API endpoints, I was able to get the desired information and implement my code and run it on a daily basis at 12 PM CST using GitHub Actions.
The second part of this project was finding a free host for my database.
I ended up choosing MongoDB as my database, as it has a very generous free tier and has some great features for this project.
With the utilization of MongoDB and its Charts feature, I have been able to create two databases and visualize the data I have been pulling.
If you are interested in seeing various data visualizations of these two places, please follow this URL:
https://charts.mongodb.com/charts-project-0-qnvswyz/dashboards/67d9bddd-64c1-46fd-887f-d9a30033d15d
