import unittest
from main import get_output_error

class MainTests(unittest.TestCase):

    def test_get_output_error(self):
        seen_movies = [{'title': 'abc-123'}]
        watchlist_movies = [{'title': 'abc-123'}]
        result = get_output_error('abc-123', seen_movies, watchlist_movies)
        self.assertEqual('Movie already exists in data.', result)

if __name__ == '__main__':
    unittest.main()