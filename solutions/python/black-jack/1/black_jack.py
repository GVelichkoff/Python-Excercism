def value_of_card(card):
    score = 0
    if 'J' in card or 'Q' in card or 'K' in card:
        score += 10
    elif 'A' in card:
        score += 1
    else:
        score += int(card)
    return score

def higher_card(card_one, card_two):
    score_one = value_of_card(card_one)
    score_two = value_of_card(card_two)
    if score_one == score_two:
        return (card_one, card_two)
    elif score_one > score_two:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    result = 0
    if (card_one == 'A' or card_two == 'A'):
        result += 1
    elif value_card_one + value_card_two > 10:
        result += 1
    else:
        result += 11
    return result
        


def is_blackjack(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if (card_one == 'A' or card_two == 'A') and (value_card_one == 10 or value_card_two == 10):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one == value_card_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one + value_card_two in [9, 10, 11]:
        return True
    else:
        return False