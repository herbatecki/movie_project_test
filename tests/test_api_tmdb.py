# from defer import return_value # samo się zaimportowało i generuje ostrzeżenia w "pytest", chociaż nie błędy
import pytest
from main import app
from unittest.mock import Mock


@pytest.mark.parametrize('list_type',[('popular'),('top_rated'),('upcoming'),('now_playing')])


def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_with(f'movie/{list_type}')

# ('cast',['Actor 1','Actor 2'])

"""
@pytest.mark.parametrize('list_type',(
    ('popular'),
    ('top_rated'),
    ('now_playing'),
    ('upcoming')
))
"""
