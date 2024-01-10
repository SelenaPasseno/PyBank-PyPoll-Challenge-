# PyPoll Challenge:
    
        #Create Python script that analyzes the records of the file   
            # The total number of votes cast (to all candidates)
            # A list of candidates who recieved votes
            # Each candidate's total votes 
            # Each candidate's percent of votes
            # Determine winner
            # Export (print) results to text file


#1 import OS and CSV Modules
import os   #OS module will allow us to create a file path across OSystems
import csv  #CSV moudule will allow us to import data into the CSV reader

#2 set the pathway for the file to be read using a relative pathway
election_data_csv_path = os.path.join(r"c:\\Users\\slpas\\PythonClass\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#3 set and intitalize the variable to be used with dataset - need to create a variable to count each row called total_votes and set to 0.
total_votes = 0
#set up an empty dictionary to hold the candidates and votes per candidate
candidate_votes = {}

#4 read in the csv file for manipulation of data and solving the problem set up a delimina
with open(election_data_csv_path, newline="") as csvfile:
   csv_reader = csv.reader(csvfile, delimiter=',') 
   
   #5 read the header row - skipping the first row in counting items which would create a counting error
   header = next(csv_reader)

   #6 read the first row after the header and loop through the rows using a for /if/else statement to count votes and create a library of candidates
   for row in csv_reader:  
      #Loop through data to count total vote count
      total_votes += 1  #short way of writing total_votes = total_votes +1 for each row
      #set up a dictionary of candidates and count votes using index 2
      if row [2] not in candidate_votes:
         candidate_votes[row[2]] = 1
      
      else:
         candidate_votes[row[2]] += 1  # short way of writing candidate_votes = candidate_votes +1

#7 print to the terminal for screen shot requirement - needed extensive work/rework for spacing to match assignment requirement         
print("\n")
print("Election Results" + "\n")
print("--------------------\n")
print("Total Votes: " +str(total_votes)+"\n")

print("--------------------\n")
#8 set up a way to count votes for each candidate, calculatae the % and use a string to list votes counted.  "\n" used for spacing purposes
for candidate, votes in candidate_votes.items():
   print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "  (" + str(votes)+")" + "\n")
print("--------------------\n")
#9 set variable for winner based on max calculation using key
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}"+ "\n")
#print("\n")
print("--------------------")


#10 set variable to save the file to a path
# output_path = os.path.join(r"C:\Users\slpas\PythonClass\python-challenge\PyPoll\Analysis\election_data.txt") - used shorter version used on PyBank successfully

#11 Print results to text_file and save to analysis folder
election_data = os.path.join("Analysis", "election_data.txt")
with open(election_data, "w") as text_file:
   text_file.write("Election Results \n")
   text_file.write("------------------------\n")
   
   text_file.write("Total Votes: " + str(total_votes)+"\n")
   
   text_file.write("------------------------\n")
   for candidate, votes in candidate_votes.items():
      text_file.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "  (" + str(votes)+")" +"\n")  
   text_file.write("------------------------\n")
   winner = max(candidate_votes, key=candidate_votes.get)
   text_file.write(f"Winner: {winner}"+ "\n")
   text_file.write("------------------------")

# Resources used was asking my son Eric Passeno who works as a Cyber Analyst and Python SME at Williams International.  He provided advice on how to search the internet 
# looking at code of simular exercises with the same premise of looping, compiling data and setting up text_files to show results.
# I also spent about 15 hours over break reworking class homework and reviewing Eric Matthes' 2nd Edition Python Crash Course.




