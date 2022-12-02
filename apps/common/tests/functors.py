# Standard imports
from time import sleep

# Core imports.
from django.core.cache import cache

# Third-party imports.
from django_redis import get_redis_connection


class TestUpRunning:

    def test_home_page(self, client):
        url = '/'
        response = client.get(url)
        assert response.status_code == 404


    def test_admin_page(self, client):
        url = '/admin'
        response = client.get(url)
        assert response.status_code == 301


    def test_redis_is_up(self):
        default_redis_connection = get_redis_connection('default')
        assert default_redis_connection.ping()


    def test_cache_is_setup(self):
        cache.set('k', 'v', timeout=1)
        assert 'v' == cache.get('k')
        sleep(1)
        assert cache.get('k') is None
