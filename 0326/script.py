person_info = {
    "name": "Albert",
    "surname": "Einstein",
    "languages": ["German", "Latin", "Italian", "English"],
    "occupation": {
        "role": "Professor",
       "workplace": "Uni of Berlin",
        "test": {
    "test2": "test3"
}
   }
}

print(person_info)
print(type(person_info))

print(person_info["languages"])

for language in person_info["languages"]:
    print(language)

print("==")
print(person_info["languages"][2])
print(person_info["occupation"]["role"])
print(person_info["occupation"]["test"]["test2"])

for key, value in person_info.items():
    print(key, value)

person_info["new_item"] = {"new_item": "new_item"}
print(person_info)

# person_info.update({"new_item": {"new_item": "new_item"}})
# print(person_info)

del person_info["new_item"]
print(person_info)

person_info["name"] = "Lukas"
print(person_info)