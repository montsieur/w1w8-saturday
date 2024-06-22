import csv

total_goals = 0
with open('euro_cup_matches.csv','r') as file:
    content = csv.DictReader(file)
    for row in content:
        total_goals += int(row['Score A']) + int(row['Score B'])

print("Total Goals in the tournament so far: ", total_goals)


with open('euro_cup_matches.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    matches_above_3_goals = [row for row in csv_reader if int(row['Score A']) + int(row['Score B']) > 3]


fieldnames = ['Team A', 'Team B', 'Score A', 'Score B', 'Date']
with open('high_scoring_matches.csv', 'w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow(['Portugal', 'Spain', '1', '1', '2024-04-15'])
