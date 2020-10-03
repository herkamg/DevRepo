# in this example the object is a list
import json

data = '''
[
    {
     "id" : "002",
      "x" : "2",
      "name" : "Kamga"
    },
    { "id" : "009",
      "x" : "8",
      "name" : "Hermann"
    }
]'''

credent = json.loads(data)
for item in credent:
    print('id: ',item["id"] )
    print('x: ', item["x"])
    print('name: ', item["name"])
