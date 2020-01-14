from fuzzywuzzy import process

from bpaint import app


@app.template_filter('fuzzy')
def fuzzy_search(color_name, colors_list):
    print(f'\n{color_name=}\n{type(color_name)=}\n{colors_list=}\n{type(colors_list)=}\n')
    # return [result[0] for result in process.extract(color_name, colors_list) if result[1] >= 80]