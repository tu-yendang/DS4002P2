# DS4002P2
Data Science Capstone Project 2 - The Best of Both Worlds: Former Disney Stars Turned Musicians

## Section 1: Software and Platform
* The primary software used for this project was Python, specifically using Interactive Python Notebook files (ipynb). These files were created and used with Google Colab. Additionally, data was read in as JSON files and were processed to be CSV files.
* The following packages were used:
    * json - read and manipulate JSON files
    * csv - read, write and manipulate CSV files
    * datetime - input standardized date format for data
* Three laptops were used, where two devices used Mac, while one was conducted on Windows.

## Section 2: Documentation Map
The follow is a map of our project's repository.
* DS4002P2 (main directory)
    * DATA - Folder
        * Artist CSV Data - Folder
            * Folder contains CSV files for each chosen former Disney Star. The chosen Disney stars were: Bridget Mendler, Demi Lovato, Dove Cameron, Jonas Brothers, Miley Cyrus, Ross Lynch, Selena Gomez, and Vanessa Hudgens
        * Raw JSON Data - Folder
            * Folder contains JSON files (raw data) for the same former Disney Stars.
        * monthly_listeners_final.csv (final data)
    * SCRIPTS - Folder
        * preprocessing.ipynb
        * analysis.ipynb
    * OUTPUT - Folder
        * monthly_listeners_scaled_time_plot.png
        * monthly_listeners_time_plot.png
        * numerical_statistical_results.csv
        * percent_change_bar_plot.png
    * LICENSE.md
    * README.md

## Section 3: Reproducing Results Instructions
In order to replicate this study, the user should:
1. Begin by familiarizing themselves with Disney original movies and TV shows that aired between the year 2006-2016.
2. A movie or TV show is considered popular if the premeire or episodes of the show appeared in the top 50 most viewed on Disney [2, 3]. Select 8 of the most popular movies and TV shows, then identify 8 actors from those selections who also pursued a music career.
3. After selecting a pool of artists, find each musician's Spotify data on "Song Stats" then select the graph depicting "Popularity and Monthly Listeners" [1]. To obtain the data used in this graph, inspect the website, refresh the page, and find the GET request under the 'Network' tab. This will provide a JSON file containing the specific artist's popularity and monthly listeners for a given date from 2021 to the day it was accessed.
4. Run each JSON file in the preprocessing notebook by changing the file path. Upload the JSON into a Python notebook with json, csv, and datetime imported. First convert the JSON into a csv using the preprocessing notebook. This will also clean the data to ensure only dates from 2021-present. Popularity will not be evaluated in this analysis so the data can be dropped. In addition, a column will be added to keep track of the artist's name. Individual artist csv data can be made, but a final monthly_listeners_final csv will be the only required one. 
4. Once all of the artist data has been downloaded, create a new Python notebook with pandas, numpy, and matplotlib.pyplot imported (running analysis notebook). Here plot the monthly listeners for each former Disney star between the years 2021-2024 in a multiline chart by creating a new dataframe for each artist in the final data set. Repeat the process, but this time transform the data by taking the logarithm of the monthly listeners for each artist to better visualize the less popular artists on the graph. This will provide a scaled chart for more readability
5. After creating the graphs, calculate the average, minimum, maximum, and percent change of monthly listeners for each artist. To calculate the percent change in monthly listeners from the first month to the latest month, subtract the number of monthly listeners in the first month from the number of monthly listeners in the latest month, then divide the difference by the first month's listeners, and then multiply the result by 100 to get the percentage.

 ## References:
 *any reference relevated to the code can  be found directly in the Python notebooks.*

[1] “Song Stats | Welcome”, SongStats, 2024. https://songstats.com/welcome (accessed Oct. 11, 2024)

[2] “Disney Channel’s Most-Watched Premieres”, Nickandmore!, 2023.
https://www.nickandmore.com/kids-tv-history/list-of-highest-rated-disney-channel-premieres/ (accessed Oct. 16, 2024)

[3] “List of the most viewed Disney Channel original series episodes”, Wikipedia, 2024.
https://en.wikipedia.org/wiki/List_of_the_most_viewed_Disney_Channel_original_series_episodes (accessed Oct. 16, 2024)

[4] “Percent Changes”, United States Census Bureau, 2015.
https://www2.census.gov/programs-surveys/acs/tech_docs/accuracy/percchg.pdf (accessed Oct. 17)

[5] "Convert JSON to CSV in Python", GeeksForGeeks, 2021. https://www.geeksforgeeks.org/convert-json-to-csv-in-python/ (accessed Oct. 19)
