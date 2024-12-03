from bakery import assert_equal

def convert_hand(number:int)-> str:
    '''
    The function convert_hand takes in a number that represents a card and converts it
    into a string to more acurately represent that card

    Args: 
        number (int): the number assigned to the user to represent a card
    Returns:
        str: the string representing the card
    '''
    if number == 10:
        return "X"
    elif number == 11:
        return "J"
    elif number == 12:
        return "Q"
    elif number == 13:
        return "K"
    elif number == 14:
        return "A"
    else:
        return str(number)

def hand_to_string (hand: list[int]) -> str:
    '''
    This function hand_to_string takes in a list of three numbers and converts them into strings
    to represent the hand of the user

    Args: 
        hand (list[int]): a series of integers that represent the users hand
    Returns:
        str: the string representing the three cards in the hand
    '''
    num1 = convert_hand(hand[0])
    num2 = convert_hand(hand[1])
    num3 = convert_hand(hand[2])
    return num1 + " " + num2 + " " + num3


assert_equal(hand_to_string([2, 14, 10]), "2 A X")
assert_equal(hand_to_string([13, 5, 12]), "K 5 Q")
assert_equal(hand_to_string([11, 4, 6]), "J 4 6")

def sort_hand (hand: list[int]) -> list[int]:
    '''
    this function sorts the hand from greatest to least.
    Args:
        hand (list[int]): the list that represents the hand.
    Returns:
        list[int]: returns the list but sorted with values least to greatest
    '''
    if hand[0] >= hand[1] and hand[0] >= hand[2]:
        if hand[1] >= hand[2]:
            return hand
        elif hand[1] <= hand[2]:
            return [hand[0],hand[2],hand[1]]
    elif hand [0] >= hand [1] and hand[0] <= hand[2]:
        return [hand[2], hand[0], hand[1]]
    elif hand[0] <= hand[1] and hand[0] <= hand[2]:
        if hand[1] <= hand[2]:
            return [hand[2],hand[1],hand[0]]
        elif hand[1] >= hand[2]:
            return [hand[1], hand[2], hand[0]]
    elif hand[0] <= hand[1] and hand[0] >= hand [2]:
        return [hand[1],hand[0],hand[2]]
    
assert_equal(sort_hand([12,5,9]), [12,9,5])
assert_equal(sort_hand([2,14,7]), [14,7,2])
assert_equal(sort_hand([9,4,11]), [11,9,4]) 
assert_equal(sort_hand([11,7,5]), [11,7,5])
assert_equal(sort_hand([7,10,3]), [10,7,3])
assert_equal(sort_hand([13,5,5]), [13,5,5])

def has_triple (hand: list[int]) -> bool:
    '''
    This function tests whether the three numbers in the list are the same.
    Args:
        hand(list[int]): a list of three integers representing the hand
    Returns:
        bool: returns whether the three numbers are equal or not.
    '''
    if hand[0] == hand[1] == hand[2]:
        return True
    else:
        return False
    
assert_equal(has_triple([3,3,3]), True)
assert_equal(has_triple([4,12,3]), False)
assert_equal(has_triple([3,3,5]), False)

def has_straight (hand: list[int]) -> bool:
    '''
    This function tests if the hand is a straight.
    Args:
        hand (list[int]): a list of int representing the hand
    Returns:
        bool: whether or not the hand is a straight or not
    '''
    if hand[1] == (hand[0] - 1):
        if hand [2] == (hand[1] - 1):
            return True
        else:
            return False
    else:
        return False
    
assert_equal(has_straight([12,11,10]), True)
assert_equal(has_straight([14, 13, 9]), False)
assert_equal(has_straight([10,8,6]), False)

def has_pair(hand: list[int]) -> bool:
    '''
    This function tests if the hand has a pair.
    Args:
        hand (list[int]): a list of int representing the hand
    Returns:
        bool: whether or not the hand has a pair or not
    '''
    if hand[0] == hand [1]:
        return True
    elif hand [1] == hand[2]:
        return True
    else:
        return False
    
assert_equal(has_pair([2,2,1]), True)
assert_equal(has_pair([7,5,5]), True)
assert_equal(has_pair([12,6,3]), False)

def score_hand (hand: list[int]) -> int:
    '''
    This function calculates the score of each hand.
    Args:
        hand (list[int]): a list of int representing the hand
    Returns:
        int: an integer representing the score of a hand.
    '''
    if has_triple(hand) == True:
        return (16*(16**3)) + ((16**2)*hand[0]) + (16*hand[1]) + hand[2]
    elif has_pair(hand) == True:
        return (hand[1]*(16**3)) + ((16**2)*hand[0]) + (16*hand[1]) + hand[2]
    elif has_straight(hand) == True:
        return (15*(16**3)) + ((16**2)*hand[0]) + (16*hand[1]) + hand[2]
    else:
        return ((16**2)*hand[0]) + (16*hand[1]) + hand[2]
    
assert_equal(score_hand([7,4,4]), 18244)
assert_equal(score_hand([11,10,9]), 64425)
assert_equal(score_hand([3,3,3]), 66355)

def dealer_plays(hand:list[int]) -> bool:
    '''
    This function tests if the hand has a queen high or better.
    Args:
        hand (list[int]): a list of int representing the hand
    Returns:
        bool: whether or not the hand does indeed have a queen high or better.
    '''
    score = score_hand(hand)
    new_score = score - hand[2] - (16*hand[1])
    if new_score >= 3072:
        return True
    else:
        return False

assert_equal(dealer_plays([14,2,5]), True)
assert_equal(dealer_plays([4,4,4]), True)
assert_equal(dealer_plays([8,2,5]), False)

def play_round() -> int:
    '''
    This function runs all the code, running through a hand.
    Args:
        None
    Returns:
        int: the amount of points gained or lost.
    '''
    hand = deal()
    print(hand_to_string(hand))
    choice = get_choice()
    if choice == 'f':
        return -10
    dealer_hand = deal()
    print(hand_to_string(dealer_hand))
    dealer = score_hand(sort_hand(dealer_hand))
    player = score_hand(sort_hand(hand))
    if dealer > player:
        if dealer_plays(dealer_hand)==True:
            return -20
        else:
            return 10
    else:
        return 20

def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")



play_round()