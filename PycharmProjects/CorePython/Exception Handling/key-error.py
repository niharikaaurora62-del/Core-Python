dictionary = {"name":"Niharika", "age":25}
try:
    print(dictionary["nam"])
except KeyError as e:
    print("key error",e)