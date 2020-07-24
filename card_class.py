class Card_Class(object):
    def __init__(self, number_in_list):  # 管理用の番号からそのカードが持つ属性を計算して属性付け
        self.number_in_list = number_in_list

        self.suit = number_in_list % 4  # 作ったけどブラックジャックでは参照する場所が実はないような・・・？

        # 管理番号0-3の4枚がA,4-7の4枚が2....
        self.written_number = int(number_in_list/4) + 1

        if(self.written_number >= 11):
            self.point_in_game = 10
        else:
            self.point_in_game = self.written_number

        if(self.written_number == 1):
            self.sub_point_in_game = 11  # sub~はAを11として数えるための参照用
        else:
            self.sub_point_in_game = self.point_in_game

    def peep(self):  # デバッグ用
        print(self.number_in_list)
        print(self.suit)
        print(self.written_number)
        print(self.point_in_game)
        print(self.sub_point_in_game)
