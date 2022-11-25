.. image:: assets/logo_actris_ccress.png
  :width: 250
  :alt: ACTRIS logo
  :align: center

|

{{cookiecutter.project_slug}} Documentation
{% for i in  "{{cookiecutter.project_slug}} Documentation" %}={% endfor %}

.. toctree::
   :maxdepth: 2

   self
   user_guide/index.rst
   how_to/index.rst
   api_documentation/index.rst
