input_table = [
    [1, "Soumita M", "Winning Culture Lab", 280],
    [2, "Subhangi 0", "Winning Culture Lab", 75],
    [3, "Nitin Shane", "Winning Culture Lab", 1124],
    [4, "Merwin", "Mentor", 295],
    [5, "fardinkamal62", "Human Capital Lab", 263],
    [6, "_riddhi_213", "Human Capital Lab", 504],
    [7, "Rohit Dutta", "Mentor", 266],
    [8, "imshawan", "Tech Lab", 71],
    [9, "Anuraj_Saini", "BrandTech Lab", 342],
    [10, "sharath", "Student Unicorn Lab", 3367],
    [11, "Ronak 0", "Tech Lab", 302],
    [12, "Amrit Malviya", "Brandtech Lab", 336],
    [13, "Saurabh", "Mentor", 271],
    [14, "darshimalde", "Student Unicorn Lab", 3169],
    [15, "Shagun", "Tech Lab", 100],
    [16, "Ayisha", "Student Unicorn Lab", 3406],
    [17, "Palash", "Growpital", 69],
    [18, "raman", "Growpital", 539],
    [19, "Nishant", "Growpital", 299],
    [20, "Vatsal", "Kringle", 3408],
    [21, "devmenkr", "Kringle", 360]
]

team_data = {}
for row in input_table:
    team = row[2]
    if team not in team_data:
        team_data[team] = {"statements": [], "reasons": []}
    team_data[team]["statements"].append(row[0])
    team_data[team]["reasons"].append(row[3])

leaderboard = []
rank = 1
for team, data in sorted(team_data.items(), key=lambda x: sum(x[1]["reasons"]), reverse=True):
    avg_statements = sum(data["statements"]) / len(data["statements"])
    avg_reasons = sum(data["reasons"]) / len(data["reasons"])
    leaderboard.append([rank, team, avg_statements, avg_reasons])
    rank += 1

print("{:^15}{:^30}{:^20}{:^20}".format("Team Rank",
      "Thinking Teams Leaderboard", "Average Statements", "Average Reasons"))
for row in leaderboard:
    print("{:^15}{:^30}{:^20.2f}{:^20.2f}".format(*row))
