from operator import itemgetter

"""
 #  Gets intervals as input and merges all overlapping intervals into one and returns the new list of intervals.
 #  @param intervals The input list of intervals as a two-dimensional integer array.
 #  @return a two dimensional array consisting of the merged intervals
"""

def MERGE(intervals):
## Sort the list by the value of the start of the interval
    intervals.sort(key=itemgetter(0))
## Create a list which holds the merged intervals
    toUpdate = []
## Append the first interval to the list
    toUpdate.append(intervals[0])

## Loop through all intervals
    for i in range(1,len(intervals)):
    ## Check if the last interval in the list of toUpdate (the interval with which merges are still possible) is overlapping with the interval currently inspecting
        if toUpdate[-1][0] <= intervals[i][1] and toUpdate[-1][1] >= intervals[i][0]:
        ## It is overlapping. Now check if upper bound of the new overlapping interval is higher, if so update the upper bound.
            if toUpdate[-1][1] < intervals[i][1]:
              toUpdate[-1][1] = intervals[i][1]
        else:
        ## It is not overlapping. All posible merges with current interval are done. Append the new interval to the list, now
        ## this interval will get merged accordingly.
          toUpdate.append(intervals[i])
## Return the List of 
    return toUpdate