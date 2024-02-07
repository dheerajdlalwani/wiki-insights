import unittest
import requests
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'

    def test_word_frequency_analysis(self):
        topic = 'Boston Tea Party'
        n = 5

        response = requests.get(f'{self.base_url}/wiki-word-frequency', params={'topic': topic, 'n': n})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn('topic', data)
        self.assertEqual(data['topic'], topic)
        self.assertIn('top_words', data)
        self.assertEqual(len(data['top_words']), n)

    def test_search_history_endpoint(self):
        response = requests.get(f'{self.base_url}/search-history')
        self.assertEqual(response.status_code, 200)

        data = response.json()["data"]
        self.assertIsInstance(data, list)

    def test_search_history_with_query(self):
        # Test search history endpoint with query
        query = 'Bos'

        response = requests.get(f'{self.base_url}/search-history?q={query}')
        self.assertEqual(response.status_code, 200)

        data = response.json()["data"]
        for entry in data:
            self.assertTrue(entry['topic'].lower().startswith(query.lower()))

if __name__ == '__main__':
    unittest.main()
