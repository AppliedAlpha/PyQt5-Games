import random
from itertools import combinations


def combination(arr, r):
    result = list(combinations(arr, r))
    return [list(element) for element in result]


def get_answers(blocks):
    answer = []
    arr = [i for i in range(9)]
    c = {"red": 1, "yellow": 2, "blue": 3}
    b = {"white": 1, "gray": 2, "black": 3}
    s = {"circle": 1, "triangle": 2, "square": 3}

    for item in combination(arr, 3):
        color_cnt = 0
        bg_cnt = 0
        shape_cnt = 0

        for idx in item:
            color_cnt += c[blocks[idx]["color"]]
            bg_cnt += b[blocks[idx]["background"]]
            shape_cnt += s[blocks[idx]["shape"]]

        if color_cnt % 3 == 0 and bg_cnt % 3 == 0 and shape_cnt % 3 == 0:
            answer.append(item)

    return answer


def generate_blocks():
    blocks = []
    color = {"red": (255, 0, 0), "yellow": (255, 255, 0), "blue": (0, 0, 255)}
    background = {"white": (255, 255, 255), "gray": (127, 127, 127), "black": (0, 0, 0)}
    shape = ["circle", "triangle", "square"]

    for _ in range(9):
        block = {
            "color": random.choice(list(color.keys())),
            "background": random.choice(list(background.keys())),
            "shape": random.choice(shape)
        }
        blocks.append(block)

    return blocks
