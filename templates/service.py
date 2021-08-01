from typing import List

from app import db  # noqa
from .model import {{entity_name|capitalize}}
from .interface import {{entity_name|capitalize}}Interface


class {{entity_name|capitalize}}Service:
    @staticmethod
    def get_all() -> List[{{entity_name|capitalize}}]:
        return {{entity_name|capitalize}}.query.all()

    @staticmethod
    def get_by_id({{entity_name|lower}}_id: int) -> {{entity_name|capitalize}}:
        return {{entity_name|capitalize}}.query.get({{entity_name|lower}}_id)

    @staticmethod
    def update({{entity_name|lower}}: {{entity_name|capitalize}}, {{entity_name|lower}}_change_updates: {{entity_name|capitalize}}Interface) -> {{entity_name|capitalize}}:
        {{entity_name|lower}}.update({{entity_name|lower}}_change_updates)
        db.session.commit()
        return {{entity_name|lower}}

    @staticmethod
    def delete_by_id({{entity_name|lower}}_id: int) -> List[int]:
        {{entity_name|lower}} = {{entity_name|capitalize}}.query.filter({{entity_name|capitalize}}.id == {{entity_name|lower}}_id).first()
        if not {{entity_name|lower}}:
            return []
        db.session.delete({{entity_name|lower}})
        db.session.commit()
        return [{{entity_name|lower}}_id]

    @staticmethod
    def create(new_attrs: {{entity_name|capitalize}}Interface) -> {{entity_name|capitalize}}:
        new_{{entity_name|lower}} = {{entity_name|capitalize}}(
            id=new_attrs["id"],
            {% for field in fields -%}
            {{field.name}}=new_attrs["{{field.name}}"],
            {% endfor -%}
        )

        db.session.add(new_{{entity_name|lower}})
        db.session.commit()

        return new_{{entity_name|lower}}
