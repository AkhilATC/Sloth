import eel
import html_tempate_render as htmlTR


@eel.expose
def fetch_index():
    print(htmlTR.template_preload())
    return htmlTR.template_preload()

eel.init("ui")
# Start the index.html file
eel.start('index.html', size=(600, 400))