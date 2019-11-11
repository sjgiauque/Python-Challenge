# Python-Challenge

PyBank

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Dateand Profit/Losses. 

Your task is to create a Python script that analyzes the records to calculate each of the following:
•	The total number of months included in the dataset
•	The net total amount of "Profit/Losses" over the entire period
•	The average of the changes in "Profit/Losses" over the entire period
•	The greatest increase in profits (date and amount) over the entire period
•	The greatest decrease in losses (date and amount) over the entire period



PyPoll

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.  You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 

Your task is to create a Python script that analyzes the votes and calculates each of the following:
•	The total number of votes cast
•	A complete list of candidates who received votes
•	The percentage of votes each candidate won
•	The total number of votes each candidate won
•	The winner of the election based on popular vote.



PyBoss – BONUS

In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.  Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. 

Your script will need to do the following:
•	Import the employee_data.csvfile, which currently holds employee records like the below:



Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania


•	Then convert and export the data to use the following format instead:



Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA


•	In summary, the required conversions are as follows:



o	The Namecolumn should be split into separate First Nameand Last Namecolumns.
o	The DOBdata should be re-written into MM/DD/YYYYformat.
o	The SSNdata should be re-written such that the first five numbers are hidden from view.
o	The Statedata should be re-written as simple two-letter abbreviations.



PyParagraph – BONUS

In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:
•	Import a text file filled with a paragraph of your choosing.
•	Assess the passage for each of the following:
o	Approximate word count
o	Approximate sentence count
o	Approximate letter count (per word)
o	Average sentence length (in words)


