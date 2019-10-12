#!/usr/bin/python

import math


"""
tldr:
Receive two dictionaries, recipe and ingredients
Recipe dictates how many ingredients required to completed 1 recipe
Ingredients dictate how many ingredients available
Dictionary form for r and i are identical 


Required output:
int
maximum number of recipes able to be made with current ingredients

Plan:
Look for each key in each dictionary if they exist: 
Determine total amount of recipes able to be made recipe // ingredient
If all are greater than 1, add 1 to batch
If any are == 0, return 0
"""


def recipe_batches(recipe, ingredients):
    # counter = 0
    batches_counter = []

    if len(recipe) != len(ingredients):
        return 0
    for key in recipe:
        # For every key in recipe
        if key in ingredients:
          # check if key from recipe is in ingredients
          # if it is divide the value from ingredients by key and set to temp_counter
            temp_counter = ingredients[key] // recipe[key]
            # Append temp counter to empty batch counter
            batches_counter.append(temp_counter)
            # if temp_counter > counter:
            #   # and counter == False // is empty
            #   # not counter and
            #   # If temp counter is less than counter set counter to new lowest value,
            #   # this works because we're only triggering if recipe key is present in ingredients
            #   #
            #     counter = temp_counter
            # else:
            #     counter = temp_counter
        # else:
        #     counter = 0
    # return minium value from batch counter
    return min(batches_counter)
    # return counter


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
