from jinja2 import Template

template_str = """
Name: {{ name }}
Age: {{ age }}
Hobbies: {% for hobby in hobbies %}
- {{ hobby }}
{% endfor %}
"""

template = Template(template_str)

data_dict = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "hiking", "cooking"]
}

output_str = template.render(data_dict)

print(output_str)