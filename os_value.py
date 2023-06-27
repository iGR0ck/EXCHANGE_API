import os

value = os.getenv('VARIABLE_NAME')
# или
#value = os.environ.get('VARIABLE_NAME')

print(value)