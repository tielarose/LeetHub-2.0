class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert the times to minutes
        def convert_time_to_min(time_str):
            hours = int(time_str[:2])
            mins = int(time_str[3:])
            return (hours * 60) + mins

        times_list = [convert_time_to_min(x) for x in timePoints]

        # sort the list
        times_list.sort()

        # handle the edge case of times that cross midnight
        times_list.append((24 * 60) + times_list[0])
        
        # loop through the list, comparing times
        min_time = (24 * 60) + 1

        for i in range(len(times_list) - 1):
            curr_time = times_list[i]
            next_time = times_list[i + 1]

            min_time = min(min_time, next_time - curr_time)

        return min_time
