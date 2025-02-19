from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for d in data:
        if 'name' in d:
            d['name'] = d['name'].capitalize()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for d in data:
        if isinstance(redundant_keys, list):
            for key in redundant_keys:
                if key in d:
                    del d[key]
        elif isinstance(redundant_keys, str):
            if redundant_keys in d:
                del d[redundant_keys]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    found_d = []
    for d in data:
        if value in d.values():
            found_d.append(d)
    return found_d


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    if data:
        return min(data)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """
    shortest_str = None
    for item in data:
        if isinstance(item, int):
            item = str(item)
        if not shortest_str or len(item) < len(shortest_str):
            shortest_str = item
    return shortest_str


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    min_value = None
    min_d = None
    for d in data:
        if key in d:
            if not min_value or d[key] < min_value:
                min_value = d[key]
                min_d = d
    return min_d


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    max_value = None
    for l in data:
        if l:
            cur_max = max(l)
            if not max_value or max_value < cur_max:
                max_value = cur_max
    return max_value


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    sum_items = 0
    for item in data:
        sum_items += item
    return sum_items


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    sum_items = 0
    for item in text:
        sum_items += ord(item)
    return sum_items


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    for simple_numbers in range(2, 200):
        is_simple = True
        for num in range(2, simple_numbers):
            if simple_numbers % num == 0:
                is_simple = False
                break
        if is_simple:
            yield simple_numbers
