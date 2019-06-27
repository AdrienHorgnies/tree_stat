| directory | type | count | size |
| --- | --- | ---: | ---: |
{% for directory in directory_measures %}
| {{pov_formatter(directory.path)}} | ALL | {{directory.total.count}} | {{format_file_size(directory.total.volume)}} |
{% for ext, measure in directory.measures_by_file_type %}
| | {{ext}} | {{measure.count}} | {{format_file_size(measure.volume)}} |
{% endfor %}
{% endfor %}
