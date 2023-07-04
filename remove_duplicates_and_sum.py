def remove_duplicates_and_add_sum(items):
    # Create an empty dictionary to store items and their counts
    items_dict = {}
    for item in items:
        # Increase the count for each item in the dictionary
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1

    new_list = []
    total_sum = 0
    for item, count in items_dict.items():
        # If the item's count is 1, add it to the new list and the total sum
        if count == 1:
            new_list.append(item)
            total_sum += item

    # Return the new list and the total sum
    return new_list, total_sum

print(remove_duplicates_and_add_sum([1, 2, "2", 3, 4, 4, 5, 5, "5", 6, 6, 7, "8", "8", 8, 9, 10, 10]))
