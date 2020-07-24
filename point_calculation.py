from sum_list import sum_list

goal_point = 21


def point_calc(ins_someone_info):
    sum_main_point = sum_list(ins_someone_info.hand_card_point)
    sum_sub_point = sum_list(ins_someone_info.hand_card_sub_point)

    while((sum_sub_point > sum_main_point) and (sum_sub_point > goal_point)):  # １の枚数を数えるほうがいいかな…？
        sum_sub_point = sum_sub_point - 10

    if(sum_sub_point == sum_main_point or sum_sub_point > goal_point):
        return_tuple = ((sum_main_point),)

        return return_tuple
    else:
        return sum_main_point, sum_sub_point
