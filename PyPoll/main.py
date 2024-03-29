# Import os module
import os
import csv

# Map file location
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Define total_votes and candidate_votes as variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv, improved reading using CSV module
with open(csvpath,newline="") as elections:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(elections,delimiter=",") 

# Skip header
header = next(csvreader)     

# Loop through each row in the csv
for row in csvreader: 

# Count unique Voter ID's, tally as total_votes
    total_votes +=1

# Define/Assign candidate names, tally assigned number of votes by candidate
# Designate numerator in percentage vote calculation
if row[2] == "Khan": 
    khan_votes +=1
elif row[2] == "Correy":
    correy_votes +=1
elif row[2] == "Li": 
    li_votes +=1
elif row[2] == "O'Tooley":
    otooley_votes +=1

 # Define candidate variable using a dictionary, define votes assigned to candiates 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Zip candidate and votes variables together to correlate the list of candidates(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Calculate vote percentage of total for each candidate
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print Statements
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Define Print Statements output file location
output_file = Path("Python-Challenge", "PyPoll", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

# Push/Write Printed Statements to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
