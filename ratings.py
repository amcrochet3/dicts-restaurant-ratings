"""Restaurant rating lister."""

def restaurant_ratings():
    filename = "scores.txt"
    ratings_dict = {}

    with open(filename, "r") as file:
        for line in file:
            restaurant, score = line.rstrip().split(":")
            ratings_dict[restaurant] = int(score)
            
    return ratings_dict


ratings = restaurant_ratings()

def add_restaurant(ratings):
    print("Please add a rating for your favorite restaurant:")
    restaurant = input("Restaurant name> ")
    score = input("Restaurant score> ")

    ratings[restaurant] = score


def print_sorted_scores(ratings):
    for restaurant, score in sorted(ratings.items()):
        print(f"{restaurant} is rated at {score}.")


add_restaurant(ratings)
print_sorted_scores(ratings)
