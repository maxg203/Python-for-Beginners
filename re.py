import re

myString = 'Send an email from this@email.com to test@user.com 34 times.'

result = re.findall('\S+@\S+', myString)
print(result)
