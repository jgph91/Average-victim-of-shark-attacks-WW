# Data-cleaning-project "Sharks attacks"

The aim of this report is to create a profile of the average victim of a shark attack.The database used for this report its from kaggle "Global Shark Attack Incidents" (https://www.kaggle.com/teajay/global-shark-attacks/version/1). 

In order to develop the profile I have used to answer the following questions:

    - Does young people suffer most of the sharks attacks?
    - Are men more affected than women for this kind of attacks?
    - Is the USA the country with the highest number of sharks attacks?
    - Are most of the sharks attacks fatal for their victims?
    - Was the victim surfing when he/she was attacked?

The original data is included in a csv file in the input folder. Also the functions used for cleaning the data are included in the functions.py file stored in the src folder and the data cleaning is stores in the ipynb file "Sharksattacks".

Data study

First of all, only the following columns were taken to analyze: "Year", "Country", "Activity", "Sex", "Age" and "Fatal". Then I got the number of null values for each of these columns and the type of data each column stored.

For reliability purposes the data used for this investigation starts in 1900. In the case of the "Year" it wasn't neccessary to clean the data. The amount of data for 1900 to 2016 its 5323 rows.

Regarding the age it was needed to fill the na values with the "Unknown" label and to uniform the data using a function. There were some attacks where there were more than one victim, so it was necessary to get the man value of the age and insert it in the data frame. Also the data was changed to the int type in order to perform the required calculations. The three more common values were 17,18 and 20 years and the mean was 27,22 years, so we could confirm that young people suffer more sharks attacks than older people.

In the case of the "Sex" column it was required to rename the columns to erase the blank space at the end of the string. First, the na values were tag as "Unknown" and a categorizing function was applied to the data to group it by "M" for males and "F" for females and to ensure the categorization the set function was used.  4268 of the attacks were suffered by males whereas there were just 548 were the victims were females, so the hypothesis that mean are more affected for sharks attacks its confirmed.

About the country, a function was used to erase the blank spaces at the beginning and at the end of each value. The USA it's the most affected country by this kind of attacks with 1992 cases, then it follows with 1124 cases in Australia and the South Africa with 535 cases. It's confirmed that the USA is the country with the highest number of sharks attacks.

About the "Fatal" column the na values were tag as "Unknown" and a categorizing function was applied to the data to group it by "Y" for fatal attacks and "N" for non-fatal and to ensure the categorization the set function was used. 4036 attacks were non-fatal whereas 1203 were fatal, so it's not true that are most of the times fatal for the victims.

Regarding the activity which was performing the victim when she or she was attacked, the column was cleaned using regex function with the most common activities saw in the set of the column. The three most common activities are: surfing (1180), fishing (1180), and swimming (1020). So it's confirmed that surfing is the most common case.

Finally, a csv file with the cleaned data is included in the output folder.

Conclusion

The profile of average victim of a shark attack its a young male of 27 years old, attacked when he was surfing in the USA and he survived to the attack.
