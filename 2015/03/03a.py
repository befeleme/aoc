'''This script contains some doctests.
Invoke the tests from the command line:
`python -m doctest -v 03a.py`
Module documentation: https://docs.python.org/3/library/doctest.html
'''
from pathlib import Path


OFFSETS = {
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0),
    '^': (0, 1),
}


def move_to_next_house(current_position, move):
    '''
    Return the next house's coordinates.

    Examples:
        >>> move_to_next_house((0, 5), '>')
        (1, 5)

        >>> move_to_next_house((65, 2), '^')
        (65, 3)
        
        >>> move_to_next_house((-150, -68), 'v')
        (-150, -69)
    '''
    new_x, new_y = OFFSETS[move]
    old_x, old_y = current_position
    return old_x + new_x, old_y + new_y



def deliver(house_map):
    '''
    Return the count of the houses visited at least once in the area.

    Examples:
        >>> deliver('>')
        2

        >>> deliver('^>v<')
        4
        
        >>> deliver('^v^v^v^v^v')
        2
    '''
    visited_houses = set()
    current_position = (0, 0)
    visited_houses.add(current_position)
    for move in house_map:
        current_position = move_to_next_house(current_position, move)
        visited_houses.add(current_position)
    
    return len(visited_houses)


def deliver_with_robo_santa(house_map):
    '''
    Return the count of the houses visited at least once in the area
    if Santa and Robo-Santa take every second house.

    Examples:
        >>> deliver_with_robo_santa('^>v<')
        3

        >>> deliver_with_robo_santa('^v')
        3

        >>> deliver_with_robo_santa('^v^v^v^v^v')
        11
    '''
    visited_houses = set()
    santas_current_position = (0, 0)
    robo_santas_current_position = (0, 0)
    visited_houses.add(santas_current_position)

    for i, move in enumerate(house_map):
        # even houses go to Santa
        if i % 2 == 0:
            santas_current_position = move_to_next_house(santas_current_position, move)
            visited_houses.add(santas_current_position)
        # and the odd ones to Robo-Santa
        else:
            robo_santas_current_position = move_to_next_house(robo_santas_current_position, move)
            visited_houses.add(robo_santas_current_position)
    return len(visited_houses)


area_map = Path('input').read_text()
print(deliver(area_map))
print(deliver_with_robo_santa(area_map))
