from operator import itemgetter
import ast
"""
 #  This program has the function MERGE, which takes a list of lists that represent intervals and merges all overlaping intervals
 #  into one and returning all merged intervals into an output file named output.txt.
 #  @author Leander van Diepen
 #  @license MIT
 #  @version 1.0
 #  @date 2/22/2021
"""


def MERGE(intervals):
    if len(intervals) < 1:
        print("Der übergebene Parameter intervals ist leer oder falsch formatiert. Stelle sicher, dass Daten in input.txt bereitgestellt und richtig formatiert ist.")
        return
# Sort the list by the value of the start of the interval
    intervals.sort(key=itemgetter(0))  # O(1)
# Create a list which holds the merged intervals
    nowMerged = []  # O(1)
# Append the first interval to the list
    nowMerged.append(intervals[0])  # O(1)

# Loop through all intervals
    for i in range(1, len(intervals)):  # O(n)
        # Check if the last interval in the list of nowMerged (the interval with which merges are still possible) is overlapping
        # with the interval currently inspecting
        # O(1)
        if nowMerged[-1][0] <= intervals[i][1] and nowMerged[-1][1] >= intervals[i][0]:
            # It is overlapping. Now check if upper bound of the new overlapping interval is higher, if so update the upper bound.
            if nowMerged[-1][1] < intervals[i][1]:  # O(1)
                nowMerged[-1][1] = intervals[i][1]  # O(1)
        else:  # O(1)
            # It is not overlapping. All posible merges with current interval are done. Append the new interval to the list, now
            # this interval will get merged accordingly.
            nowMerged.append(intervals[i])  # O(1)
# Return the List of merged intervals
    return nowMerged


def __main__():
    intervals = []
# Read intervals from input.txt with ';' as delimiter between intervals in format '[x,y]'
    inputs = open("input.txt", "r")
    for line in inputs:  # O(1)
        intervalsString = line.split(";")
        for interval in intervalsString: # O(n)
            intervals.append(ast.literal_eval(interval))
    inputs.close()

# Run function MERGE and do not declare output as variable to save space

# Write output to a file output.txt in the same format as the input.txt
    f = open('output.txt', 'w')
    for item in MERGE(intervals):  # O(n)
        print(item)
        f.write(str(item)+';')
    f.close()


__main__()
