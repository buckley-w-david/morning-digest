from jinja2 import Template
import datetime



def render_components(components) -> str:
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    template = Template(
        """\
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>{{ subject }}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
  </head>
  <body>
    {% for component in components %}
    <section>
      <p>{{ component.url }}</p>
      {% for content in component.content %}
        <p>{{ content.title }}</p>
        <img src={{ content.image }} style="width:100%; height:auto; border:none;" />
      {% endfor %}
    </section>
    <hr />
    {% endfor %}
  </body>
</html>
"""
    )

    return template.render(subject=f"Morning Digest - {date}", components=components)
