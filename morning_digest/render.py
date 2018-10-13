from jinja2 import Template
import datetime



def render_sources(sources) -> str:
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
    {% for source in sources %}
    <section>
      <h2>{{ source.url }}</h2>
      {% for content in source.content %}
        <p>{{ content.text }}</p>
        {% if content.image %}
          <img src={{ content.image }} style="max-width:100%; height:auto; border:none;" />
        {% endif %}
      {% endfor %}
    </section>
    <hr />
    {% endfor %}
  </body>
</html>
"""
    )

    return template.render(subject=f"Morning Digest - {date}", sources=sources)
