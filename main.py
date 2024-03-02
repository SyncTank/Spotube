from SpotifyClientAuth import App_authentication
from InterfaceSpt import MainWindow
import dearpygui.dearpygui as dpg

# New_user = App_authentication()
# New_user.request_example()

#main_window = MainWindow()



def on_button_click(sender, app_data):
    input_text = dpg.get_value("input_text_tag")
    print(f"Button clicked! {input_text}")

def save_callback(reponse):
    print(f"Save Clicked")

dpg.create_context()

dpg.create_viewport(title='Spotube', width=200, height=200)

with dpg.window(tag="Primary Window"):
    dpg.add_text("Welcome to DearPyGui!")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string", tag="input_text_tag")
    dpg.add_button(label="Click Me", callback=on_button_click)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()