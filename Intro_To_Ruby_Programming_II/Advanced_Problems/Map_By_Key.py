# Write a method map_by_key that takes in an array of hashes and a key string.
# The method should return a new array containing the values of each has for the
# given key

def map_by_key(arr, key):
    return list(map(lambda x: x[key], arr))

if __name__ == "__main__":
    locations = [
        {'city': 'New York City', 'state': 'New York', 'coast': 'East'},
        {'city': 'San Francisco', 'state': 'California', 'coast': 'West'}
    ]

    print(map_by_key(locations, 'state'))