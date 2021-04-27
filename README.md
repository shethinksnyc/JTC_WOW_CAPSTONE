<<<<<<< HEAD
![Justice Through Code](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/jtc.png?raw=true)

# Justice Through Code capstone project

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
1. We began by importing the csv's 
![read_csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/read_csv.png?raw=true)
2. We then began dropping data that we did not need 
![drop_columns](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/drop_columns.png?raw=true)
3. then we converting datatypes to get clean outputs 
4. next we combined that dataframes to a veriable, then concatenated the variable 
![combinding_and_concatenating](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/concat.png?raw=true)
5. To compleat the city data we converted the data frame in to a csv 
![converting_dataframe_csv](https://github.com/shethinksnyc/JTC_WOW_CAPSTONE/blob/main/readme_img/to_csv.png?raw=true)
=======
# JTC_WOW_CAPSTONE
## Justice Through Code capstone project
#### 

**_This text will be 

![carbon (1)](https://user-images.githubusercontent.com/78012387/115937432-073d2800-a466-11eb-9211-3133c74b83fc.png)

anything 
>>>>>>> city_data_clean
