"""
Median is a numerical value separating the upper half of a sorted array of numbers from the lower half. In a list where there are an odd number of entities, the median is the number found in the middle of the array. If the array contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle. For this mission, you are given a non-empty array of natural numbers (X). 'With it, you must separate the upper half of the numbers from the lower half and find the median. 
"""

def median(lists):
    lists.sort()
    is_odd = False if len(lists) % 2 == 0 else True
    count = len(lists)

    if is_odd:
        return lists[count/2]
    else:
        mid = count/2
        avg = float(lists[mid] + lists[mid-1])/2
        return avg

print median([1, 2, 3, 4, 5]) == 3
print median([3, 1, 2, 5, 3]) == 3
print median([1, 300, 2, 200, 1]) == 2
print median([3, 6, 20, 99, 10, 15]) == 12.5

