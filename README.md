# Data Collection & Visualization
This repository contains the front-end and back-end portion of a four-person project. The project was done over the course of a week during Tech Safari. There are two primary parts to the project, which will be discussed below.  

### 1. Collecting Environmental Data & Tracking Our Own Tracks 
Code related to this portion of the project is written using Arduino. James Deromedi built and designed a device that would collect data regarding the environment around us prior to the start of the trip. More information regarding this portion of the project can be found on a different repository on Bitbucket. The rationale for collecting this data is that San Francisco and the surrounding areas act as 'micro-climates,' due to the hills, mountains, oceans, and the bay nearby. This information would be collected during Tech Safari. The data is pushed into a text file which can be accessed later. Additionally, James also created a device that connects to a satellite so that we could collect information regarding our location. 

Data is collected every 7 seconds after the 14th of March. Prior to that, data was collected based on whether we were driving or walking based on a hypothesis previously discussed: is there a difference in data collection based on mode of transportation. (The answer is no.) 

### 2. Documenting Our Time in the Bay Area & Silicon Valley 
Along with data, we also tried to be viligant about taking pictures and videos of our time here on the west coast. Just text is no fun, especially when our project is meant to be visual-leaning.  

### 3. Visualizing the Data  
But what to do with all this data? You visualize it (and maybe tell a story in the process). The data that is collected per day would then be cleaned and pushed into a CSV file. Our system relies solely on a webpage and a flat file database. 

## Our Stack 
The firmware was done using Arduino. More information about the hardware can be found on the Bitbucket. 

Data was cleaned and processed using Python. We relied primarily on vanilla JavaScript combined with Leaflet.JS. 

## How to Get Started 
Make sure to ```git clone``` or have a local copy of the repository on your machine. We relied primarily on Python's simple server to start a local instance up and running on our side. You can do this by typing the following: 

Python 2.7: ```python -m SimpleHTTPServer``` 
Python 3: ```python -m http.server```

## Developers 
* James Deromedi (hardware/firmware) 
* Cedric Hermel (front-end/back-end)
* Dong Zhou (back-end)
* Yan Shi (front-end)