"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME  = 40

def bake_time_remaining( elapsed_bake_time = int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
MY_LASAGNA = bake_time_remaining(40)
PREPARATION_TIME = 33
print(bake_time_remaining(30), 'min are reamining.')

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the time in minutes for the preparation of number of layers.
    :param number_of_layers: the time for the layers being added
    """
    time_taken = 2 
    return  number_of_layers * time_taken





def elapsed_time_in_minutes(number_of_layer, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    :param number_of_layers: int - the number of layers in the lasagna. 
    :elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    return preparation_time_in_minutes(number_of_layer) + elapsed_bake_time
    

print(elapsed_time_in_minutes(3, 20))