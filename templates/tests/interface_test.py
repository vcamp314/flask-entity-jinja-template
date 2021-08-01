from pytest import fixture

from app.{{entity_name|lower}}.model import {{entity_name|capitalize}}
from app.{{entity_name|lower}}.interface import {{entity_name|capitalize}}Interface


@fixture
def interface() -> {{entity_name|capitalize}}Interface:

    params: {{entity_name|capitalize}}Interface = {
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
    return params


def test_{{entity_name|capitalize}}Interface_create(interface: {{entity_name|capitalize}}Interface):
    assert interface


def test_{{entity_name|capitalize}}Interface_works(interface: {{entity_name|capitalize}}Interface):
    assert {{entity_name|capitalize}}(**interface)

