Flask Entity Jinja2 Template
=================================
Jinja2 template for a flask entity, to be used together with the command line tool:
https://github.com/vcamp314/template-transcriber

++++++
Usage
++++++
- Clone this project.
- Create a json file with the following structure::


    {
      "entity_name": "project",
      "resulting_folder_name": "project",
      "fields": [
        {
          "name": "name",
          "type": "str",
          "db_type": "Column(String(255))"
        },
        {
          "name": "description",
          "type": "str",
          "db_type": "Column(String(255))"
        },
        {
          "name": "start",
          "type": "datetime",
          "db_type": "Column(TIMESTAMP(timezone=True))"
        }
      ]
    }

- Replace contents with whatever entity name and fields you'd like.
- Run the template-transcriber tool with the path to the json as the first argument and the path to this project's cloned code base as the other.
- Please see the readme for the template transcriber tool for details on how to run (https://github.com/vcamp314/template-transcriber).

