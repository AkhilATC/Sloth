import eel
import argparse
from sloth_func import html_tempate_render as htmlTR
import os


BASE_DIR = os.path.dirname(__file__)
render = "log_out"


@eel.expose
def fetch_index():
    # print(htmlTR.template_preload())
    if render == 'log_in':
        return htmlTR.template_preload_login()
    return htmlTR.template_preload()


eel.init(f"{BASE_DIR}/ui")
# Start the index.html file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-owner", "--render", default="log_out")
    args = parser.parse_args()
    render = args.render
    eel.start(f'index.html', size=(600, 400))
