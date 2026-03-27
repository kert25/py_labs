import json


data = {
    "name": "Иван",
    "age": 25,
    "languages": ["Python", "JavaScript"],
    "is_student": True
}

json_string = json.dumps(data, ensure_ascii=False, indent=4)
print("JSON строка:")
print(json_string)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("\nДанные сохранены в data.json")

with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("\nЗагруженные данные:")
print(loaded_data)
