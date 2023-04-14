table = [
    ["S No", "name", "uid", "total_statements", "total_reasons"],
    [1, "Soumita M", 280, 13, 21],
    [2, "Subhangi 0", 75, 13, 16],
    [3, "Nitin Shane", 1124, 12, 11],
    [4, "Merwin", 295, 13, 12],
    [5, "fardinkamal62", 263, 2, 2],
    [6, "_riddhi_213", 504, 2, 7],
    [7, "Rohit Dutta", 266, 3, 3],
    [8, "imshawan", 71, 9, 9],
    [9, "Anuraj_Saini", 342, 7, 7],
    [10, "sharath", 3367, 8, 8],
    [11, "Ronak 0", 302, 16, 19],
    [12, "Amrit Malviya", 336, 2, 4],
    [13, "Saurabh", 271, 6, 8],
    [14, "darshimalde", 3169, 3, 3],
    [15, "Shagun", 100, 2, 2],
    [16, "Ayisha", 3406, 11, 8],
    [17, "Palash", 69, 6, 7],
    [18, "raman", 539, 5, 5],
    [19, "Nishant", 299, 4, 5],
    [20, "Vatsal", 3408, 2, 2],
    [21, "devmenkr", 360, 7, 7],
]

# sort the table based on the number of statements and reasons in descending order
sorted_table = sorted(table[1:], key=lambda x: (x[3], x[4]), reverse=True)

# create a leaderboard table
leaderboard = [["Rank", "Name", "UID", "No. of Statements", "No. of Reasons"]]
for i, row in enumerate(sorted_table):
    leaderboard.append([i+1, row[1], row[2], row[3], row[4]])

# print the leaderboard table
for row in leaderboard:
    print("{:<5}{:<15}{:<10}{:<20}{:<20}".format(*row))
