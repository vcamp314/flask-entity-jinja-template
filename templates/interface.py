from datetime import datetime
from typing import TypedDict


class {{entity_name|capitalize}}Interface(TypedDict, total=False):
    id: int
    {% for field in fields -%}
    {{field.name}}: {{field.type}}
    {% endfor -%}
