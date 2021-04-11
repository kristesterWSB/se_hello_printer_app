import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        expected = {"imie": "Krzysztoffff", "msg": "Hello Worlddddddd!"}
        actual = json.loads(rv.data)
        self.assertEqual(expected["imie"], actual["imie"])  # noqa

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<greetings><name>Krzysztof</name><msg>Hello World!</msg></greetings>', rv.data) #noqa
