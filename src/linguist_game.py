def read_input_data_from_file(path_to_file: str):
    """
    The function parses the data by variables

    Args:
        path_to_file: The path to the input data

    Returns:
        count_words: The all values in list

    Raises:
        FileNotFoundError: The file is not found in currently path
        ValueError: The value is not corrected
    """
    try:
        with open(path_to_file, 'r') as file:
            count_words = int(file.readline())
            words_list = list(file.readline().strip('\n') for _ in range(count_words))
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found")
    except ValueError:
        raise ValueError('Value is not corrected')

    file.close()
    return count_words, words_list


def string_of_words(input_words_list: list, count_words: str):
    """
        The function find string of words

        Args:
            input_words_list: The list of words

        Returns:
            max_length: The maximum legnth of sting of words (int)
        """
    sorted_words_list = sorted(input_words_list, key=len, reverse=True)

    max_cross_letter = 1
    memoized = set(sorted_words_list[count_words - 1])
    max_length = 1

    def recursion(n):
        nonlocal max_length
        if n == 0:
            return max_length
        elif len(set(sorted_words_list[n - 1]).difference(memoized)) == max_cross_letter:
            memoized.update(sorted_words_list[n - 1])
            max_length += 1
        return recursion(n - 1)

    return recursion(count_words)


def write_output_data_to_file(path: str, max_lenght: int):
    """
        The function write output data to file

        Args:
            path: The path to output file
            max_lenght: The value than should be write to file
        """
    file = open(path, 'w')
    file.write(str(max_lenght))
    file.close()
