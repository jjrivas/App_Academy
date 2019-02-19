# Write a method map_by_name that takes in an array of hashes and returns a new array
# containing the names of each hash

def map_by_name(arr):
    # new_arr = []
    # for x in arr:
    #     new_arr.append(x['name'])
    # return new_arr

    return list(map(lambda x: x['name'], arr))
    

if __name__ == "__main__":
    pets = [
        {'type': 'dog', 'name': 'Rolo'},
        {'type': 'cat', 'name': 'Sunny'},
    ]

    print(map_by_name(pets))