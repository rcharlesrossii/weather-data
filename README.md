# Weather Comparison Tracker

A personal project that compares daily weather between **Port Washington, WI** (where I moved from) and **Charlotte, NC** (where I moved to). I built this to track how the climates differ over time and to get excited about the move by seeing the warmer weather in action.

---

## Project Overview

This project automatically collects weather data each day, stores it in a database, and creates visual comparisons between the two cities. It also sends fun Discord notifications when unusual or interesting weather events occur.

## Temperature Comparison Snapshots

### Charlotte Temperature Trends
![Charlotte Temperature](screenshots/charlotte_temperature.png)

### Port Washington Temperature Trends
![Port Washington Temperature](screenshots/port_washington_temperature.png)

## Live Dashboard

The interactive MongoDB Charts dashboard for this project can be viewed here:

**[View Live Weather Comparison Dashboard](https://charts.mongodb.com/charts-project-0-qnvswyz/dashboards/67d9bddd-64c1-46fd-887f-d9a30033d15d)**


### What It Does

- Pulls daily weather data from a public weather API  
- Stores historical records in **MongoDB**  
- Generates visualizations comparing both cities  
- Sends Discord alerts for events like:
  - Snow in Charlotte  
  - Charlotte having a colder current temperature than in Port Washington  
  - Port Washington having a warmer current temperature than in Charlotte  

---

## Technologies Used

- Python  
- Weather API  
- MongoDB  
- Data visualization tools  
- Discord webhooks  
- Scheduled automation  

---

## What I Learned

This project helped me practice:

- Working with external APIs  
- Building a simple automated data pipeline  
- Storing and querying data in MongoDB  
- Creating basic visualizations  
- Integrating software with Discord notifications  

---

## Future Ideas

- Add more cities for comparison  
- Build a small web dashboard  
- Track long-term trends and averages  
- Package the project for easier reuse  

---

This is a small and simple project, but it was a fun way to combine programming and data into my real-life move to a new city!
