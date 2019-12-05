import unittest
import requests
from subprocess import Popen, PIPE
from tempfile import TemporaryFile
import socket
import sys
import time

class HttpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._server = Popen('python ./server.py', shell=True, stdout=sys.stdout, stderr=sys.stderr)
        time.sleep(0.2)
    
    @classmethod
    def tearDownClass(cls):
        cls._server.terminate()

    def testSimpleRequest(self):
        resp = requests.get('http://localhost:8080/')
        self.assertTrue(resp.ok)
    
    def testMultipleRequests(self):
        with requests.session() as s:
            self.assertTrue(s.get('http://localhost:8080/').ok)
            self.assertTrue(s.get('http://localhost:8080/').ok)
        
if __name__ == '__main__':
    unittest.main()