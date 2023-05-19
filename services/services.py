import random

from lexicon.lexicon_ru import LEXICON_RU



# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spok'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, set[str]] = {
        'rock': {'scissors', 'lizard'},
        'spok': {'rock', 'scissors'},
        'scissors': {'paper', 'lizard'},
        'paper': {'rock', 'spok'},
        'lizard': {'spok', 'paper'}
    }

    if user_choice == bot_choice:
        return 'nobody_won'
    elif bot_choice in rules[user_choice]:
        return 'user_won'
    elif user_choice in rules[bot_choice]:
        return 'bot_won'
    else:
        return 'invalid_choice'
