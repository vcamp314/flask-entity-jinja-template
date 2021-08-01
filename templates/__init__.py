from .model import {{entity_name|capitalize}}
from .schema import {{entity_name|capitalize}}Schema


def register_routes(root_api, root="/api"):
    from .controller import api as {{entity_name|lower}}_api

    root_api.add_namespace({{entity_name|lower}}_api, path=f"{root}/{{entity_name|lower}}")
