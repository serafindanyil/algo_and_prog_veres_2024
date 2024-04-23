def naive_method(haystack: str, needle: str):
    if haystack is None or needle is None:
        raise ValueError('Input string is None')
    elif len(needle) > len(haystack):
        raise ValueError('Needle should be smaller that Haystack')

    n, m = len(haystack), len(needle)

    needle_index = None
    count_compare = None

    for index in range(0, (n - m) + 1):

        for needle_compare_idx in range(0, m):
            if haystack[needle_compare_idx + index] != needle[needle_compare_idx]:
                break
            elif needle_compare_idx == (m - 1):
                needle_index = index
                count_compare = index + needle_compare_idx + 1
            else:
                continue

    return needle_index, count_compare
