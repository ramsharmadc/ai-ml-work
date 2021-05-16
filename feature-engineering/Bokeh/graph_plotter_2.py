from numpy.random import random
from bokeh.io import curdoc

from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import widgetbox

def get_data(N):
    return dict(x=random(size=N), y=random(size=N), r=random(size=N) * 0.03)

source = ColumnDataSource(data=get_data(200))

p = figure(tools="", toolbar_location=None)
r = p.circle(x='x', y='y', radius='r', source=source, color="navy", alpha=0.6, line_color="white")
    
slider_widget = Slider(start = 10, end = 100, step = 10, title= "Slider1")

def update_points(attrname, old, new):
        N = int(slider_widget.value)
        source.data = get_data(N)
slider_widget.on_change('value', update_points)

layout = column(row(slider_widget, width=400), row(p))

# add the layout to curdoc
curdoc().add_root(layout)