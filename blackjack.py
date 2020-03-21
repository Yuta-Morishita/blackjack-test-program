
# (deck) トランプを作る：　得点を数えられるようにする
# (deal) トランプを二枚配る：　絵札（J,Q,K）で表示させる
# (hand) プレイヤーに配られたカードを記録する
# (hit) ヒットの場合　hand を追加する
# (game) 実際にプレーする
# (total) プレイヤーの合計を求める
# TODO (result) 勝ち負けを表記する
# (play_again) もう一度プライする

import random

deck = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4

def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
          card = "J"
        if card == 12:
          card = "Q"
        if card == 13:
          card = "K"
        if card == 1:
          card = "A"
        hand.append(card)
    return hand
  
def hit(hand):
    
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
      card = "J"
    if card == 12:
      card = "Q"
    if card == 13:
      card = "K"
    if card == 1:
      card = "A"
    hand.append(card)
    return hand


def total(hand):
  score = 0
  for card in hand:
      if card == "J" or card == "Q" or card == "K":
        score = score+10
      elif  card == "A":
        if score >= 11:
            score += 1
        else:
            score += 11
      else:
          score += card
    
  return score
    

def play_again():
  again = input("もう一度プレーしますか？ (y/n):")
  if again == "y" or again == "Y":
    game()
    return
  else:
    print("お疲れ様でした")
    exit()
    
    
def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(f"\nディーラーの合計は{total(dealer_hand)}あなたの合計は{total(player_hand)}です。You Win!")
    elif total(dealer_hand) > total(player_hand):
        print(f"\nディーラーの合計は{total(dealer_hand)}あなたの合計は{total(player_hand)}です。You Lose....")

def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"ディーラーカードの{dealer_hand[0]}です")
    print(f"プレイヤーのカードは{player_hand}合計は{total(player_hand)}です")
    
    
    choice = 0
    
    while choice != quit:
        choice = input("ヒットしますか？ スタンドしますか？ (HIT/STAND):").lower()
        if choice =="hit":
            hit(player_hand)
            print(f"\nあなたに {player_hand[-1]} が配られ、カードは {player_hand}です。 合計は {total(player_hand)} です")
            if total(player_hand) > 21:
                print("あなたは21を超えてしました。You Lose.....")
                choice = quit
                
        elif choice == "stand":
          print(f"\nディーラーの２枚目のカードは{dealer_hand[1]} 合計は{total(dealer_hand)}です。")
          while total(dealer_hand) < 17:
              hit(dealer_hand)
              print(f"ディーラーに {dealer_hand[-1]} のカードが配られ、カードは {dealer_hand}です。 合計は {total(dealer_hand)} です")
              if total(dealer_hand) > 21:
                  print("ディーラーは21を超えてしました。You Win")
                  choice = quit
          if total(dealer_hand) <= 21:
              result(dealer_hand, player_hand)
              choice = quit
            
game()
play_again()
