import turtle
import random


def get_restaurant_location():
    # Ask the user for a random x,y location for restaurant
    x = int(input("Enter the x-coordinate of the restaurant location: "))
    y = int(input("Enter the y-coordinate of the restaurant location: "))

    return x, y


def move_turtle(x, y):
    # Set up the turtle
    wn = turtle.Screen()
    t = turtle.Turtle()

    # Move the turtle to the restaurant location
    t.penup()
    t.goto(x, y)
    t.pendown()

    return t


def get_breakfast_choice():
    # Ask the user for breakfast options
    breakfast = input(
        "What would you like for breakfast? Bacon sandwich, sausage sandwich, or oatmeal? ")

    # Use if, elif, and elif statement to decide how the user wants their breakfast
    if breakfast.lower() == "bacon sandwich":
        print("You have ordered a bacon sandwich.")
    elif breakfast.lower() == "sausage sandwich":
        print("You have ordered a sausage sandwich.")
    elif breakfast.lower() == "oatmeal":
        print("You have ordered oatmeal.")
    else:
        print("Sorry, that's not a valid breakfast option.")

    return breakfast


def buy_something_else():
    while True:
        response = input("Do you want to buy something else? (yes or no): ")
        if response.lower() == "yes":
            item = input("What would you like to buy? ")
            print("You have ordered a", item)
        elif response.lower() == "no":
            print("Thank you for your order!")
            break
        else:
            print("Sorry, that's not a valid response. Please enter yes or no.")


def main():
    x, y = get_restaurant_location()
    t = move_turtle(x, y)
    breakfast = get_breakfast_choice()
    buy_something_else()


if __name__ == "__main__":
    main()
