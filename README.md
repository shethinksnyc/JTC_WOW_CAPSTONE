![Justice Through Code](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/jtc.jpg?raw=true)

# Justice Through Code Capstone Project

# Using Data Visualization 

For this project we collected data by using opensource software. We visually represent data that we collected. Data visualization is an effective way to provide information to viewers, in a way that makes it easy to identify and recognize trends and patterns. Data visualization gives the viewer a clear idea of the information that is being expressed in a concise and accessible format.

# The Issue 
While social and civil unrest have become a normal occurrence in the nation, deep flaws and divides over policing have been shoved into the spotlight. The financial impact that these issues cause is often overlooked. Our vision is to use data to shed light on the cost of police misconduct. 

# The Data

All police misconduct settlement data is from the [Marshal Project](https://github.com/themarshallproject/police-settlements) 

All population data is from [Census Bureau](https://www.census.gov/)

## Folder Structure
The folders:
1. census_population_data
2. final_city_data
3. visualizations
4. plot_bugs
5. city_data_clean
6. unit_testing

Each folder contains:
1. Readme.md file that specifies the contents of the folder.
2. Original CSV files used to create new data frames.
3. Jupyter Notebook files where data cleaning and analysis took place.
* The visualizations folder contains an additional folder with PNG files for viewing

## The Variables
Variable name | Definition
--------------| -----------------
calendar_year | Pulled from settlement date or closed_date
city | City name
state | State abbreviation
closed_date | Date at which settlement was reached OR paid (depending on what was provided)
amount_awarded | Amount awarded to claimant in the settlement
Census | All persons who are "usually resident" in a specified geographic area.
Estimates    | The population count or estimate used as the starting point in the estimates process.
2010-2019 | The population count for each individual year
yearly_incident | Police misconduct incident count per city 
total  | Total Police misconduct incident count per city from 2010-2019

# The Libraries
Library    | Usage 
---------|----------------------------------
Pandas  | An open source python package that is mostly used for data sicence
Seaborn | A data visualization library derived from matplotlib that provides the user with visiually appealing statistical graphics 
Matplotlib | A basic plotting library that consists of bars, pies, lines and scatter plots 

# The process 
We began by importing the data that we would be using for our project. As explained in the [city_clean_data](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/clean_city_data) the data we imported and used were from the [Marshal Project](https://github.com/themarshallproject/police-settlements) and were done so in the form of csv's. Next we combined the multiple csv's, cleaned the data and converted the data bases into a csv. see. [final_city_data](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/final_city_data). After completion of our city data, we then went on to clean census data that we imported from [Census Bureau](https://www.census.gov/) see. [census_population_data](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/census_population_data). Once our population data was cleaned and converted into csv's, we began plotting our data. Illustrated in the [visualizations](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/visualizations) this was done by using seaborn, matplotlib, matplotlib.pyplot. Running into some issues with our visualization, some debugging was needed. see. [plot_bugs](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/plot_bugs). Seeing that the visualization was up and running, unit testing was the final step in making sure that our code was running efficently. see. [unit_testing](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/unit_testing)


## The Result

![Scatter Plot](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/visualizations/PNG%20images/scatter_plot.png?raw=true)
![Bar Plot](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/visualizations/PNG%20images/top_5_bar.png?raw=true)
![Line Chart](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/visualizations/PNG%20images/top_5_line.png?raw=true)
![Per Capita](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/visualizations/PNG%20images/per_capita.png?raw=true)



![](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/statement-of-solidarity.jpg?raw=true)

As the tide changes and America grapples with its tainted past we are at a critical moment, in order to shape an equitable society, we must be uncompromising in our stance against all forms of racial and social inequality. We mourn each Black and Brown life lost to police violence and impacted by an unjust justice system. To all communities of color and of every gender identity, we fight with you, we fight for you and we pledge to use our new skills to build and uplift our communities. 