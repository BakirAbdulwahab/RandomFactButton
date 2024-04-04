import random

fact_list = ["The honeybee is the only insect that produces food eaten by humans.",
"The Great Wall of China is visible from space.",
"A day on Venus is longer than its year.",
"The Eiffel Tower can grow up to 6 inches during the summer due to thermal expansion.",
"The world’s largest desert is not the Sahara; it’s Antarctica.",
"The smallest bone in the human body is the stapes bone in the ear.",
"The Mona Lisa has no eyebrows or eyelashes.",
"The average person will spend six months of their life waiting for red lights to turn green.",
"The world’s oldest known recipe is for beer.", 
"The dot over the letter ‘i’ is called a tittle."]

random_fact = random.choice(fact_list)

print("\nHello! Welcome to the Random Fact Button!\n")

while True:
    user_input = input("If you would like to click it write 'y' or to quit write 'q': ")
    if user_input == "y":
        print(f"\n{random_fact}\n")
        random_fact = random.choice(fact_list)
        continue
    elif user_input == "q":
        print("\nOkay bye!")
        break
    else:
        print("\nSorry, Invalid input!")
        continue