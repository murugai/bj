def judge_point(tuple_player_point,tuple_dealer_point):
    goal_point = 21

    if (max(tuple_player_point) > goal_point):
        return -1
    if (max(tuple_dealer_point) > goal_point):
        return 1
    if(max(tuple_player_point) > max(tuple_dealer_point)):
        return 1
    elif(max(tuple_player_point) == max(tuple_dealer_point)):
        return 0
    else:
        return -1