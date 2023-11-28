import json

# JSON:
x =  '{ "name":"Ritvik", "age":21, "city":"Bengaluru"}'

# Converts JSON to python dictionary format
y = json.loads(x)
print(y["age"])


# Python dictionary:
x = {
 "name":"Ritvik",
 "age":21,
 "city":"Bengaluru"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

