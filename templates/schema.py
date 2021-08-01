from app import ma
from .model import {{entity_name|capitalize}}


class {{entity_name|capitalize}}Schema(ma.SQLAlchemyAutoSchema):
    """{{entity_name|capitalize}}"""

    class Meta:
        model = {{entity_name|capitalize}}
