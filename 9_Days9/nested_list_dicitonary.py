capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
starting_dictionary = {
    "a": 9,
    "b": 8,
}
starting_dictionary["c"] = 7
print(starting_dictionary)
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0])

travel_log2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visited": 4
    },
}

print(travel_log2["Germany"]["cities_visited"][1])