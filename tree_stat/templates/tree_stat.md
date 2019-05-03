| directory | type | count | size |
| --- | --- | ---: | ---: |
{% for directory in directory_measures %}
| {{directory.path}} | ALL | {{directory.total.count}} | {{human_readable_size(directory.total.volume)}} |
{% for ext, measure in directory.file_type_measures.items() %}
| {{directory.path}} | {{ext}} | {{measure.count}} | {{human_readable_size(measure.volume)}} |
{% endfor %}
{% endfor %}
