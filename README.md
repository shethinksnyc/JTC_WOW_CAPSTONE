![Justice Through Code](jtc-1.jpg)


#  JTC_WOW_CAPSTONE
### Justice Through Code capstone project


# Using Data Visualization 

For this project we collected data through csv’s, by using opensource software we visually represent data that we collected. Data visualization is an effective way to provide information to viewers, in a way that makes it easy to identify and recognize trends and patterns. Data visualization gives the viewer a clear idea of the information that is being expressed, in a relatively shorter and easier mental format to digest.

# The Issue 
While social and civil unrest have become a normal occurrence in the nation, deep flaws and divides over policing have been shoved into the spotlight. But the financial impact that these social issues has caused, has not seemed to receive the same lighting.

Making data visualization more effective than looking through hundreds and even thousands of rows on a spreadsheet.

# The Data

All police misconduct settlement data is from the [Marshal Project](https://github.com/themarshallproject/police-settlements) 

All population data is from [Census Bureau](https://www.census.gov/)

## Folder Structure
The folders:
1. census_population_data
2. final_city_data
3. visualizations
4. plot_bugs

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
Libraries names | Usage 
---------|----------------------------------
Pandas  | An open source python package that is mostly used for data sicence
Seaborn | A data visualization library derived from matplotlib that provides the user with visiually appealing statistical graphics 
Matplotlib | A basic plotting library that consists of bars, pies, lines and scatter plots 

# The process 
We began by importing the csv's 
![read_csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/read_csv.png?raw=true)