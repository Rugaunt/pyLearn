# generate some items!
import random as rdm
import ItemListSearcher as Searcher

tab_name_wondrous_items = 'WondrousItems'

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
prefix_big = 'Greater'
prefix_small = 'Lesser'
affix_minor = 'Minor'
affix_med = 'Medium'
affix_major = 'Major'


def determine_level_of_item(min_item, max_item):
    min_it = item_level.get(min_item)
    max_it = item_level.get(max_item)
    item_range = min_it - max_it
    if item_range != 1:
        selected_item_range = min_it + rdm.randint(1, item_range) - 1
    else:
        selected_item_range = min_it
    return selected_item_range


# potential error here if no types selected TODO look into this
def determine_type_of_item(types):
    type_selection = rdm.randint(1, types.len) - 1
    return types[type_selection]


def generate_wondrous_item(min_item, max_item, types):
    if item_level.get(min_item) <= item_level.get(max_item):
        item_lvl = determine_level_of_item(min_item, max_item)

        prefix = None
        affix = None
        match item_lvl:
            case 1:
                prefix = 'Least'
                affix = affix_minor
            case 2:
                prefix = prefix_small
                affix = affix_minor
            case 3:
                prefix = prefix_big
                affix = affix_minor
            case 4:
                prefix = prefix_small
                affix = affix_med
            case 5:
                prefix = prefix_big
                affix = affix_med
            case 6:
                prefix = prefix_small
                affix = affix_major
            case 7:
                prefix = prefix_big
                affix = affix_major
        the_type = determine_type_of_item(types)
        roll = rdm.randint(1, 100)
        return Searcher.process_workbook(tab_name_wondrous_items, roll, prefix, affix, the_type)
    else:
        return "Error: Minimum Item too high"



