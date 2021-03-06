import operator
import re
import math


def calculate_string(str_to_calculate, str_operator):
    m = re.search(r'//\[(.*)]', str_to_calculate)
    str_without_pattern = re.search(r'(?<=]).*', str_to_calculate)
    op = get_operator(str_operator)
    numbers_list = str_without_pattern.group(0).split(str(m.group(1)))
    answer = int(numbers_list[0])

    if op is math.sqrt:
        for num in numbers_list[1:]:
            answer = operator.add(answer, int(num))
        answer = op(answer)
    else:
        for num in numbers_list[1:]:
            answer = op(answer, int(num))

    return answer


def get_operator(str_operator: str):
    return {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv,
        'square_root': math.sqrt
    }[str_operator.lower()]
