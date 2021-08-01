from flask_restx import Resource
from flask import request
from flask_restx import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import {{entity_name|capitalize}}Schema
from .model import {{entity_name|capitalize}}
from .service import {{entity_name|capitalize}}Service

api = Namespace("{{entity_name|capitalize}}", description="{{entity_name|capitalize}} information")


@api.route("/")
class {{entity_name|capitalize}}Resource(Resource):
    """{{entity_name|capitalize}}s"""

    @responds(schema={{entity_name|capitalize}}Schema(many=True))
    def get(self) -> List[{{entity_name|capitalize}}]:
        """Get all {{entity_name|capitalize}}s"""

        return {{entity_name|capitalize}}Service.get_all()

    @accepts(schema={{entity_name|capitalize}}Schema, api=api)
    @responds(schema={{entity_name|capitalize}}Schema)
    def post(self):
        """Create a Single {{entity_name|capitalize}}"""

        return {{entity_name|capitalize}}Service.create(request.parsed_obj)


@api.route("/<int:id>")
@api.param("id", "{{entity_name|capitalize}} database ID")
class {{entity_name|capitalize}}IdResource(Resource):
    @responds(schema={{entity_name|capitalize}}Schema)
    def get(self, id: int) -> {{entity_name|capitalize}}:
        """Get Single {{entity_name|capitalize}}"""

        return {{entity_name|capitalize}}Service.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single {{entity_name|capitalize}}"""

        from flask import jsonify

        id = {{entity_name|capitalize}}Service.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema={{entity_name|capitalize}}Schema, api=api)
    @responds(schema={{entity_name|capitalize}}Schema)
    def put(self, id: int) -> {{entity_name|capitalize}}:
        """Update Single {{entity_name|capitalize}}"""

        changes = request.parsed_obj
        {{entity_name|lower}} = {{entity_name|capitalize}}Service.get_by_id(id)
        return {{entity_name|capitalize}}Service.update({{entity_name|lower}}, changes)
