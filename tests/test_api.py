from data.card_model import Card


def test_cards_api(api):
    response = api.get('https://statsroyale.com/api/cards')
    assert response.ok

    cards_json = response.json()
    cards = []
    for card in cards_json:
        cards.append(Card(**card))

    assert len(cards) == 98
    first_card = cards[0]


def test_search_for_card(api):
    response = api.get('https://statsroyale.com/api/cards')
    cards = [Card(**card) for card in response.json()]
    card = next(card for card in cards if card.name == 'Battle Healer')
    assert card.cost == 4


def test_homedepot_links(py):
    py.visit('https://www.homedepot.com/b/Home-Decor-Home-Accents/N-5yc1vZar58')
    links = py.find('ul > li > a')
    hrefs = [link.get_attribute('href') for link in links]

    for href in hrefs:
        print(href)
        assert py.request.get(href).ok
