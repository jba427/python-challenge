# import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')



# initialize variables
totalvotes = 0
candidates = []
votes = []
votedict = {}
maxvotes = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # tally the total votes cast
        totalvotes += 1
        
        # create a list of the votes
        votes.append(row[2])

        # create a list of the candidates
        if row[2] not in candidates:
                candidates.append(row[2])
                
# populate dictionary with candidates and their votes
for candidate in votes:
    votedict[candidate] = votedict.get(candidate, 0) + 1

# Display results to screen
print ("Election Results")
print ("--------------------")
print ("Total Votes: " + str(totalvotes))
print ("--------------------")
for candidate in votedict:
    candidatepct = votedict[candidate]/totalvotes*100
    print (candidate + ": {0:<2,.3f}".format(candidatepct) + "% (" + str(votedict[candidate]) + ")")
    if votedict[candidate] > maxvotes:
        maxvotes = votedict[candidate]
        winner = candidate
print ("--------------------")
print ("Winner: " + winner)
print ("--------------------")

# Push the output to a text file
with open("election_results.txt", "w") as f:
    print ("Election Results", file=f)
    print ("--------------------", file=f)
    print ("Total Votes: " + str(totalvotes), file=f)
    print ("--------------------", file=f)
    for candidate in votedict:
        candidatepct = votedict[candidate]/totalvotes*100
        print (candidate + ": {0:<2,.3f}".format(candidatepct) + "% (" + str(votedict[candidate]) + ")", file=f)
        # if votedict[candidate] > maxvotes:
        #     maxvotes = votedict[candidate]
        #     winner = candidate
    print ("--------------------", file=f)
    print ("Winner: " + winner, file=f)
    print ("--------------------", file=f)



    
