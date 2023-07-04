def rotate_list(items, item_to_count):
    count = 1
    for i in range(len(items)):
        if items[i].lower() == item_to_count.lower():
            count += i
    return count

print(rotate_list(['apple', 'banana', 'Apple', 'cherry', 'apple', 'grape', 'peach', 'orange', 'kiwi', 'mango', 
                   'lemon', 'lime', 'pineapple', 'coconut', 'pear', 'strawberry', 'blueberry', 'raspberry', 
                   'blackberry', 'guava', 'pomegranate', 'plum', 'grapefruit', 'tangerine', 'melon'], 'Apple'))
