from app import app
import os
import json
import unittest
import tempfile

paises = [
    {
        'nombre': 'brazil',
        'codigo': u'55',
    },
    {
        'nombre': 'france',
        'codigo': u'33',
    },
    {
        'nombre': 'italy',
        'codigo': u'39',
    },
    {
        'nombre': 'japan',
        'codigo': u'81',
    },
    {
        'nombre': 'spain',
        'codigo': u'34',
    }
]
class flaskAppTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        result = tester.get('/')
        self.assertEqual(result.status_code, 200)

    def test_paises(self):
        tester = app.test_client(self)
        response = tester.get('/api/paises', content_type='application/json')
        dic = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(dic['paises']),len(paises))

    def test_pais(self):
        tester = app.test_client(self)
        result = tester.get('/api/paises/brazil')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
