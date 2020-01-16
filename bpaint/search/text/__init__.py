from fuzzywuzzy import process

from bpaint import app


@app.template_filter('fuzzy')
def fuzzy_search(color_name, colors_list):
    pass