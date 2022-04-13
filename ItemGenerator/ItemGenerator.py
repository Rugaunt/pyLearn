# generate some items!

minimum_item_value = ""
item_level = {
    "Least": 1,
    "Lesser Minor": 2,
    "Greater Minor": 3,
    "Lesser Medium": 4,
    "Greater Medium": 5,
    "Lesser Major": 6,
    "Greater Major": 7
}


def generate_wondrous_item(min_item, max_item, types):
    if item_level.get(min_item)<=item_level.get(max_item):
        # a ting
    else:
        return "Error: Minimum Item too high"



class ItemGenerator:
    pass
