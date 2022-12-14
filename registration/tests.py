from django.test import TestCase

# Create your tests here.
fields = ['username','first_name','last_name','email','date_joined','last_login']

for i in fields:
    print(type(i))
