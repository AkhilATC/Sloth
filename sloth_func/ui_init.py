import eel
import argparse
from sloth_func import html_tempate_render as htmlTR
import os


BASE_DIR = os.path.dirname(__file__)


@eel.expose
def fetch_index():
    print(htmlTR.template_preload())
    return htmlTR.template_preload()

eel.init(f"{BASE_DIR}/ui")
# Start the index.html file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-owner", "--render", default="base")
    args = parser.parse_args()
    if args.render == 'admin':
        eel.start('admin.html', size=(600, 400))
    else:
        eel.start(f'index.html', size=(600, 400))
