import random

from card_class import Card_Class

class Deal_Card:
    deal_card_counter = 0
  
    random_deck_order_list = list(range(52))
    random.shuffle(random_deck_order_list)  #静的な変数としてクラス変数を使用
    
    
    def deal_card(self,ins_someone_info):#インスタンスの入った配列を作成し、それの属性を読むことで情報を出す予定だったが扱いが難しすぎたため要素別にリスト作成する仕様に・・・
                                                                        
        card_number = self.random_deck_order_list[self.deal_card_counter]
        card_dealed = Card_Class(int(card_number))                      #選ばれた0-51の数に対応する管理番号のインスタンスを作成
        
        ins_someone_info.hand_card_number.append(card_dealed.written_number)
        ins_someone_info.hand_card_point.append(card_dealed.point_in_game)
        ins_someone_info.hand_card_sub_point.append(card_dealed.sub_point_in_game)
        
            
        self.deal_card_counter = self.deal_card_counter + 1
               
    def hit_card(self,ins_someone_info):
        print("カードを引きました")
        self.deal_card(ins_someone_info)

    def shuffle_deck(self):
        self.deal_card_counter = 0
        random.shuffle(self.random_deck_order_list)
        print("捨て札をデッキに戻しシャッフルしました")
