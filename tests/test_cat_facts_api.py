import requests
import pytest

base_url = 'https://catfact.ninja'

@pytest.mark.api
def test_get_random_cat_fact():
    endpoint = '/fact'
    url = base_url + endpoint
    response = requests.get(url)
    assert response.status_code == 200, "Failed to get a random cat fact"
    assert response.status_code == 200, response.raise_for_status()

    data = response.json()
    assert 'fact' in data, "Response does not contain 'fact' key"
    assert isinstance(data['fact'], str), "Cat fact is not a string"

@pytest.mark.api
def test_get_cat_facts_with_pagination():
    endpoint = '/facts'
    params = {'limit': 5, 'page': 1}
    url = base_url + endpoint

    response = requests.get(url, params=params)
    assert response.status_code == 200, "Failed to get cat facts with pagination"
    assert response.status_code == 200, response.raise_for_status()

    data = response.json()
    assert 'data' in data, "Response does not contain 'data' key"
    assert isinstance(data['data'], list), "Data is not a list"
    assert len(data['data']) > 0, "No cat facts returned"
    assert len(data['data']) == 5, "Number of cat facts returned is not equal to the requested limit"

@pytest.mark.api
def test_get_random_cat_breeds():
    endpoint = '/breeds'
    url = base_url + endpoint

    response = requests.get(url)
    assert response.status_code == 200, "Failed to get cat breeds"
    assert response.status_code == 200, response.raise_for_status()

    data = response.json()
    assert isinstance(data['data'], list), "Data is not a list"
    assert 'breed' in data['data'][0], "Response does not contain 'breed' key"
    assert isinstance(data['data'][0]['breed'], str), "Cat breed is not a string"

@pytest.mark.api
def test_get_cat_breeds_with_pagination():
    endpoint = '/breeds'
    params = {'limit': 5, 'page': 1}
    url = base_url + endpoint

    response = requests.get(url, params=params)
    assert response.status_code == 200, "Failed to get cat breeds with pagination"
    assert response.status_code == 200, response.raise_for_status()

    data = response.json()
    assert 'breed' in data['data'][0], "Response does not contain 'breed' key"
    assert isinstance(data['data'], list), "Data is not a list"
    assert len(data['data']) > 0, "No cat breeds were returned"
    assert len(data['data']) == 5, "Number of cat breeds returned is not equal to the requested limit"
