"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

lucky = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}
def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in'JQK' :  
        return 10
    if card in'A' :  
        return 1
    if card in lucky:
        return  lucky[card]
def value_of_cardd(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in'JQK' :  
        return 10
    if card in'A' :  
        return 11
    if card in lucky:
        return  lucky[card]
    # if card[1] in '2345678910':
        # return card[1]
# card = 'Jkkk'
# print('Jk' in card)

# print(value_of_card('2'))


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_two) > value_of_card(card_one): 
        return card_two
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two

# print(higher_card('K', '3'))

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
        


    if value_of_card(card_one) + value_of_card(card_two) +  11 > 21 or card_one == 'A' or card_two == 'A' :
        return 1
    if value_of_card(card_one) + value_of_card(card_two) + 11 <= 21 :
        return 11

# print(value_of_ace('A', 'K'))

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if value_of_cardd(card_one) == 11 and value_of_cardd(card_two) == 10:
        return True
    if value_of_cardd(card_two) == 11 and value_of_cardd(card_one) == 10:
        return True
    else:
        return False
    
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_cardd(card_one) == value_of_cardd(card_two):
        return True
    else: return False

# print(can_split_pairs('10', 'A'))
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    Ace =  value_of_ace(card_one, card_two)
    print(Ace)
    if value_of_card(card_one) + value_of_card(card_two) in {9, 10, 11}:
        return True
    else:
        return False

print(can_double_down( 'K' , 'A'))