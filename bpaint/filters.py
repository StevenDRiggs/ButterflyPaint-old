
'''
JINJA FILTERS
--------------
'''
from bpaint import app
from bpaint.methods import returnTrue

#HERE THERE ARE TWO WAYS OF USING FILTERS

#EITHER BY USING DEFINED FUNCTIONS
app.jinja_env.filters['returnTrue'] = returnTrue

#OUR DEFINING THE FUNCTION WITH A FILTER DECORATOR
@app.template_filter()
def roundit(number, point=1):
    return round(number, point)
        