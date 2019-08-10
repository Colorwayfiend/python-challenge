import os
import csv

totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_reader = next(csvreader)

    for row in csvreader:
        totalVotes += 1
       # print(totalVotes)
        if row[2] == 'Khan':
            khanVotes += 1
        elif row[2] == 'Correy':
            correyVotes += 1
        elif row[2] == 'Li':
            liVotes += 1
        elif row[2] == 'O’Tooley':
            otooleyVotes += 1
# create a list
candidates = ['Khan', 'Correy', 'Li', 'O’Tooley']
votes = [khanVotes, correyVotes, liVotes, otooleyVotes]

# the purpose of zip is to map the similar index of multiple containers
# so they can be used just using as single entity
# max function to return the winner
dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Create percentages
khan_percent = (khanVotes/totalVotes)
correy_percent = (correyVotes/totalVotes)
li_percent = (liVotes/totalVotes)
otooley_percent = (otooleyVotes/totalVotes)

print(f"Election Results")
print(f"- ---------------------")
print(f"Total Votes: {totalVotes}")
print(f"- ---------------------")
print(f'Khan: {khan_percent: .3%} ({khanVotes})')
print(f'Correy: {correy_percent: .3%} ({correyVotes})')
print(f'Li: {li_percent: .3%} ({liVotes})')
print(f'O’Tooley: {otooley_percent: .3%} ({otooleyVotes})')
print(f"- ----------------------")
print(f"Winner: {key}")
print(f"- ----------------------")

f = open("Pypoll-output.txt", "w")
print("Election Results", file=f)
print(f"- ---------------------")
print(f"Total Votes: {totalVotes}", file=f)
print(f"- ---------------------")
print(f"Khan: {khan_percent: .3%} ({khanVotes})", file=f)
print(f"Correy: {correy_percent: .3%} ({correyVotes})", file=f)
print(f"Li: {li_percent: .3%} ({liVotes})", file=f)
print(f"O’Tooley: {otooley_percent: .3%} ({otooleyVotes})", file=f)
print(f"- ----------------------")
print(f"Winner: {key}", file=f)
f.close()
