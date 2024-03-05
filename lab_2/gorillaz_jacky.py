"""
Gorillaz Jacky
"""


def jacky_min_eating_speed(piles, hours):

    def validator():
        n = len(piles)
        if not piles:
            raise ValueError(f'Array piles is empty: {n}')
        if hours < n:
            raise ValueError(f'Count piles is greater from hours: {hours} < {n}')

    def maximum(arr):
        max_value = 0
        for x in arr:
            if x > max_value:
                max_value = x
        return max_value

    def jacky_can(speed):
        result = 0
        for pile in piles:
            result += (pile + speed - 1) // speed
        return result <= hours

    validator()

    left, right = 1, maximum(piles)
    while left < right:
        mid = (left + right) // 2
        if jacky_can(mid):
            right = mid
        else:
            left = mid + 1
    return left
