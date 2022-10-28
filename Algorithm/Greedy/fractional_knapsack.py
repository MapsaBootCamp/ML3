from typing import List, Tuple, Dict

items = [(2, 10), (4, 15), (8, 4)]

def fractional_knapsack(items: List[Tuple], capacity: int) -> Dict[Tuple, float]:

    sorted_density: List[Tuple] = []
    result: Dict[Tuple, float] = {}

    for indx, elm in enumerate(items):
        assert elm[1] != 0, "vazn bayad vozorgtar az sefr bashe"
        # if elm[1] == 0:
        #     raise Exception("vazn bayad vozorgtar az sefr bashe")

        sorted_density.append((indx, elm[0] / elm[1]))
    sorted_density.sort(key=lambda x : x[1], reverse=True)
    for index, _ in sorted_density:
        if capacity == 0:
            break
        elif capacity >= items[index][1]:
            result[items[index]] = 1
            capacity -= items[index][1]
        else:
            result[items[index]] = capacity / items[index][1]
            break
    return result

print(fractional_knapsack(items, 2))
