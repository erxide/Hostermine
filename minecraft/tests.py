from django.test import TestCase

# Create your tests here.
import requests

print(((requests.get("http://localhost:5000/test")).json())['crt'])