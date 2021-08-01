from unittest.mock import patch
from flask.testing import FlaskClient
from flask.wrappers import Response
from datetime import datetime

from app.test.fixtures import client, app  # noqa
from app.{{entity_name|lower}}.model import {{entity_name|capitalize}}
from app.{{entity_name|lower}}.schema import {{entity_name|capitalize}}Schema
from app.{{entity_name|lower}}.service import {{entity_name|capitalize}}Service
from app.{{entity_name|lower}}.interface import {{entity_name|capitalize}}Interface


def {{entity_name|lower}}({{entity_name|lower}}_id: int = 123, {{fields[0].name}}: str = "Test {{fields[0].name}}") -> {{entity_name|capitalize}}:
    return {{entity_name|capitalize}}(
        id={{entity_name|lower}}_id,
        {% for field in fields -%}
        {% if field.name == fields[0].name -%}
        {{field.name}}={{field.name}},
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


class Test{{entity_name|capitalize}}Resource:
    @patch.object({{entity_name|capitalize}}Service, "get_all", lambda: [{{entity_name|lower}}(123), {{entity_name|lower}}(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/{{entity_name|lower}}", follow_redirects=True).get_json()
            expected = {{entity_name|capitalize}}Schema(many=True).dump([{{entity_name|lower}}(456), {{entity_name|lower}}(123)])
            for r in results:
                assert r in expected


class Test{{entity_name|capitalize}}{{entity_name|capitalize}}Resource:
    @patch.object(
        {{entity_name|capitalize}}Service,
        "get_all",
        lambda: [{{entity_name|lower}}(123, {{fields[0].name}}="Test {{fields[0].name}} 1"), {{entity_name|lower}}(456, {{fields[0].name}}="Test {{fields[0].name}} 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/{{entity_name|lower}}", follow_redirects=True).get_json()
            expected = (
                {{entity_name|capitalize}}Schema(many=True)
                .dump([{{entity_name|lower}}(123, {{fields[0].name}}="Test {{fields[0].name}} 1"), {{entity_name|lower}}(456, {{fields[0].name}}="Test {{fields[0].name}} 2")])
            )
            for r in results:
                assert r in expected

    @patch.object(
        {{entity_name|capitalize}}Service,
        "create",
        lambda create_request: {{entity_name|capitalize}}(
            id=create_request.get("id"),
            {% for field in fields -%}
            {{field.name}}=create_request.get("{{field.name}}"),
            {% endfor -%}
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(
                {% for field in fields -%}
                {% if field.type == "int" -%}
                {{field.name}}=1,
                {% elif field.type == "datetime" -%}
                {{field.name}}=datetime.strptime("2018-06-29 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"),
                {% else -%}
                {{field.name}}="{{field.name}}",
                {% endif -%}
                {% endfor -%}
            )
            result: dict = client.post("/api/{{entity_name|lower}}/", json=payload).get_json()
            expected = (
                {{entity_name|capitalize}}Schema()
                .dump({{entity_name|capitalize}}(
                    {% for field in fields -%}
                    {{field.name}}=payload["{{field.name}}"],
                    {% endfor -%}
            ))
            )
            print(expected)
            print(result)
            assert result == expected


def fake_update({{entity_name|lower}}: {{entity_name|capitalize}}, changes: {{entity_name|capitalize}}Interface) -> {{entity_name|capitalize}}:
    # To fake an update, just return a new object
    updated_{{entity_name|lower}} = {{entity_name|capitalize}}(id={{entity_name|lower}}.id, {{fields[0].name}}=changes["{{fields[0].name}}"])
    return updated_{{entity_name|lower}}


class Test{{entity_name|capitalize}}IdResource:
    @patch.object({{entity_name|capitalize}}Service, "get_by_id", lambda id: {{entity_name|capitalize}}(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.get("/api/{{entity_name|lower}}/123").get_json()
            expected = {{entity_name|capitalize}}(id=123)
            assert result["id"] == expected.id

    @patch.object({{entity_name|capitalize}}Service, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.delete("/api/{{entity_name|lower}}/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object({{entity_name|capitalize}}Service, "get_by_id", lambda id: {{entity_name|capitalize}}(id=id))
    @patch.object({{entity_name|capitalize}}Service, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.put(
                "/api/{{entity_name|lower}}/123", json={ "{{fields[0].name}}": "New {{fields[0].name}}"}
            ).get_json()
            expected: dict = {{entity_name|capitalize}}Schema().dump(
                {{entity_name|capitalize}}(id=123, {{fields[0].name}}="New {{fields[0].name}}")
            )
            assert result == expected
