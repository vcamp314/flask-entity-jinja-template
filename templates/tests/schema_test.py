from pytest import fixture
from datetime import datetime

from app.{{entity_name|lower}}.model import {{entity_name|capitalize}}
from app.{{entity_name|lower}}.schema import {{entity_name|capitalize}}Schema
from app.{{entity_name|lower}}.interface import {{entity_name|capitalize}}Interface


@fixture
def schema() -> {{entity_name|capitalize}}Schema:
    return {{entity_name|capitalize}}Schema()


def test_{{entity_name|capitalize}}Schema_create(schema: {{entity_name|capitalize}}Schema):
    assert schema


def test_{{entity_name|capitalize}}Schema_works(schema: {{entity_name|capitalize}}Schema):
    params: {{entity_name|capitalize}}Interface = schema.load(
        {
            "id": 1,
            {% for field in fields -%}
            {% if field.type == "int" -%}
            "{{field.name}}": 1,
            {% elif field.type == "datetime" -%}
            "{{field.name}}": "2021-07-27T09:33:15.142Z",
            {% else -%}
            "{{field.name}}": "Test {{field.name}}",
            {% endif -%}
            {% endfor -%}
        }
    )
    {{entity_name|lower}} = {{entity_name|capitalize}}(**params)

    assert {{entity_name|lower}}.id == 1
    {% for field in fields -%}
    {% if field.type == "int" -%}
    assert {{entity_name | lower}}.{{field.name}} == 1
    {% elif field.type == "datetime" -%}
    assert {{entity_name|lower}}.{{field.name}} == "2021-07-27T09:33:15.142Z"
    {% else -%}
    assert {{entity_name|lower}}.{{field.name}} == "Test {{field.name}}"
    {% endif -%}
    {% endfor -%}
