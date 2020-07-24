from disp_info import disp_point_of_someone, disp_list_point
from deal import Deal_Card
from card_class import Card_Class
from player_info_class import Player_Info

from judge import judge_point
from point_calculation import point_calc


goal_point = 21

end_game_flag = False
end_menu_loop_flag = False

deal_card = Deal_Card()

'''____________________________________'''''

while (end_game_flag == False):

    end_game_flag = False
    end_menu_loop_flag = False

    player_info = Player_Info()
    dealer_info = Player_Info()

    # 実際のゲームでは2枚入るけどプレイヤー側が見える情報は1枚だけなのでこのPGでは1枚だけ入れておく
    deal_card.deal_card(dealer_info)

    for i in range(2):
        deal_card.deal_card(player_info)

    tuple_players_point = disp_point_of_someone("あなた", player_info)
    print("カードの番号は")
    print(player_info.hand_card_number)

    tuple_dealers_point = disp_point_of_someone("ディーラー", dealer_info)
    print("カードの番号は")
    print(dealer_info.hand_card_number)

    # この辺に入力云々追加予定
    while (max(tuple_players_point) < goal_point):
        manipulation_word = input("Hit or Stand?")
        if (manipulation_word.upper() == "HIT"):

            deal_card.hit_card(player_info)
            tuple_players_point = disp_point_of_someone("あなた", player_info)
            print("カードの番号は")
            print(player_info.hand_card_number)
        elif(manipulation_word.upper() == "STAND"):
            break
        else:
            print("HitかStandしか入力を受け付けません")
    if(max(tuple_players_point) > goal_point):
        print("バーストしました")

        print("あなたの得点は21点です")

    print("ディーラーの番です")
    while (max(tuple_dealers_point) < 16):
        deal_card.hit_card(dealer_info)
        tuple_dealers_point = point_calc(dealer_info)

    tuple_dealers_point = disp_point_of_someone("ディーラー", dealer_info)
    print("カードの番号は")
    print(dealer_info.hand_card_number)

    result = judge_point(tuple_players_point, tuple_dealers_point)
    print("~~~~~~~~~~~~~勝負の結果は？~~~~~~~~~~~~~~~~")
    if (result == 0):
        print("引き分け")
    elif(result > 0):
        print("今回はお前の勝ちだ...")
    else:
        print("あんたの負け")

    while (end_menu_loop_flag == False):
        end_manipulation_input = input("end this game?")
        if (end_manipulation_input.upper() == "NO"):
            end_menu_loop_flag = True

            if(deal_card.deal_card_counter > 30):
                deal_card.shuffle_deck()
                deal_card.deal_card_counter = 0
        elif(end_manipulation_input.upper() == "YES"):
            end_menu_loop_flag = True
            end_game_flag = True
            print("Thank you for playing!")

        else:
            print("YesかNoしか受け付けません")
