from jinja2 import Template


class MyClass1:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def render_template(self):
        template_str = "MyClass1: param1={{ param1 }}, param2={{ param2 }}"
        template = Template(template_str)
        return template.render(param1=self.param1, param2=self.param2)


class MyClass2:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def render_template(self):
        template_str = "MyClass2: param1={{ param1 }}, param2={{ param2 }}, param3={{ param3 }}"
        template = Template(template_str)
        return template.render(param1=self.param1, param2=self.param2, param3=self.param3)


# 在不同的类中使用相同的Jinja2模板
template_str = "param1={{ param1 }}, param2={{ param2 }}, param3={{ param3 }}"
template = Template(template_str)

# MyClass1传递参数并渲染模板
obj1 = MyClass1("value1", "value2")
result1 = obj1.render_template()
print(result1)

# MyClass2传递参数并渲染模板
obj2 = MyClass2("value1", "value2", "value3")
result2 = obj2.render_template()
print(result2)


# 在另一个类中使用相同的Jinja2模板并传递不同的参数
class AnotherClass:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def render_template(self):
        return template.render(param1=self.param1, param2=self.param2, param3=self.param3)


# AnotherClass传递参数并渲染模板
obj3 = AnotherClass("value4", "value5", "value6")
result3 = obj3.render_template()
print(result3)