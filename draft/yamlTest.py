import yaml

data = {"name": "John", "age": 30, "city": "New York", "emoji": "🎯"}

with open("data.yaml", "w") as f:
    yaml.dump(data, f)
with open('data.yaml', 'r') as f:
    ctx = yaml.safe_load(f)
print(ctx)
