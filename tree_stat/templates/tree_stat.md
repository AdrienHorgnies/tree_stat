| directory | type | count | size |
| --- | --- | ---: | ---: |
{% for directory in directory_measures %}
| {{directory.path}} | ALL | {{directory.total.count}} | {{display_file_size(directory.total.volume)}} |
{% for ext, measure in directory.file_type_measures|dictsort %}
| {{directory.path}} | {{ext}} | {{measure.count}} | {{display_file_size(measure.volume)}} |
{% endfor %}
{% endfor %}
