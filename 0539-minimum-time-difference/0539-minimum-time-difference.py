class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time_point):
            """Takes in a time in format "HH:MM",
            returns time in minutes from midnight""" 
            hrs = int(time_point[:2])
            mins = int(time_point[3:])

            return (hrs * 60) + mins

        # convert all times to num of minutes
        times_in_min = [convert_to_minutes(x) for x in timePoints]

        # sort the list in ascending order
        times_in_min.sort()

        # handle edge case: add 24 hours to the first time, in case it's closer to the last time. For example, 23:59 and 00:00 are only one minute apart, but when coverted to minutes, they seem very far apart (1439 and 0); adding 1440 to the smaller time (0) accounts for this "crossing midnight" (1439 and 1440 are correctly calculated as only one minute apart)
        times_in_min.append(times_in_min[0] + 1440)

        # set the min diff to larger than the max possible difference
        min_diff = 1441

        # iterate through the sorted times, comparing each pair to the current min
        for i in range(len(times_in_min) - 1):
            curr_time = times_in_min[i]
            next_time = times_in_min[i+1]

            min_diff = min(min_diff, next_time - curr_time)

        return min_diff
        