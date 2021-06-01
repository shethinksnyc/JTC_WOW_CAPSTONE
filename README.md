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
1. combinding_raw_csv's
2. final_city_data
3. census_population_data
4. visualizations
5. plot_bugs
6. unit_testing

Each folder contains:
1. Readme.md file that specifies the contents of the folder.
2. CSV files used to create new data frames. Whether original Marshal Project CSV or one derived from them.
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
We began by importing the data that we would be using for our project. In the [1_combinding_raw_csv's](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/1%20combinding_raw_csv's) folder we isolated cities we needed, which were downloaded from the [Marshal Project](https://github.com/themarshallproject/police-settlements) in the form of CSV's. We then imported them in to our jupyter notebook located in the [complete_raw_city_data-source file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/1%20combinding_raw_csv's/complete_raw_city_data-source%20file). In this folder we dropped columns that we did not need; created a veriable from what was left; concatenated the dataframes and created a new CSV. see.[complete_raw_city-output file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/1%20combinding_raw_csv's/complete_raw_city-output%20file). The isolated CSV needed to run this notebook is contained in the [complete_raw_city_data-source file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/1%20combinding_raw_csv's/complete_raw_city_data-source%20file). The CSV can be created by running the notebook, but we also provided a copy in the [complete_raw_city-output file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/1%20combinding_raw_csv's/complete_raw_city-output%20file). Next in the [2_final_city_data](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/2%20final_city_data) file. Specifically in the [cleaned_city_data-source file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/2%20final_city_data/cleaned_city_data-source%20file) We cleaned the compleat_raw_cities.CSV and converted the data bases into a new CSV. see. [clean_city_data-output file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/2%20final_city_data/clean_city_data-output%20file). WE provided the  [complete_raw_city-output file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/1%20combinding_raw_csv's/complete_raw_city-output%20file) CSV to run the [cleaned_city_data-source file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/2%20final_city_data/cleaned_city_data-source%20file). The CSV that is contained within the [clean_city_data-output file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/2%20final_city_data/clean_city_data-output%20file) is provided but can be reproduced by running the [cleaned_city_data-source file](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/2%20final_city_data/cleaned_city_data-source%20file) notebook.  After completion of our city data, we then went on to clean census data that we imported from [Census Bureau](https://www.census.gov/) in the form of an Excel Spreadsheet. In the [census_population_data](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/census_population_data) folder. Specifically the [population.ipynb](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/3%20census_population_data/population.ipynb) folder. We read in a spreadsheet this time and once agian began deleting columns; assigining variables and converting the finished data in to a CSV. see. [population_data.csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/3%20census_population_data/population_data.csv). We provided a copy of the [population_data.csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/3%20census_population_data/population_data.csv) that was created, but one can be reproduced by running the [population.ipynb](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/3%20census_population_data/population.ipynb) notebook. Once our population data was cleaned and converted into csv's, we began plotting our data. Illustrated in the [visualizations](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/4%20visualizations) this was done by using seaborn, matplotlib, matplotlib.pyplot. We provided the [population_data.csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/3%20census_population_data/population_data.csv) and [clean_city_data.csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/2%20final_city_data/clean_city_data-output%20file/clean_city_data.csv) needed to run the notebook. And the images can be produced by running the notebook. Running into some issues with our visualization, some debugging was needed. see. [plot_bugs](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/plot_bugs). Seeing that the visualization was up and running, unit testing was the final step in making sure that our code was running efficently. see. [unit_testing](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/tree/main/unit_testing)


## The Result

![Scatter Plot](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/4_visualizations/PNG_output%20images/scatter_plot.png?raw=true)
# In this 'Scatter Plot' the individual amounts each city payed out between 2010 to 2020 was graphed side by side. This could be effective in showing, if there is a correlation between the years and amounts for each city. Also outliers can be easily identified. 

![Bar Plot](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/4_visualizations/PNG_output%20images/top_5_bar.png?raw=true)
# In this 'Bar Chart' the 5 highest paying cities were identified and graphed side by side. This could be effective in showing the payout differences even between the 5 highest paying cities.
![Line Chart](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/4_visualizations/PNG_output%20images/top_5_line.png?raw=true)
# In this 'Line Chart' the 5 highest paying cities were futher plotted and graphed from 2015 to 2019. This could be useful in identifying the trends of these cities over this time period. 
![Per Capita](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/4_visualizations/PNG_output%20images/per_capita.png?raw=true)
# In this 'Scatter Plot' the estemated per capita from 2010 to 2020 was graphed. Showing how much a city would essentualy pay each of its population per person. This could be useful in adding another personal dimension to the data



![](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/statement-of-solidarity.jpg?raw=true)

As the tide changes and America grapples with its tainted past we are at a critical moment, in order to shape an equitable society, we must be uncompromising in our stance against all forms of racial and social inequality. To communities of color and of every gender identity, we fight with you, we fight for you and we pledge to use our new skills to build and uplift our communities. 
