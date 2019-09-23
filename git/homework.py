from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    return id(first) == id(second)


def multiple_ints(first_value: int, second_value: int) -> int:
    if isinstance(first_value, int) and isinstance(second_value, int):
        return first_value * second_value
    else:
        raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        first_value = int(first_value)
        second_value = int(second_value)
        return first_value * second_value
    except TypeError:
        raise ValueError


def is_word_in_text(word: str, text: str) -> bool:
    return word in text.split()


def some_loop_exercise() -> list:
    list1 = []
    for i in range(13):
        if i < 6 or i > 7:
            list1.append(i)
    return list1


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    list1 = []
    for i in data:
        if i > 0:
            list1.append(i)
    return list1


def alphabet() -> dict:
    dict1 = {}
    for i in range(97, 123):
        dict1[i-96] = chr(i)
    return dict1


def simple_sort(data: List[int]) -> List[list]:
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                tmp = data[j+1]
                data[j+1] = data[j]
                data[j] = tmp
    return data

