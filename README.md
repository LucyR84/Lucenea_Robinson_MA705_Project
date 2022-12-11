# MA705 Final Project

Name: Lucenea Robinson\
Date: December 13, 2022

This repository contains files used in my MA705 dashboard project.


## Dashboard Description

***Motivating Question:** How are games trending over time?*

This dashboard seeks to identify trends in the gaming industry by looking at data for games released from 2015 to 2022 (12/02/2022).


### Data Sources

The data was sourced from RAWG.com, "the largest video game database and game discovery service," through their API service (RAWG, n.d.). RAWG provides a free API package that allows 20,000 calls per month. 

The data was collected over several days and store in the JSON format for later processing (18,941 files). This was mostly necessary due to the paginated structure of RAWG API calls, the complicated structure of JSON data (nested lists and dictionaries), and limited information in the documentation. Using the "get games" parameter, there was a max of 40 results per page and a max of 250 pages for the time period and/or the parameters specified (this was not listed in documentation). After a few testing starting with 2022, I decided to split a year into 10 day intervals and loop over each period to get all the results for a year (10 days had less than 250 pages). A single year was done at a time due to machine capabilities and network issues, that is, do not have to keep the machine on for long periods and keep watch constantly to restart calls when there is a bad response.


From the JSON files, relevant info including the game names, released date, genre, platforms, and ratings were extracted to a dataframe and saved to a csv. The unique platform, genre, tag, and store names were also extracted for later use in filtering data frame and for checklists. As for cleaning the data frame, duplicates created due to extra calls from reaching page limit were removed.^1^ This dataframe contained all the total games released each year (including initial releases). From this, another dataframe was created with **TBD**

**Sources:**

RAWG. (n.d). Explore RAWG video games database API • RAWG. • RAWG. Retrieved December 10, 2022, from https://rawg.io/apidocs 

RAWG. (n.d.). RAWG Video Games Database API (v1.0). Rawg Video Games Database API. Retrieved December 10, 2022, from https://api.rawg.io/docs/ 


### Other Comments
1. Extra calls were made for January 24, 2022 and February 11, 2022.
2. Folders with JSON files are zipped due to size #####ASK Prof if needed####
3. User Discretion Advised: There are many games rated for mature audiences and so names may contain inappropriate language.
