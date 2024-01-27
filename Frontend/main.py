from taipy.gui import Gui, notify

value = "10" 
content = "https://media1.tenor.com/m/P65vO2X2vPYAAAAC/polite-cat.gif"

page = """
Hey! Select a year and get a meme!

<|{value}|selector|lov=Item 1;Item 2;Item 3|dropdown|on_action=on_button_action>

<|{content}|image|>

"""

def on_button_action(state):
    (state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"


def on_change(state, var_name):
    if var_name == "item2":
        content = "https://media1.tenor.com/m/ZFLDdbp0zhEAAAAC/gif.gif"
        return


gui = Gui(page)
gui.run()
