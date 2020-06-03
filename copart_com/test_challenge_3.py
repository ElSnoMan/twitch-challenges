
def test_challenge_3(py):
    """
    1. Go to copart.com
    2. Gather all of the popular Makes and Models on the Home Page
    3. Print the name and URL of each Make and Model
    4. Check that there are 20 Makes and Models
    """
    py.visit('https://copart.com')
    makes_and_models = py.find("[ng-repeat*='popularSearch'] > a")
    for car in makes_and_models:
        name = car.text()
        url = car.get_attribute('href')
        print(f'{name} - {url}')
    assert makes_and_models.should().have_length(20)


def test_challenge3_copart(py):
    py.visit('https://copart.com')
    cars = py.find("li[ng-repeat*='popularSearch'] > a")
    for car in cars:
        print(f'{car.text()} - {car.get_attribute("href")}')
    assert cars.should().have_length(20)
