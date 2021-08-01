from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from typing import List
from app.{{entity_name|lower}}.model import {{entity_name|capitalize}}
from app.{{entity_name|lower}}.service import {{entity_name|capitalize}}Service  # noqa
from app.{{entity_name|lower}}.interface import {{entity_name|capitalize}}Interface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: {{entity_name|capitalize}} = {{entity_name|capitalize}}(id=1, {{fields[0].name}}="Yin")
    yang: {{entity_name|capitalize}} = {{entity_name|capitalize}}(id=2, {{fields[0].name}}="Yang")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[{{entity_name|capitalize}}] = {{entity_name|capitalize}}Service.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: {{entity_name|capitalize}} = {{entity_name|capitalize}}(id=1, {{fields[0].name}}="Yin")

    db.session.add(yin)
    db.session.commit()
    updates = dict({{fields[0].name}}="Yang")

    {{entity_name|capitalize}}Service.update(yin, updates)

    result: {{entity_name|capitalize}} = {{entity_name|capitalize}}.query.get(yin.id)
    assert result.{{fields[0].name}} == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: {{entity_name|capitalize}} = {{entity_name|capitalize}}(id=1, {{fields[0].name}}="Yin")
    yang: {{entity_name|capitalize}} = {{entity_name|capitalize}}(id=2, {{fields[0].name}}="Yang")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    {{entity_name|capitalize}}Service.delete_by_id(1)
    results: List[{{entity_name|capitalize}}] = {{entity_name|capitalize}}.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: {{entity_name|capitalize}}Interface = {{entity_name|capitalize}}Interface(
        id=1,
        {% for field in fields -%}
        {% if field.name == fields[0].name -%}
        {{field.name}}="Yin",
        {% else -%}
        {% if field.type == "int" -%}
        {{field.name}}=1,
        {% elif field.type == "datetime" -%}
        {{field.name}}=datetime.strptime("2018-06-29 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"),
        {% else -%}
        {{field.name}}="Test {{field.name}}",
        {% endif -%}
        {% endif -%}
        {% endfor -%}
    )
    {{entity_name|capitalize}}Service.create(yin)
    results: List[{{entity_name|capitalize}}] = {{entity_name|capitalize}}.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
