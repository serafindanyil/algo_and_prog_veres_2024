"""
Lab 2 Variant 3
"""
from gorillaz_jacky import jacky_min_eating_speed


def main():
    piles = [3, 6, 7, 11]
    h = 8
    result = jacky_min_eating_speed(piles, h)
    print(result)


if __name__ == "__main__":
    main()