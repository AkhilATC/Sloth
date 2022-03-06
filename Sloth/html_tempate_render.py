from jinja2 import Template
from sloth_couch import SlothDataCouchRead as SDCR
from jinja2 import Template
from datetime import date

def preload(fun_):
    def wrap_(*args):
        basic_info = SDCR().read_basic_info()
        task_info = SDCR().read_task_info()
        return fun_(basic_info, task_info)
    return wrap_


@preload
def template_preload(b_info, t_info):

    with open('render/template.html') as file:
        template = Template(file.read())
    # Date: 03th March, 2022
    today = date.today()
    today = today.strftime("%dth. %B %Y")

    TIME_STAMP = today
    # output = template.render(basic_info=b_info, tasks=t_info, TIME_STAMP=TIME_STAMP)
    return template.render(basic_info=b_info, tasks=t_info, TIME_STAMP=TIME_STAMP)

