from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models.widgets import TextInput, Button, Paragraph

# create some widgets
input = TextInput(value="")
button = Button(label="Say Hi!")
output = Paragraph()

# add a callback to a widget
def update():
    output.text = "Hello, " + input.value
button.on_click(update)

# create a layout for everything
layout = column(input, button, output)

# add the layout to curdoc
curdoc().add_root(layout)