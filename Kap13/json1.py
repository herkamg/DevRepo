import json
# in this example the data is a dictionary

data = '''
{
    "name" : "Kamga",
    "phone" : {
        "type" : "intl",
        "number" : "74183908"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('name: ', info["name"])
print('Hide: ', info["email"]["hide"])
