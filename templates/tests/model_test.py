from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app.test.fixtures import app, db  # noqa
from app.{{entity_name|lower}}.model import {{entity_name|capitalize}}


@fixture
def {{entity_name|lower}}() -> {{entity_name|capitalize}}:
    return {{entity_name|capitalize}}(
        id=1,
        {% for field in fields -%}
        {% if field.type == "int" -%}
        {{field.name}}=1,
        {% elif field.type == "datetime" -%}
        {{field.name}}=datetime.strptime("2018-06-29 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"),
        {% else -%}
        {{field.name}}="Test {{field.name}}",
        {% endif -%}
        {% endfor -%}
    )


def test_{{entity_name|capitalize}}_create({{entity_name|lower}}: {{entity_name|capitalize}}):
    assert {{entity_name|lower}}


def test_{{entity_name|capitalize}}_retrieve({{entity_name|lower}}: {{entity_name|capitalize}}, db: SQLAlchemy):  # noqa
    db.session.add({{entity_name|lower}})
    db.session.commit()
    s = {{entity_name|capitalize}}.query.first()
    assert s.__dict__ == {{entity_name|lower}}.__dict__
