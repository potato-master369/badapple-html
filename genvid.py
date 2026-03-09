from jinja2 import Environment, FileSystemLoader
import base64
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('base.html')
with open('fortemplate.mp4', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
data = {'video_content': b64}
rendered_output = template.render(data)
with open('final.html', 'w') as f:
    f.write(rendered_output)