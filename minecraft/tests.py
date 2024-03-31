from django.test import TestCase

# Create your tests here.
import subprocess

res = subprocess.run(['bash', 'bash/ls.sh'], capture_output=True, text=True)

print(res.stdout)