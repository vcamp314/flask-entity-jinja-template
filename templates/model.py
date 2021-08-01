from sqlalchemy import Integer, Column, String, TIMESTAMP
from app import db  # noqa
from .interface import {{entity_name|capitalize}}Interface


class {{entity_name|capitalize}}(db.Model):
    """A {{entity_name|capitalize}}"""

    __tablename__ = "{{entity_name|lower}}"
    id = Column(Integer(), primary_key=True)
    {% for field in fields -%}
    {{field.name}} = {{field.db_type}}
    {% endfor %}
    def update(self, changes: {{entity_name|capitalize}}Interface):
        for key, val in changes.items():
            setattr(self, key, val)
        return
