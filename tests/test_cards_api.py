from models.card import Card


def test_card_contract():
    card_json = {
        "id": 26000014,
        "name": "Musketeer",
        "icon": "musketeer",
        "cost": 4,
        "rarity": "Rare",
        "type": "tid_card_type_character",
        "arena": 0,
        "hash": "b26f2c4dab2ba00cbabd91c2cc755f9f"
    }

    card = Card(**card_json)
    assert card.name == 'Musketeer'


def test_get_cards(api):
    response = api.get('https://statsroyale.com/api/cards')
    assert response.ok

    cards = []
    for card in response.json():
        cards.append(Card(**card))

    assert len(cards) == 98
