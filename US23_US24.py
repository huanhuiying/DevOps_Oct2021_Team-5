import ast

highscore_file = open("highscore.txt", "r")
highscore_file = highscore_file.read()
highscore_dict = ast.literal_eval(highscore_file)

# US23
def print_leaderboard(highscore_dict):
    leaderboard_names = []
    sorted_highscore_dict = dict(sorted(highscore_dict.items(), key = lambda item: item[1], reverse = True))
    print('--------- HIGH SCORES ---------')
    print('Pos Player                Score')
    print('--- ------                -----')

    count = 1
    for i in sorted_highscore_dict:
        if count < 11:
            leaderboard_names.append(str(i))
            if count < 10:
                print(" {}. {}{}{}".format(str(count), str(i), " " * (25 - len(i)), str(sorted_highscore_dict[i])))
            else:
                print("{}. {}{}{}".format(str(count), str(i), " " * (25 - len(i)), str(sorted_highscore_dict[i])))
        count += 1

    print("-------------------------------")

    return leaderboard_names


# US24
def check_position(score, highscore_dict):
    scores = list(highscore_dict.values())
    scores.append(score)
    scores.sort(reverse = True)
    position = scores.index(score) + 1
    return position

def check_name_input(name):
    if len(name) > 20:
        return False
    else:
        return True

def save_score(name, score, highscore_dict):
    highscore_dict[name] = score
    with open("highscore.txt", "r+") as f:
        f.seek(0)
        f.write(str(highscore_dict))
        f.truncate()
        
    return highscore_dict
