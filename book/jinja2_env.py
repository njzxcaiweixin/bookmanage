from django.template.defaulttags import date
from jinja2 import Environment


# 使用Django的过滤器定义jinja2的过滤器
def environment(**option):
    env = Environment(**option)

    env.globals.update(
        {
            'date': date
        }
    )
    return env
