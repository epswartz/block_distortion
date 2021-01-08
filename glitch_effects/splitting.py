import numpy as np
from heapq import heappush, heappop

def pure_random_split(grid, init_box, n=20, orient="random"):
    """
    Iteratively splits the grid.

    Uniformly choosing boxes to split at each iteration.

    Tends to leave large parts of the grid un-split, since the more a certain area is split, the more likely it is to that the next split is in that area.
    """
    if not isinstance(init_box, list):
        boxes = [init_box]
    else:
        boxes = init_box

    for t in range(n):
        idx = randint(0,len(boxes)-1)
        new_boxes = boxes[idx].rand_split(orient=orient)
        boxes = boxes[:idx] + list(new_boxes) + boxes[idx+1:]
    return boxes


def area_proportioned_split(grid, init_box, n=20, orient="random"):
    """
    Iteratively splits the grid.

    Chooses to split a box with probability proportionate to its area.
    """
    if not isinstance(init_box, list):
        boxes = [init_box]
    else:
        boxes = init_box

    for t in range(n):
        areas = np.asarray([b.area() for b in boxes])
        areas = areas / areas.sum()
        idx = np.random.choice(range(len(boxes)),p=areas)

        new_boxes = boxes[idx].rand_split(orient=orient)
        boxes = boxes[:idx] + list(new_boxes) + boxes[idx+1:]
    return boxes


def sq_area_proportioned_split(grid, init_box, n=20, orient="random"):
    """
    Iteratively splits the grid.

    Chooses to split a box with probability proportionate to its square area.
    """
    if not isinstance(init_box, list):
        boxes = [init_box]
    else:
        boxes = init_box

    for t in range(n):
        areas = np.asarray([b.area() for b in boxes])
        areas = areas**2
        areas = areas / areas.sum()
        idx = np.random.choice(range(len(boxes)), p=areas)

        new_boxes = boxes[idx].rand_split(orient=orient)
        boxes = boxes[:idx] + list(new_boxes) + boxes[idx+1:]
    return boxes


def always_largest_split(grid, init_box, n=20, orient="random"):
    """
    Iteratively splits the grid.

    Always splits the largest box.

    This method lends itself to an easy heap implementation,
    so it's much, much faster than the other splitting schemes.
    """
    if not isinstance(init_box, list):
        boxes = [init_box]
    else:
        boxes = heapify(init_box)

    for t in range(n):
        box = heappop(boxes)

        new_boxes = box.rand_split(orient=orient)
        for nb in new_boxes:
            heappush(boxes, nb)
    return boxes
