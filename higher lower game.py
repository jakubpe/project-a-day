import training
import random
game_data = training.data


def random_item():
    i = random.randint(0, len(game_data))
    comparable = game_data[i]
    return comparable


def game():
    score = 0
    first_thing = random_item()
    second_thing = random_item()
    while True:
        while first_thing['name'] == second_thing['name']:
            second_thing = random_item()
        print("Who is more popular?\n" + first_thing['name'] + ' from ' + first_thing['country'])
        print('Description: ' + first_thing['description'] + '\nor')
        print(second_thing['name'] + ' from ' + second_thing['country'])
        print('Description: ' + second_thing['description'])
        winner = int(input("1 or 2: "))
        if winner == 1 and first_thing['follower_count'] > second_thing['follower_count']:
            score += 1
            print("Nice! Your current score is: {}".format(score))
            print(first_thing['name'] + ' has ' + str(first_thing['follower_count']) + ' followers')
            print(second_thing['name'] + ' has ' + str(second_thing['follower_count']) + ' followers')
            second_thing = random_item()
        elif winner == 2 and second_thing['follower_count'] > first_thing['follower_count']:
            score += 1
            print("Nice! Your current score is: {}".format(score))
            print(first_thing['name'] + ' has ' + str(first_thing['follower_count']) + ' followers')
            print(second_thing['name'] + ' has ' + str(second_thing['follower_count']) + ' followers')
            first_thing = second_thing
            second_thing = random_item()
        else:
            print("Incorrect. Game over. Your game score is {}".format(score))
            print(first_thing['name'] + ' has ' + str(first_thing['follower_count']) + ' followers')
            print(second_thing['name'] + ' has ' + str(second_thing['follower_count']) + ' followers')
            if input("Do you want to play a new game? y/n") == 'y':
                game()
            return False
        print("")


game()