import operator


def calculate_string(str_to_calculate, str_operator):
    op = get_operator(str_operator)
    numbers = str_to_calculate.split(",")
    answer = int(numbers[0])
    for num in numbers[1:]:
        temp = op(answer, int(num))
        answer = temp

    return answer


def get_operator(str_operator: str):
    return {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv,
        'square_root': operator.pow
    }[str_operator.lower()]
