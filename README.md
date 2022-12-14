# MA705 Final Project

Name: Lucenea Robinson\
Date: December 13, 2022

This repository contains files used in my MA705 dashboard project.


## Dashboard Description

***Motivating Question:** What's trending in the game industry?*

This dashboard summarizes information on games released (2015 to 2022)<sup>1</sup> to help identify potential year over year trends in regards to available genres, platforms and stores. 


### Data Sources

The data was sourced from RAWG.com, "the largest video game database and game discovery service," through their API service (RAWG, n.d.). RAWG provides a free API package that allows 20,000 calls per month. 

The data was collected over several days (12/2 - 12/9/2022) and store in the JSON format for later processing (18,941 files). This was mostly necessary due to the paginated structure of RAWG API calls, the complicated structure of JSON data (nested lists and dictionaries), and limited information in the documentation. Using the "get games" parameter, there was a max of 40 results per page and a max of 250 pages for the time period and/or the parameters specified (this was not listed in documentation). After a few testing starting with 2022, I decided to split a year into 10 day intervals and loop over each period to get all the results for a year (10 days had less than 250 pages). A single year was done at a time due to machine capabilities and network issues, that is, do not have to keep the machine on for long periods and keep watch constantly to restart calls when there is a bad response.


From the JSON files, relevant info including the game names, released date, genre, platforms, and ratings were extracted to a dataframe and saved to a csv. The unique platform, genre, tag, and store names were also extracted and saved to csvs for later use in filtering dataframes and for checklists. As for cleaning the dataframe, duplicates^2 and columns with little to no info were removed. Null values for the platforms, stores, genre, and tags were assumed to be "Other" based whether at least one of these variables had value. For example, there were 2160 Nulls for platforms, a quick look through a few of them yielded that the system was VR and so other seemed appropriate. Similar justifications were made for the other columns. There was only one game entry that had null for these four columns and was removed as a non-game entry. See "Games Data Cleaning" py file for more detail on cleaning. The final master dataframe was save to rawg_games_Final csv.

Unfortnuately, during deployment the file was too large and so a manually modifed (deleted columns only) version rawg_games_Final3 was created and used. This version only contains the day a game was released, the name of the game, and the 5 variables of interest (Platforms, Platform Types, Genres, Stores, and Tags).


**Sources:**

RAWG. (n.d). Explore RAWG video games database API • RAWG. • RAWG. Retrieved December 10, 2022, from https://rawg.io/apidocs 
RAWG. (n.d.). RAWG Video Games Database API (v1.0). Rawg Video Games Database API. Retrieved December 10, 2022, from https://api.rawg.io/docs/ 

*API Calls url*\
https://api.rawg.io/api/games

*Dash Package References*\
https://plotly.com/python/reference/layout/
https://dash.plotly.com/dash-core-components/dropdown
https://plotly.com/python/figure-labels/
https://dash.plotly.com/datatable
https://dash.plotly.com/datatable/interactivity
https://dash.plotly.com/datatable/width
https://dash.plotly.com/datatable
https://dash.plotly.com/datatable/reference
https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/table/
https://www.youtube.com/watch?v=1nEL0S8i2Wk
https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
https://stackoverflow.com/questions/68007438/r-how-to-stop-rounding-percentages-to-0-decimal-places-on-plotly-chart
https://community.plotly.com/t/datatable-how-to-scroll-x-horizontal/15604
https://community.plotly.com/t/how-to-wrap-text-in-cell-in-dash-table/15687/7


### Other Comments
1. 2022 has data up to December 2, 2022
2. Some duplicates were due to extra calls made for January 24, 2022 and February 11, 2022, which were due to page limit restrictions
3. Could not add JSON files due to large size of them (even after zipped) and need space to add my final master dataframe
4. User Discretion Advised: There are many games rated for mature audiences and so names may contain inappropriate language.

*Other Sources*
*Sources use to identify gaming system for less popular systems*\
https://www.amazon.com/Game-Gear-Sega-Portable-Video-System/dp/B00004YZAU
https://www.popularmechanics.com/technology/gadgets/a27437/amiga-2017-a1222-tabor/
https://www.walmart.com/ip/Sega-Genesis-Classic-Game-Console-with-81-Classic-Games-Built-in-Black-FB8280C/252082334
https://en.wikipedia.org/wiki/Neo_Geo_(system)
https://www.ebay.com/b/Atari-Jaguar-Video-Game-Consoles/139971/bn_77199498
https://www.dkoldies.com/dreamcast/ \
